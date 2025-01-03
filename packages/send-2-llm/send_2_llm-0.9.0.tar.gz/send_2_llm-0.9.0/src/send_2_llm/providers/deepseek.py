"""
DeepSeek provider implementation.
Compatible with OpenAI SDK.
Base URL: https://api.deepseek.com
"""

import os
from typing import Optional, Dict, Any
from datetime import datetime
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


class DeepSeekProvider(BaseLLMProvider):
    """DeepSeek API provider implementation."""
    
    def __init__(self):
        """Initialize DeepSeek provider."""
        super().__init__()
        self.provider_type = ProviderType.DEEPSEEK
        self.default_model = "deepseek-chat"
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        
        if not self.api_key:
            raise ProviderAPIError("DEEPSEEK_API_KEY environment variable not set")
        
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com"
        )
    
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.DEEPSEEK
    
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate text using DeepSeek API."""
        try:
            start_time = datetime.now()
            
            response = await self.client.chat.completions.create(
                model=request.model or self.default_model,
                messages=[{"role": "user", "content": request.prompt}],
                max_tokens=request.max_tokens,
                temperature=request.temperature,
                top_p=request.top_p
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
            
            # Create metadata
            metadata = LLMMetadata(
                provider=self.provider_type,
                model=response.model,
                created_at=start_time,
                usage=token_usage,
                raw_response=response_dict
            )
            
            return LLMResponse(
                text=text,
                metadata=metadata
            )
            
        except Exception as e:
            raise ProviderAPIError(f"DeepSeek API error: {str(e)}") 