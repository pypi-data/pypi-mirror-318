"""Main client for send_2_llm module."""

import os
import logging
from typing import Optional, Any, Dict, List

# Настройка логирования
logger = logging.getLogger(__name__)
if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

from .types import (
    LLMResponse,
    ProviderType,
    StrategyType,
    StrategyError,
    OutputFormat,
)
from .strategies.base import BaseStrategy
from .strategies.single import SingleProviderStrategy
from .strategies.fallback import FallbackStrategy
from .config import load_config, ConfigurationError
from .response_formatter import ResponseFormatter
from .providers import get_provider


class LLMClient:
    """Main client for interacting with LLM providers."""
    
    def __init__(
        self,
        strategy_type: Optional[StrategyType] = None,
        provider_type: Optional[ProviderType] = None,
        providers: Optional[List[ProviderType]] = None,
        model: Optional[str] = None,
        models: Optional[List[str]] = None,
        output_format: Optional[OutputFormat] = None,
        **kwargs: Any
    ):
        """Initialize LLM client."""
        try:
            # Load configuration
            self.config = load_config()
            
            # Get strategy type
            self.strategy_type = strategy_type or self.config["strategy"]
            
            # Get provider settings
            if self.strategy_type == StrategyType.SINGLE:
                self.provider_type = provider_type or self.config["default_provider"]
                self.provider_class = get_provider(self.provider_type)
                if not self.provider_type:
                    raise StrategyError("No provider specified for single provider strategy")
                self.providers = [self.provider_type]
                self.models = [model] if model else None
            else:  # FALLBACK strategy
                self.providers = providers or self.config["providers"]
                if not self.providers:
                    raise StrategyError("No providers specified for strategy")
                self.models = models or self.config["models"]
                
            # Set output format
            self.output_format = output_format
            
            # Create strategy
            self._strategy = self._create_strategy()
            
        except Exception as e:
            raise StrategyError(f"Strategy initialization failed: {str(e)}")
    
    def _create_strategy(self) -> BaseStrategy:
        """Create strategy instance based on configuration."""
        if self.strategy_type == StrategyType.SINGLE:
            return SingleProviderStrategy(
                provider_type=self.provider_type,
                model=self.models[0] if self.models else None
            )
        elif self.strategy_type == StrategyType.FALLBACK:
            return FallbackStrategy(
                providers=self.providers,
                models=self.models
            )
        else:
            raise StrategyError(f"Unknown strategy type: {self.strategy_type}")
    
    async def generate(
        self,
        prompt: str,
        provider_type: Optional[ProviderType] = None,
        providers: Optional[List[ProviderType]] = None,
        model: Optional[str] = None,
        models: Optional[List[str]] = None,
        output_format: Optional[OutputFormat] = None,
        **kwargs: Any
    ) -> LLMResponse:
        """Generate response using current strategy."""
        # Create new strategy if parameters override defaults
        if any([provider_type, providers, model, models, kwargs]):
            strategy_kwargs = self.kwargs.copy()
            strategy_kwargs.update(kwargs)
            
            if self.strategy_type == StrategyType.SINGLE:
                strategy = SingleProviderStrategy(
                    provider_type=provider_type or self.provider_type,
                    model=model or self.model,
                    **strategy_kwargs
                )
            elif self.strategy_type == StrategyType.FALLBACK:
                strategy = FallbackStrategy(
                    providers=providers or self.providers,
                    models=models or self.models,
                    **strategy_kwargs
                )
            else:
                raise StrategyError(f"Strategy type {self.strategy_type} not implemented")
        else:
            strategy = self._strategy
            
        # Get raw response from strategy
        response = await strategy.execute(prompt)
        
        # Format response if needed
        format_to_use = output_format or self.output_format
        if format_to_use and format_to_use != OutputFormat.RAW:
            response = ResponseFormatter.format_response(response, format_to_use)
            
        return response
    
    async def __aenter__(self) -> "LLMClient":
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        pass 