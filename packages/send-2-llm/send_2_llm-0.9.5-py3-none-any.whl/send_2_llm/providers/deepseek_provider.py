"""
DeepSeek provider implementation.
Uses OpenAI SDK with custom base_url for API compatibility.
"""

import os
import logging
from datetime import datetime
from typing import List, Optional, Dict, Any
from openai import AsyncOpenAI

from ..types import (
    ProviderType,
    LLMRequest,
    LLMResponse,
    LLMMetadata,
    TokenUsage,
    ProviderAPIError
)
from .base import BaseLLMProvider
from ..config import load_config

logger = logging.getLogger(__name__)

class DeepSeekProvider(BaseLLMProvider):
    """DeepSeek provider implementation."""
    
    DEFAULT_MODEL = "deepseek-chat"
    PRIORITY = 60  # Medium-low priority
    IS_FALLBACK = False  # Not recommended as fallback
    
    def __init__(self, **kwargs):
        """Initialize DeepSeek provider."""
        super().__init__(provider_type=ProviderType.DEEPSEEK)
        
        # Load config
        config = load_config()
        
        # Set model with priority:
        # 1. model parameter from constructor
        # 2. DEEPSEEK_MODEL environment variable
        # 3. DEFAULT_MODEL constant
        env_model = os.getenv("DEEPSEEK_MODEL")
        if env_model:
            logger.info(f"Using model from DEEPSEEK_MODEL: {env_model}")
        self.model = kwargs.get('model') or env_model or self.DEFAULT_MODEL
        
        if self.model == self.DEFAULT_MODEL:
            logger.warning(
                f"Using default model {self.DEFAULT_MODEL}. "
                "Consider setting DEEPSEEK_MODEL environment variable."
            )
            
        self.max_output_tokens = config.get("max_output_tokens", 4096)
        
        # Get API key and base URL
        api_key = os.getenv("DEEPSEEK_API_KEY")
        base_url = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
        
        if not api_key:
            raise ProviderAPIError(
                "DEEPSEEK_API_KEY environment variable not set",
                provider=self.provider_type
            )
            
        # Initialize client
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using DeepSeek API."""
        # Get default values from env or use provider defaults
        default_temperature = float(os.getenv("TEMPERATURE", "0.1"))
        default_top_p = float(os.getenv("DEFAULT_TOP_P", "1.0"))
        default_token_ratio = float(os.getenv("TOKEN_ESTIMATION_RATIO", "1.3"))
        
        # Prepare messages
        messages = []
        if request.extra_params and "system_prompt" in request.extra_params:
            messages.append({
                "role": "system",
                "content": request.extra_params["system_prompt"]
            })
        messages.append({
            "role": "user",
            "content": request.prompt
        })
        
        # Prepare generation config
        generation_config = {
            "model": self.model,
            "messages": messages,
            "temperature": request.temperature or default_temperature,
            "top_p": request.top_p or default_top_p,
            "max_tokens": request.max_tokens or self.max_output_tokens,
        }

        # Add any extra provider-specific parameters
        if request.extra_params:
            extra_params = request.extra_params.copy()
            extra_params.pop("system_prompt", None)  # Remove system prompt as it's handled above
            generation_config.update(extra_params)

        # Send request and get response
        logger.debug(f"Sending request to DeepSeek API: {request.prompt[:100]}...")
        start_time = datetime.now()
        
        response = await self.client.chat.completions.create(**generation_config)
        logger.debug("Received response from DeepSeek API")

        # Calculate latency
        end_time = datetime.now()
        latency = (end_time - start_time).total_seconds()

        # Get response text
        text = response.choices[0].message.content

        # Store raw response
        raw_response = {
            "model": self.model,
            "text": text,
            "generation_config": generation_config,
            "raw": response.model_dump()
        }

        # Get token usage from response
        usage = response.usage
        prompt_tokens = usage.prompt_tokens
        completion_tokens = usage.completion_tokens
        total_tokens = usage.total_tokens

        # Calculate cost based on token usage
        cost = self._calculate_cost(prompt_tokens, completion_tokens)

        return LLMResponse(
            text=text,
            metadata=LLMMetadata(
                provider=self.provider_type,
                model=self.model,
                usage=TokenUsage(
                    prompt_tokens=prompt_tokens,
                    completion_tokens=completion_tokens,
                    total_tokens=total_tokens,
                    cost=cost
                ),
                raw_response=raw_response,
                created_at=end_time,
                latency=latency
            )
        )

    def _calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate cost based on token usage and model."""
        # DeepSeek pricing varies by model, using average cost for now
        # TODO: Add model-specific pricing
        input_cost = 0.0002 * (prompt_tokens / 1000)  # $0.0002 per 1K input tokens
        output_cost = 0.0002 * (completion_tokens / 1000)  # $0.0002 per 1K output tokens
        return input_cost + output_cost

    async def list_models(self) -> List[str]:
        """List available models."""
        try:
            models = await self.client.models.list()
            return [m.id for m in models.data]
        except Exception as e:
            logger.error(f"Failed to list models: {str(e)}")
            return [] 