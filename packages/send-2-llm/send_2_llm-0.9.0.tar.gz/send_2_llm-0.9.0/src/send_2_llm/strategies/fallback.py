"""Fallback strategy implementation."""

from typing import List, Optional, Any

from ..types import (
    LLMResponse,
    LLMRequest,
    ProviderType,
    StrategyType,
    StrategyError,
    ProviderAPIError,
)
from .base import BaseStrategy


class FallbackStrategy(BaseStrategy):
    """Strategy that tries multiple providers in sequence."""
    
    def __init__(
        self,
        providers: List[ProviderType],
        models: Optional[List[str]] = None,
        **kwargs: Any
    ):
        """Initialize fallback strategy.
        
        Args:
            providers: List of providers to try in order
            models: Optional list of models (must match providers length)
            **kwargs: Additional provider parameters
        """
        super().__init__(providers=providers, **kwargs)
        
        if not providers:
            raise ValueError("At least one provider must be specified")
            
        if models and len(models) != len(providers):
            raise ValueError("Number of models must match number of providers")
            
        self.models = models or [None] * len(providers)
        self.strategy_type = StrategyType.FALLBACK

    async def execute(self, prompt: str) -> LLMResponse:
        """Execute strategy trying providers in sequence.
        
        Args:
            prompt: Input prompt
            
        Returns:
            LLMResponse with generated text and metadata
            
        Raises:
            StrategyError: If all providers fail
        """
        errors = []
        
        # Try each provider in sequence
        for provider_type, model in zip(self.providers, self.models):
            try:
                provider = self._create_provider(
                    provider_type=provider_type,
                    model=model,
                )
                
                # Create request object
                request = LLMRequest(
                    prompt=prompt,
                    provider_type=provider_type,
                    model=model,
                    strategy=self.strategy_type,
                    **self.kwargs
                )
                
                response = await provider.generate(request)
                
                # Add strategy info to metadata
                if response.metadata:
                    response.metadata.strategy = self.strategy_type
                    
                return response
                
            except Exception as e:
                errors.append(f"{provider_type}: {str(e)}")
                continue
                
        # All providers failed
        raise StrategyError(
            f"All providers failed: {'; '.join(errors)}"
        ) 