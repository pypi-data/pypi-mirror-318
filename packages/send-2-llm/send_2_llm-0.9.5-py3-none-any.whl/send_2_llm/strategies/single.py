"""Single provider strategy implementation."""

from typing import Optional, Any
import os

from ..types import (
    LLMResponse,
    LLMRequest,
    ProviderType,
    StrategyType,
    StrategyError,
    ProviderNotAvailableError,
)
from .base import BaseStrategy
from ..providers import get_provider


class SingleProviderStrategy(BaseStrategy):
    """Strategy for using a single provider."""
    
    def __init__(
        self,
        provider_type: Optional[ProviderType] = None,
        model: Optional[str] = None,
        **kwargs: Any
    ):
        """Initialize single provider strategy.
        
        Args:
            provider_type: Provider to use (defaults to default_provider)
            model: Model name to use
            **kwargs: Additional provider parameters
        """
        super().__init__(**kwargs)
        self.provider_type = provider_type
        self.model = model
        self.strategy_type = StrategyType.SINGLE

    async def execute(self, prompt: str) -> LLMResponse:
        """Execute strategy using single provider.
        
        Args:
            prompt: Input prompt
            
        Returns:
            LLMResponse with generated text and metadata
            
        Raises:
            StrategyError: If no provider available
        """
        # Use specified provider or default
        if not self.provider_type:
            raise StrategyError("No provider specified")
            
        try:
            # Get provider class and create instance
            provider_class = get_provider(self.provider_type)
            provider = provider_class(model=self.model)
            
            # Create request
            request = LLMRequest(
                prompt=prompt,
                provider_type=self.provider_type,
                model=self.model
            )
            
            # Execute request
            return await provider.generate(request)
            
        except Exception as e:
            raise ProviderNotAvailableError(f"Provider {self.provider_type} not available: {str(e)}") 