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
from typing import Optional, List, Callable, Any, Coroutine, TypeVar, Dict
import uuid
import time
import asyncio
from datetime import datetime

from ..types import LLMRequest, LLMResponse, ProviderType, RelatedQuestionsConfig, RelatedQuestionsRequest, RelatedQuestionsResponse, RelatedQuestion, RetryConfig, ErrorDetails, ProviderAPIError
from ..logging.api import api_logger
from ..logging.metrics import metrics_logger, timing_decorator
from ..constants import config_manager, PriceConfig

# Настройка логирования
logger = logging.getLogger(__name__)
if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

T = TypeVar('T')

class BaseLLMProvider(ABC):
    """Base class for LLM providers."""
    
    def __init__(self, provider_type: ProviderType):
        self.provider_type = provider_type
        self.config_manager = config_manager
    
    def get_model_price(self, model: str, source: str = "direct") -> PriceConfig:
        """Get pricing for the specified model.
        
        Args:
            model: Model name
            source: Source of the model (direct/together/etc)
            
        Returns:
            PriceConfig with model pricing
            
        Raises:
            ValueError: If pricing not found
        """
        try:
            price_data = self.config_manager.get_model_price(
                provider=self.provider_type.value,
                source=source,
                model=model
            )
            if isinstance(price_data, dict) and "prices" in price_data:
                prices = price_data["prices"]
                return PriceConfig(
                    prompt=prices.get("prompt", 0.0),
                    completion=prices.get("completion", 0.0)
                )
            return PriceConfig(prompt=0.0, completion=0.0)
        except ValueError as e:
            logger.warning(f"No pricing found for {model} via {source}: {e}")
            return PriceConfig(prompt=0.0, completion=0.0)
    
    def get_model_features(self, model: str) -> Dict[str, bool]:
        """Get features supported by the model.
        
        Args:
            model: Model name
            
        Returns:
            Dict of feature flags
            
        Raises:
            ValueError: If features not found
        """
        try:
            return self.config_manager.get_model_features(
                provider=self.provider_type.value,
                model=model
            )
        except ValueError as e:
            logger.warning(f"No features found for {model}: {e}")
            return {}
    
    def get_system_prompt(self, prompt_type: str) -> str:
        """Get system prompt by type.
        
        Args:
            prompt_type: Type of system prompt
            
        Returns:
            System prompt text
            
        Raises:
            ValueError: If prompt not found
        """
        try:
            return self.config_manager.get_system_prompt(prompt_type)
        except ValueError as e:
            logger.warning(f"No system prompt found for {prompt_type}: {e}")
            return ""
    
    @abstractmethod
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response for the given request.
        
        This method should be implemented by each provider to handle the actual API call.
        """
        pass

    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response with retries and error handling."""
        return await self._handle_request_with_retries(
            request,
            lambda: self._generate(request)
        )
    
    async def _handle_request_with_retries(
        self,
        request: LLMRequest,
        operation: Callable[[], Coroutine[Any, Any, T]]
    ) -> T:
        """Handle request with retries and error handling.
        
        Args:
            request: The LLM request containing retry configuration
            operation: The async operation to execute with retries
            
        Returns:
            The result of the operation
            
        Raises:
            ProviderAPIError: If the operation fails after all retries
        """
        retry_count = 0
        retry_config = request.retry_config or RetryConfig()
        
        while True:
            try:
                return await operation()
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                # Create error details
                error_details = ErrorDetails(
                    error_type=error_type,
                    message=error_msg,
                    retryable=error_type in retry_config.retry_on_errors
                )
                
                # Check if we should retry
                if (error_details.retryable and 
                    retry_count < retry_config.max_retries):
                    retry_count += 1
                    delay = min(
                        retry_config.initial_delay * (retry_config.exponential_base ** retry_count),
                        retry_config.max_delay
                    )
                    
                    logger.warning(
                        f"Retryable error occurred ({error_type}). "
                        f"Retrying in {delay:.1f}s (attempt {retry_count}/{retry_config.max_retries})"
                    )
                    
                    await asyncio.sleep(delay)
                    continue
                
                # If we get here, error is not retryable or we're out of retries
                logger.error(f"{self.provider_type} API error: {error_msg}")
                raise ProviderAPIError(
                    f"{self.provider_type} API error: {error_msg}",
                    provider=self.provider_type
                ) from e

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