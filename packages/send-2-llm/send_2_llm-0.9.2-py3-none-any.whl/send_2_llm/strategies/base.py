"""Base strategy interface."""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

from ..types import LLMResponse, ProviderType, StrategyType
from ..providers.base import BaseLLMProvider
from ..providers import get_provider


class BaseStrategy(ABC):
    """Base class for LLM strategies."""
    
    def __init__(
        self,
        providers: Optional[List[ProviderType]] = None,
        default_provider: Optional[ProviderType] = None,
        **kwargs: Any
    ):
        """Initialize strategy.
        
        Args:
            providers: List of providers to use
            default_provider: Default provider if none specified
            **kwargs: Additional strategy-specific parameters
        """
        self.providers = providers or []
        self.default_provider = default_provider
        self.kwargs = kwargs
        
    @abstractmethod
    async def execute(self, prompt: str) -> LLMResponse:
        """Execute strategy to get response.
        
        Args:
            prompt: Input prompt
            
        Returns:
            LLMResponse with generated text and metadata
            
        Raises:
            StrategyError: On strategy execution error
        """
        raise NotImplementedError
    
    def _create_provider(
        self,
        provider_type: ProviderType,
        model: Optional[str] = None,
        **kwargs: Any
    ) -> BaseLLMProvider:
        """Create provider instance.
        
        Args:
            provider_type: Type of provider to create
            model: Model name to use
            **kwargs: Additional provider parameters
            
        Returns:
            Provider instance
        """
        provider_class = get_provider(provider_type)
        return provider_class(model=model, **kwargs) 