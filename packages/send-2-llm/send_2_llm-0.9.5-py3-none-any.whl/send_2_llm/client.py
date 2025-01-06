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
            
            # Store initialization parameters
            self.strategy_type = strategy_type or StrategyType.SINGLE
            self.provider_type = provider_type
            self.providers = providers
            self.model = model
            self.models = models
            self.output_format = output_format
            self.kwargs = kwargs
            
            # Initialize strategy
            self._init_strategy()
            
        except Exception as e:
            logger.error(f"Failed to initialize client: {str(e)}")
            raise
            
    def _init_strategy(self):
        """Initialize strategy based on configuration."""
        if self.strategy_type == StrategyType.SINGLE:
            if not self.provider_type:
                raise ConfigurationError("Provider type is required for single provider strategy")
                
            self._strategy = SingleProviderStrategy(
                provider_type=self.provider_type,
                model=self.model,
                **self.kwargs
            )
        elif self.strategy_type == StrategyType.FALLBACK:
            if not self.providers:
                raise ConfigurationError("Providers list is required for fallback strategy")
                
            self._strategy = FallbackStrategy(
                providers=self.providers,
                models=self.models,
                **self.kwargs
            )
        else:
            raise StrategyError(f"Strategy type {self.strategy_type} not implemented")
    
    async def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> LLMResponse:
        """Generate response using current strategy."""
        try:
            # Update kwargs with any new parameters
            request_kwargs = self.kwargs.copy()
            request_kwargs.update(kwargs)
            if max_tokens is not None:
                request_kwargs['max_tokens'] = max_tokens
            
            # Get response from strategy
            response = await self._strategy.execute(prompt, **request_kwargs)
            
            # Format response if needed
            if self.output_format and self.output_format != OutputFormat.RAW:
                response = ResponseFormatter.format_response(response, self.output_format)
                
            return response
            
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            raise 