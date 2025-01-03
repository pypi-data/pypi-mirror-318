"""
OpenAI provider implementation v2.
Uses all settings from environment variables.
"""

import os
from typing import Optional, Dict, Any
import openai
from openai import AsyncClient
from datetime import datetime

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

class OpenAIProviderV2(BaseLLMProvider):
    """OpenAI API provider implementation with full env configuration."""
    
    def __init__(self):
        """Initialize OpenAI provider."""
        super().__init__()
        self.provider_type = ProviderType.OPENAI
        
        # Load config
        config = load_config()
        
        # Get model from env with fallback to config
        self.default_model = os.getenv(
            "OPENAI_MODEL",
            config.get("openai_model", "gpt-3.5-turbo")
        )
        
        # Get API key
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ProviderAPIError("OPENAI_API_KEY environment variable not set")
        
        # Get generation settings from env/config
        self.temperature = float(os.getenv(
            "TEMPERATURE",
            config.get("temperature", 0.7)
        ))
        self.top_p = float(os.getenv(
            "TOP_P",
            config.get("top_p", 0.95)
        ))
        self.max_tokens = int(os.getenv(
            "MAX_TOKENS",
            config.get("max_output_tokens", 1024)
        ))
        self.presence_penalty = float(os.getenv(
            "PRESENCE_PENALTY",
            config.get("presence_penalty", 0.0)
        ))
        self.frequency_penalty = float(os.getenv(
            "FREQUENCY_PENALTY",
            config.get("frequency_penalty", 0.0)
        ))
        
        # Initialize client
        self.client = AsyncClient(api_key=self.api_key)
    
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.OPENAI
    
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate text using OpenAI API."""
        try:
            start_time = datetime.now()
            
            # Use request parameters if provided, otherwise use defaults from env
            response = await self.client.chat.completions.create(
                model=request.model or self.default_model,
                messages=[{"role": "user", "content": request.prompt}],
                max_tokens=request.max_tokens or self.max_tokens,
                temperature=request.temperature or self.temperature,
                top_p=request.top_p or self.top_p,
                presence_penalty=self.presence_penalty,
                frequency_penalty=self.frequency_penalty
            )
            
            end_time = datetime.now()
            
            # Extract response text
            text = response.choices[0].message.content
            
            # Create token usage info
            response_dict = response.model_dump()
            token_usage = TokenUsage(
                prompt_tokens=response_dict["usage"]["prompt_tokens"],
                completion_tokens=response_dict["usage"]["completion_tokens"],
                total_tokens=response_dict["usage"]["total_tokens"]
            )
            
            # Calculate cost based on model and tokens
            model = response.model
            if "gpt-4" in model:
                prompt_cost = 0.03 * (token_usage.prompt_tokens / 1000)  # $0.03 per 1K tokens
                completion_cost = 0.06 * (token_usage.completion_tokens / 1000)  # $0.06 per 1K tokens
            else:  # gpt-3.5-turbo
                prompt_cost = 0.0015 * (token_usage.prompt_tokens / 1000)  # $0.0015 per 1K tokens
                completion_cost = 0.002 * (token_usage.completion_tokens / 1000)  # $0.002 per 1K tokens
            
            token_usage.cost = prompt_cost + completion_cost
            
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
            raise ProviderAPIError(f"OpenAI API error: {str(e)}") 