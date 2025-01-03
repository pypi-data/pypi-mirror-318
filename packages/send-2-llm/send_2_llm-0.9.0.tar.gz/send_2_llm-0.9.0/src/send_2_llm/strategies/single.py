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
        provider_type = self.provider_type or self.default_provider
        if not provider_type:
            raise StrategyError("No provider specified and no default provider set")

        try:
            # Create and use provider
            provider = self._create_provider(
                provider_type=provider_type,
                model=self.model,
            )
            
            # Get model from environment for OpenAI
            model = self.model
            if provider_type == ProviderType.OPENAI:
                model = os.getenv("OPENAI_MODEL", model)
            
            # Create request object
            kwargs = {k: v for k, v in self.kwargs.items() if k != 'strategy'}
            request = LLMRequest(
                prompt=prompt,
                provider_type=provider_type,
                model=model,
                strategy=self.strategy_type,
                **kwargs
            )
            
            response = await provider.generate(request)
            
            # Add strategy info to metadata
            if response.metadata:
                response.metadata.strategy = self.strategy_type
                
            return response
            
        except ProviderNotAvailableError as e:
            raise StrategyError(f"Provider {provider_type} not available") from e
        except Exception as e:
            raise StrategyError(f"Strategy execution failed: {str(e)}") from e 