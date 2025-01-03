"""
!!! WARNING - STABLE BASE PROVIDER !!!
This is the base provider class used by OpenAI implementation.
DO NOT MODIFY without explicit permission.
Commit: b25d24a
Tag: stable_openai_v1

Critical functionality:
- Base provider interface
- Abstract generate method
- Type definitions

Dependencies:
- OpenAI provider inherits from this
- All provider implementations depend on this
!!! WARNING !!!
"""

import os
import logging
from abc import ABC, abstractmethod
from typing import Optional, List
import uuid
import time

from ..types import LLMRequest, LLMResponse, ProviderType, RelatedQuestionsConfig, RelatedQuestionsRequest, RelatedQuestionsResponse, RelatedQuestion
from ..logging.api import api_logger
from ..logging.metrics import metrics_logger, timing_decorator

# Настройка логирования
logger = logging.getLogger(__name__)
if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

class BaseLLMProvider(ABC):
    """Base class for LLM providers."""
    
    def __init__(self):
        """Initialize provider."""
        self.provider_type = self._get_provider_type()
    
    @abstractmethod
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        pass
    
    @timing_decorator("llm_generate")
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response from LLM provider.
        
        Args:
            request: LLM request
            
        Returns:
            LLM response
            
        Raises:
            ProviderAPIError: If provider API call fails
        """
        # Generate request ID
        request_id = str(uuid.uuid4())
        start_time = time.time()
        
        try:
            # Log API request
            api_logger.log_request(
                provider=self.provider_type.value,
                endpoint="/generate",
                method="POST",
                request_id=request_id,
                payload={
                    "prompt": request.prompt,
                    "parameters": {
                        "model": request.model,
                        "max_tokens": request.max_tokens,
                        "temperature": request.temperature,
                        "top_p": request.top_p,
                        "stop": request.stop,
                        "extra_params": request.extra_params
                    }
                }
            )
            
            # Call provider-specific implementation
            response = await self._generate(request)
            duration = time.time() - start_time
            
            # Log successful response
            api_logger.log_response(
                provider=self.provider_type.value,
                endpoint="/generate",
                method="POST",
                request_id=request_id,
                status_code=200,
                response_time=duration,
                response_data={
                    "text": response.text,
                    "metadata": response.metadata.dict()
                }
            )
            
            # Log token usage
            if response.metadata.usage:
                metrics_logger.log_token_usage(
                    provider=self.provider_type.value,
                    prompt_tokens=response.metadata.usage.prompt_tokens,
                    completion_tokens=response.metadata.usage.completion_tokens,
                    total_tokens=response.metadata.usage.total_tokens,
                    cost=response.metadata.usage.cost,
                    model=response.metadata.model
                )
            
            return response
            
        except Exception as e:
            # Log error response
            api_logger.log_response(
                provider=self.provider_type.value,
                endpoint="/generate",
                method="POST",
                request_id=request_id,
                status_code=500,
                response_time=time.time() - start_time,
                error=str(e)
            )
            
            # Log error metrics
            metrics_logger.log_error(
                error_type=type(e).__name__,
                error_message=str(e),
                provider=self.provider_type.value,
                endpoint="/generate"
            )
            
            raise
    
    @abstractmethod
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Provider-specific implementation of generate method."""
        pass

    async def generate_related_questions(
        self,
        original_question: str,
        config: Optional[RelatedQuestionsConfig] = None
    ) -> List[str]:
        """Generate related questions for the given question."""
        if not config:
            config = RelatedQuestionsConfig()
            
        if not config.enabled:
            return []
            
        try:
            # Создаем запрос для генерации вопросов
            request = LLMRequest(
                prompt=config.generator.format_prompt(original_question),
                temperature=config.generator.temperature,
                max_tokens=300,  # Достаточно для нескольких вопросов
                extra_params={
                    "system_prompt": config.generator.system_prompt
                }
            )
            
            # Получаем ответ от модели
            response = await self.generate(request)
            
            # Парсим ответ в список вопросов
            questions = config.generator.parse_response(response.text)
            
            logger.debug(f"Generated {len(questions)} related questions")
            return questions
            
        except Exception as e:
            logger.warning(f"Failed to generate related questions: {str(e)}")
            return [] 

    async def get_related_questions(
        self,
        request: RelatedQuestionsRequest
    ) -> RelatedQuestionsResponse:
        """Get related questions through universal API."""
        try:
            # Получаем вопросы через базовый метод
            raw_questions = await self.generate_related_questions(
                request.original_question,
                request.config
            )
            
            # Преобразуем в структурированный формат
            questions = [
                RelatedQuestion(
                    text=q,
                    confidence=1.0,
                    source="generated",
                    metadata={}
                )
                for q in raw_questions
            ]
            
            # Фильтруем по уверенности и ограничиваем количество
            filtered_questions = [
                q for q in questions 
                if q.confidence >= request.min_confidence
            ][:request.max_questions]
            
            return RelatedQuestionsResponse(
                questions=filtered_questions,
                metadata={
                    "provider": self.provider_type,
                    "total_generated": len(raw_questions),
                    "filtered_out": len(raw_questions) - len(filtered_questions)
                }
            )
            
        except Exception as e:
            logger.error(f"Error getting related questions: {str(e)}")
            return RelatedQuestionsResponse(
                questions=[],
                metadata={
                    "error": str(e),
                    "provider": self.provider_type
                }
            ) 