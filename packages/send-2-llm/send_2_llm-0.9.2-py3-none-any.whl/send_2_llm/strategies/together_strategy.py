"""Together AI strategy implementation."""

import os
from typing import Optional, Any, Dict
from openai import AsyncOpenAI

from ..types import (
    LLMResponse,
    LLMMetadata,
    TokenUsage,
    ProviderType,
    StrategyType,
    StrategyError,
)


class TogetherStrategy:
    """Simple strategy for Together AI."""
    
    def __init__(
        self,
        model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1",
        api_key: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 512,
        top_p: float = 0.95,
        system_prompt: str = "You are a helpful assistant.",
        **kwargs: Any,
    ):
        """Initialize Together AI strategy.
        
        Args:
            model: Model name to use
            api_key: Together AI API key (defaults to TOGETHER_API_KEY env var)
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            top_p: Nucleus sampling parameter
            system_prompt: System prompt for the model
            **kwargs: Additional parameters
        """
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.system_prompt = system_prompt
        self.kwargs = kwargs
        
        # Setup API client
        self.api_key = api_key or os.getenv("TOGETHER_API_KEY")
        if not self.api_key:
            raise ValueError("Together AI API key not found")
            
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.together.xyz/v1",
        )
        
    async def generate(self, prompt: str) -> LLMResponse:
        """Generate text using Together AI.
        
        Args:
            prompt: Input prompt
            
        Returns:
            LLMResponse with generated text and metadata
            
        Raises:
            StrategyError: On API errors
        """
        try:
            # Create completion
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                **self.kwargs
            )
            
            # Extract response text
            text = response.choices[0].message.content
            
            # Create response metadata
            usage = TokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
                cost=0.0,  # Together AI pricing can be added here
            )
            
            metadata = LLMMetadata(
                provider=ProviderType.TOGETHER,
                model=self.model,
                usage=usage,
                raw_response=response.model_dump(),
                strategy=StrategyType.SINGLE,
            )
            
            return LLMResponse(text=text, metadata=metadata)
            
        except Exception as e:
            raise StrategyError(f"Together AI strategy failed: {str(e)}")
            
    async def close(self):
        """Close client connection."""
        await self.client.close() 