"""
⚠️ STABLE COMPONENT - DO NOT MODIFY ⚠️

This is a stable version of OpenAI provider implementation.
Tag: stable_openai_v1
Commit: b25d24a
Coverage: 96%

Protected functionality:
- Provider initialization
- Chat completion generation
- Error handling
- Token usage tracking
- Response metadata handling

To modify:
1. Get explicit permission
2. Create new file
3. Follow STABLE_COMPONENTS.md

⚠️ ANY CHANGES MUST BE APPROVED ⚠️
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

# !!! STABLE IMPLEMENTATION - DO NOT MODIFY !!!
class OpenAIProvider(BaseLLMProvider):
    """OpenAI API provider implementation."""
    
    def __init__(self):
        """Initialize OpenAI provider."""
        super().__init__()
        self.provider_type = ProviderType.OPENAI
        self.default_model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ProviderAPIError("OPENAI_API_KEY environment variable not set")
        
        self.client = AsyncClient(api_key=self.api_key)
    
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.OPENAI
    
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate text using OpenAI API."""
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