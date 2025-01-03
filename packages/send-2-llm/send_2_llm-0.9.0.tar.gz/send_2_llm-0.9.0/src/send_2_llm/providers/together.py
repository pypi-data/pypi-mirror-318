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
from typing import Optional, Dict, Any
import openai
from openai import AsyncOpenAI
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


# !!! STABLE CLASS - DO NOT MODIFY !!!
class TogetherProvider(BaseLLMProvider):
    """Together AI API provider implementation."""
    
    def __init__(self):
        """Initialize Together AI provider.
        
        Raises:
            ProviderAPIError: If TOGETHER_API_KEY is not set
        """
        super().__init__()
        self.provider_type = ProviderType.TOGETHER
        self.default_model = os.getenv(
            "TOGETHER_MODEL", 
            "meta-llama/Llama-Vision-Free"  # Default model - DO NOT MODIFY
        )
        self.api_key = os.getenv("TOGETHER_API_KEY")
        
        if not self.api_key:
            raise ProviderAPIError(
                "TOGETHER_API_KEY environment variable not set",
                provider=self.provider_type
            )
        
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.together.xyz/v1",  # API endpoint - DO NOT MODIFY
        )
    
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.TOGETHER
    
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate text using Together AI API.
        
        Args:
            request: Request parameters including prompt, model, etc.
                To use system prompt, pass it in extra_params:
                extra_params={"system_prompt": "Your system prompt here"}
            
        Returns:
            LLMResponse with generated text and metadata
        """
        try:
            start_time = datetime.now()
            
            # Get system prompt from extra_params if provided
            extra_params = request.extra_params or {}
            system_prompt = extra_params.pop("system_prompt", None)
            
            # Prepare messages
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": request.prompt})
            
            # Make API call
            response = await self.client.chat.completions.create(
                model=request.model or self.default_model,
                messages=messages,
                max_tokens=request.max_tokens,
                temperature=request.temperature,
                top_p=request.top_p,
                **extra_params
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
            # Together AI pricing: $0.0004 per 1K tokens for most models
            cost_per_1k = 0.0004
            token_usage.cost = cost_per_1k * (token_usage.total_tokens / 1000)
            
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
            raise ProviderAPIError(f"Together AI error: {str(e)}") 