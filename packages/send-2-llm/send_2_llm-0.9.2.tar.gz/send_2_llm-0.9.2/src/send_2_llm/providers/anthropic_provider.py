"""Anthropic provider implementation."""

import os
import logging
from typing import Optional, Dict, Any
from datetime import datetime
from anthropic import AsyncAnthropic

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

class AnthropicProvider(BaseLLMProvider):
    """Anthropic API provider implementation."""
    
    DEFAULT_MODEL = "claude-3-haiku-20240307"
    PRIORITY = 90  # High priority but below OpenAI
    IS_FALLBACK = True  # Can be used as fallback
    
    def __init__(self, model: Optional[str] = None, **kwargs: Any):
        """Initialize Anthropic provider.
        
        Args:
            model: Model name to use (defaults to ANTHROPIC_MODEL env var or DEFAULT_MODEL)
            **kwargs: Additional provider parameters
        """
        super().__init__(provider_type=ProviderType.ANTHROPIC)
        
        # Get API key
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ProviderAPIError("ANTHROPIC_API_KEY not found in environment variables")
            
        # Initialize client
        self.client = AsyncAnthropic(api_key=api_key)
        
        # Set model with priority:
        # 1. model parameter from constructor
        # 2. ANTHROPIC_MODEL environment variable
        # 3. DEFAULT_MODEL constant
        env_model = os.getenv("ANTHROPIC_MODEL")
        if env_model:
            logger.info(f"Using model from ANTHROPIC_MODEL: {env_model}")
        self.model = model or env_model or self.DEFAULT_MODEL
        
        if self.model == self.DEFAULT_MODEL:
            logger.warning(
                f"Using default model {self.DEFAULT_MODEL}. "
                "Consider setting ANTHROPIC_MODEL environment variable."
            )
        
        # Validate model name
        self.valid_models = [
            # Claude 3.5 Models (Latest Generation)
            "claude-3-5-sonnet-20241022",
            "claude-3-5-sonnet-latest",
            "claude-3-5-haiku-20241022",
            "claude-3-5-haiku-latest",
            
            # Claude 3 Models
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307"
        ]
        
        if self.model not in self.valid_models:
            logger.warning(f"Model {self.model} not in list of known models: {', '.join(self.valid_models)}")
        
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
        """Generate response using Anthropic model."""
        try:
            # Use model from request, instance, or default
            model_name = request.model or self.model
            generation_config = self._get_generation_config(request)
            
            # Generate response
            response = await self.client.messages.create(
                model=model_name,
                messages=[{"role": "user", "content": request.prompt}],
                **generation_config
            )
            
            # Extract response text
            text = response.content[0].text
            
            # Create metadata
            metadata = LLMMetadata(
                provider=ProviderType.ANTHROPIC,
                model=model_name,
                usage=TokenUsage(
                    prompt_tokens=response.usage.input_tokens,
                    completion_tokens=response.usage.output_tokens,
                    total_tokens=response.usage.input_tokens + response.usage.output_tokens
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
            raise ProviderAPIError(f"Anthropic API error: {e}", error_details=error_details)

    def _calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate cost based on token usage and model."""
        # Anthropic pricing varies by model
        # Using Claude 3 Haiku rates as default
        input_cost = 0.00025 * (prompt_tokens / 1000)  # $0.00025 per 1K input tokens
        output_cost = 0.00075 * (completion_tokens / 1000)  # $0.00075 per 1K output tokens
        return input_cost + output_cost 