"""
OpenAI provider implementation v2.
Uses all settings from environment variables.
"""

import os
from typing import Optional, Dict, Any
import openai
from openai import AsyncClient
from datetime import datetime
import logging

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
from ..config import load_config

logger = logging.getLogger(__name__)

class OpenAIProviderV2(BaseLLMProvider):
    """OpenAI API provider implementation."""
    
    DEFAULT_MODEL = "gpt-3.5-turbo"
    PRIORITY = 100  # Highest priority provider
    IS_FALLBACK = True  # Can be used as fallback
    
    def __init__(self, model: Optional[str] = None, **kwargs: Any):
        """Initialize OpenAI provider.
        
        Args:
            model: Model name to use (defaults to DEFAULT_MODEL)
            **kwargs: Additional provider parameters
        """
        super().__init__(provider_type=ProviderType.OPENAI)
        
        # Get API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ProviderAPIError("OPENAI_API_KEY not found in environment variables")
            
        # Initialize client
        self.client = AsyncClient(api_key=api_key)
        
        # Set model with priority:
        # 1. model parameter from constructor
        # 2. OPENAI_MODEL environment variable
        # 3. DEFAULT_MODEL constant
        env_model = os.getenv("OPENAI_MODEL")
        if env_model:
            logger.info(f"Using model from OPENAI_MODEL: {env_model}")
        self.model = model or env_model or self.DEFAULT_MODEL
        
        if self.model == self.DEFAULT_MODEL:
            logger.warning(
                f"Using default model {self.DEFAULT_MODEL}. "
                "Consider setting OPENAI_MODEL environment variable."
            )
        
    def _get_generation_config(self, request: LLMRequest) -> Dict[str, Any]:
        """Get generation configuration from request."""
        config = {
            "temperature": request.temperature if request.temperature is not None else 0.7,
            "top_p": request.top_p if request.top_p is not None else 0.7,
            "max_tokens": request.max_tokens if request.max_tokens is not None else 1024,
            "stream": False
        }
        return config
        
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using OpenAI model."""
        try:
            # Use model from request, instance, or default
            model_name = request.model or self.model
            generation_config = self._get_generation_config(request)
            
            # Format messages
            messages = [{"role": "user", "content": request.prompt}]
            
            # Generate response
            response = await self.client.chat.completions.create(
                model=model_name,
                messages=messages,
                **generation_config
            )
            
            # Extract response text
            text = response.choices[0].message.content
            
            # Create metadata
            metadata = LLMMetadata(
                provider=ProviderType.OPENAI,
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
            raise ProviderAPIError(f"OpenAI API error: {e}", error_details=error_details)

    def _calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate cost based on token usage and model."""
        # OpenAI pricing varies by model, using gpt-3.5-turbo rates for now
        # TODO: Add model-specific pricing
        input_cost = 0.0015 * (prompt_tokens / 1000)  # $0.0015 per 1K input tokens
        output_cost = 0.002 * (completion_tokens / 1000)  # $0.002 per 1K output tokens
        return input_cost + output_cost 