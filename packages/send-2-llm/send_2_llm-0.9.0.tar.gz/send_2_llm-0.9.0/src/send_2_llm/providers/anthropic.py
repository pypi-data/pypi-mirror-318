"""
Anthropic provider implementation.
Supports Claude 3 models with text generation capabilities.
"""

import os
from typing import Optional, Dict, Any
from datetime import datetime
from anthropic import AsyncAnthropic

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


class AnthropicProvider(BaseLLMProvider):
    """Anthropic API provider implementation."""
    
    def __init__(self):
        """Initialize Anthropic provider."""
        super().__init__()
        self.provider_type = ProviderType.ANTHROPIC
        
        # Load config
        config = load_config()
        self.default_model = config.get("anthropic_model", "claude-3-haiku-20240307")
        self.default_max_tokens = config.get("max_output_tokens", 1024)
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            raise ProviderAPIError("ANTHROPIC_API_KEY environment variable not set", provider=self.provider_type)
        
        # Validate model name
        valid_models = [
            # Claude 3.5 Models (Latest Generation)
            "claude-3-5-sonnet-20241022",
            "claude-3-5-sonnet-latest",
            "claude-3-5-haiku-20241022",
            "claude-3-5-haiku-latest",
            
            # Claude 3 Models
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307"
        ]
        
        if self.default_model not in valid_models:
            raise ProviderAPIError(
                f"Invalid model name: {self.default_model}. Must be one of: {', '.join(valid_models)}",
                provider=self.provider_type
            )
        
        self.client = AsyncAnthropic(api_key=self.api_key)
    
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.ANTHROPIC
    
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate text using Anthropic API."""
        try:
            start_time = datetime.now()
            
            # Get extra parameters
            extra_params = request.extra_params or {}
            system_prompt = extra_params.pop("system_prompt", None)
            
            # Prepare messages
            messages = []
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            messages.append({
                "role": "user",
                "content": request.prompt
            })
            
            # Make API call
            response = await self.client.messages.create(
                model=request.model or self.default_model,
                messages=messages,
                max_tokens=request.max_tokens or self.default_max_tokens,
                temperature=request.temperature,
                top_p=request.top_p,
                **extra_params
            )
            
            end_time = datetime.now()
            
            # Extract response text
            text = response.content[0].text
            
            # Create token usage info
            response_dict = response.model_dump()
            token_usage = TokenUsage(
                prompt_tokens=response_dict["usage"]["input_tokens"],
                completion_tokens=response_dict["usage"]["output_tokens"],
                total_tokens=response_dict["usage"]["input_tokens"] + response_dict["usage"]["output_tokens"]
            )
            
            # Calculate cost based on model and tokens
            model = response.model
            if "claude-3-opus" in model:
                input_cost = 0.015 * (token_usage.prompt_tokens / 1000)  # $0.015 per 1K input tokens
                output_cost = 0.075 * (token_usage.completion_tokens / 1000)  # $0.075 per 1K output tokens
            elif "claude-3-sonnet" in model:
                input_cost = 0.003 * (token_usage.prompt_tokens / 1000)  # $0.003 per 1K input tokens
                output_cost = 0.015 * (token_usage.completion_tokens / 1000)  # $0.015 per 1K output tokens
            else:  # claude-3-haiku
                input_cost = 0.00025 * (token_usage.prompt_tokens / 1000)  # $0.00025 per 1K input tokens
                output_cost = 0.00125 * (token_usage.completion_tokens / 1000)  # $0.00125 per 1K output tokens
            
            token_usage.cost = input_cost + output_cost
            
            # Create metadata
            metadata = LLMMetadata(
                provider=self.provider_type,
                model=response.model,
                created_at=start_time,
                usage=token_usage,
                raw_response=response_dict,
                latency=(end_time - start_time).total_seconds()
            )
            
            return LLMResponse(
                text=text,
                metadata=metadata
            )
            
        except Exception as e:
            raise ProviderAPIError(f"Anthropic API error: {str(e)}") 