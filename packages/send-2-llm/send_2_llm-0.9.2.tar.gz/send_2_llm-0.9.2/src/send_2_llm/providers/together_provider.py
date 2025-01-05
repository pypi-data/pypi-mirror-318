"""
!!! WARNING - STABLE TOGETHER AI PROVIDER !!!
This is the stable Together AI provider implementation.
DO NOT MODIFY without explicit permission.
Commit: [COMMIT_HASH]
Tag: stable_together_v1

Critical functionality:
- Together AI provider initialization
- Chat completion generation
- System prompt handling via extra_params
- Error handling
- Token usage tracking
- Response metadata handling

Protected components:
- Default model configuration
- API client initialization
- Message formatting
- Response processing

Required dependencies:
- openai>=1.12.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0

Recovery instructions:
- To restore stable version: git checkout stable_together_v1
- Run tests: PYTHONPATH=src pytest tests/test_providers/test_together.py -v
- Verify all Together AI tests pass before any changes

Modification rules:
- All changes must maintain 95%+ test coverage
- No breaking changes to public interfaces
- Must pass all existing Together AI tests
- Document any dependency updates
- Create new test cases for new features
!!! WARNING !!!
"""

import os
import logging
from datetime import datetime
from typing import List, Optional, Dict, Any
from together import Together
import asyncio

from ..types import (
    ProviderType,
    LLMRequest,
    LLMResponse,
    LLMMetadata,
    TokenUsage,
    ProviderAPIError,
    ErrorDetails
)
from .base import BaseLLMProvider

logger = logging.getLogger(__name__)

class TogetherProvider(BaseLLMProvider):
    """Provider for Together AI models."""
    
    DEFAULT_MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
    PRIORITY = 80  # Medium-high priority
    IS_FALLBACK = True  # Can be used as fallback
    
    def __init__(self, model: Optional[str] = None, **kwargs: Any):
        """Initialize Together provider.
        
        Args:
            model: Model name to use (defaults to DEFAULT_MODEL)
            **kwargs: Additional provider parameters
        """
        super().__init__(provider_type=ProviderType.TOGETHER)
        
        # Get API key
        api_key = os.getenv("TOGETHER_API_KEY")
        if not api_key:
            raise ProviderAPIError("TOGETHER_API_KEY not found in environment variables")
            
        # Initialize Together client
        self.client = Together()
        
        # Set model with priority:
        # 1. model parameter from constructor
        # 2. TOGETHER_MODEL environment variable
        # 3. DEFAULT_MODEL constant
        env_model = os.getenv("TOGETHER_MODEL")
        if env_model:
            logger.info(f"Using model from TOGETHER_MODEL: {env_model}")
        self.model = model or env_model or self.DEFAULT_MODEL
        
        if self.model == self.DEFAULT_MODEL:
            logger.warning(
                f"Using default model {self.DEFAULT_MODEL}. "
                "Consider setting TOGETHER_MODEL environment variable."
            )
        
    def _get_generation_config(self, request: LLMRequest) -> Dict[str, Any]:
        """Get generation configuration from request."""
        config = {
            "temperature": request.temperature if request.temperature is not None else 0.7,
            "top_p": request.top_p if request.top_p is not None else 0.7,
            "top_k": request.top_k if request.top_k is not None else 50,
            "max_tokens": request.max_tokens if request.max_tokens is not None else 1024,
            "repetition_penalty": 1,
            "stop": ["<|eot_id|>", "<|eom_id|>"],
            "stream": False
        }
        return config
        
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using Together model."""
        try:
            # Use model from request, instance, or default
            model_name = request.model or self.model
            generation_config = self._get_generation_config(request)
            
            # Format messages
            messages = [{"role": "user", "content": request.prompt}]
            
            # Generate response
            response = self.client.chat.completions.create(
                model=model_name,
                messages=messages,
                **generation_config
            )
            
            # Extract response text
            text = response.choices[0].message.content
            
            # Create metadata
            metadata = LLMMetadata(
                provider=ProviderType.TOGETHER,
                model=model_name,
                usage=TokenUsage(
                    prompt_tokens=response.usage.prompt_tokens,
                    completion_tokens=response.usage.completion_tokens,
                    total_tokens=response.usage.total_tokens
                ),
                raw_response=response.model_dump()
            )
            
            return LLMResponse(
                text=text,
                metadata=metadata
            )
            
        except Exception as e:
            error_details = ErrorDetails(
                error_type="ProviderError",
                message=str(e),
                retryable=True
            )
            raise ProviderAPIError(f"Together API error: {e}", error_details=error_details)

    def _calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate cost based on token usage and model."""
        # Together pricing varies by model, using average cost for now
        # TODO: Add model-specific pricing
        input_cost = 0.0002 * (prompt_tokens / 1000)  # $0.0002 per 1K input tokens
        output_cost = 0.0002 * (completion_tokens / 1000)  # $0.0002 per 1K output tokens
        return input_cost + output_cost

    async def list_models(self) -> List[str]:
        """List available models."""
        try:
            models = self.client.models.list()
            return [m.id for m in models]
        except Exception as e:
            logger.error(f"Failed to list models: {str(e)}")
            return [] 