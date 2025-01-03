"""
Google Gemini provider using new Google Gen AI SDK.
https://github.com/googleapis/python-genai
"""

import os
from datetime import datetime
from typing import Optional, Dict, Any
import asyncio

from google import genai
from google.genai import types as genai_types

from send_2_llm.types import (
    LLMRequest,
    LLMResponse,
    LLMMetadata,
    ProviderType,
    TokenUsage,
    ProviderAPIError
)
from .base import BaseLLMProvider

class GeminiProvider(BaseLLMProvider):
    """Google Gemini provider using official SDK."""

    def __init__(self):
        """Initialize Gemini provider with API key."""
        super().__init__()
        self.provider_type = ProviderType.GEMINI
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ProviderAPIError("GEMINI_API_KEY environment variable not set")

        # Get model name from env
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro-latest")
        
        # Initialize client
        try:
            self.client = genai.Client(api_key=self.api_key)
        except Exception as e:
            raise ProviderAPIError(f"Failed to initialize Gemini client: {str(e)}")

    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.GEMINI

    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using Gemini API."""
        try:
            start_time = datetime.now()

            # Get extra parameters
            extra_params = request.extra_params or {}
            system_instruction = extra_params.pop("system_instruction", None)
            
            # Prepare generation config
            config = genai_types.GenerateContentConfig(
                temperature=request.temperature,
                top_p=request.top_p,
                top_k=extra_params.get("top_k", 40),
                max_output_tokens=request.max_tokens or 2048,
                candidate_count=extra_params.get("candidate_count", 1),
                stop_sequences=request.stop or []
            )

            # Add system instruction if provided
            if system_instruction:
                config.system_instruction = system_instruction

            # Send request and get response
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: self.client.models.generate_content(
                    model=self.model_name,
                    contents=request.prompt,
                    config=config
                )
            )

            # Calculate latency
            end_time = datetime.now()
            latency = (end_time - start_time).total_seconds()

            # Get response text
            text = response.text

            # Store raw response
            raw_response = {
                "model": self.model_name,
                "text": text,
                "candidates": response.candidates,
                "generation_config": config.dict()
            }

            # Estimate token usage (Gemini doesn't provide token counts)
            # Using rough estimation based on words
            prompt_words = len(request.prompt.split())
            completion_words = len(text.split())
            
            # Estimate tokens (avg 1.3 tokens per word)
            prompt_tokens = int(prompt_words * 1.3)
            completion_tokens = int(completion_words * 1.3)
            total_tokens = prompt_tokens + completion_tokens
            
            # Calculate cost (Gemini Pro pricing: $0.00025 per 1K tokens)
            cost = 0.00025 * (total_tokens / 1000)

            return LLMResponse(
                text=text,
                metadata=LLMMetadata(
                    provider=self.provider_type,
                    model=self.model_name,
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

        except Exception as e:
            raise ProviderAPIError(f"Gemini API error: {str(e)}") 