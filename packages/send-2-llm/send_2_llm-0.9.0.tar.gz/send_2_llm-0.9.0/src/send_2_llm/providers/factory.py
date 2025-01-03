"""Provider factory module."""

import os
import logging
from typing import Dict, Type, Optional, Any, List
from dotenv import load_dotenv

# Загрузка .env файла
load_dotenv()

# Настройка логирования
logger = logging.getLogger(__name__)
if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

from ..types import (
    ProviderType,
    ProviderNotAvailableError,
)
from ..config import load_config
from .base import BaseLLMProvider
from .together import TogetherProvider
from .openai_v2 import OpenAIProviderV2
from .anthropic import AnthropicProvider
from .deepseek import DeepSeekProvider
from .gemini import GeminiProvider
from .perplexity import PerplexityProvider

# Default provider from environment
config = load_config()
DEFAULT_PROVIDER = config.get("default_provider")
if DEFAULT_PROVIDER is None:
    logger.warning("No default provider configured in environment")
    raise ProviderNotAvailableError("No default provider configured. Please set DEFAULT_PROVIDER in .env")

# Registry of available providers
_PROVIDER_REGISTRY: Dict[ProviderType, Type[BaseLLMProvider]] = {
    ProviderType.TOGETHER: TogetherProvider,
    ProviderType.OPENAI: OpenAIProviderV2,
    ProviderType.ANTHROPIC: AnthropicProvider,
    ProviderType.DEEPSEEK: DeepSeekProvider,
    ProviderType.GEMINI: GeminiProvider,
    ProviderType.PERPLEXITY: PerplexityProvider,
}

def create_provider(
    provider_type: Optional[ProviderType] = None,
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    max_tokens: Optional[int] = None,
    **kwargs: Any
) -> BaseLLMProvider:
    """Create provider instance."""
    # Use default provider if none specified
    if provider_type is None:
        provider_type = DEFAULT_PROVIDER
        logger.debug(f"No provider specified, using default: {provider_type}")

    logger.debug(f"Attempting to create provider: {provider_type}")
    logger.debug(f"Model: {model}, Temperature: {temperature}, Max tokens: {max_tokens}")
    
    # Get provider class
    provider_cls = _PROVIDER_REGISTRY.get(provider_type)
    if not provider_cls:
        logger.error(f"Provider {provider_type} not found in registry")
        logger.debug(f"Available providers: {list(_PROVIDER_REGISTRY.keys())}")
        raise ProviderNotAvailableError(
            f"Provider {provider_type} not found. Available providers: {list(_PROVIDER_REGISTRY.keys())}"
        )
    
    try:
        # Special case for providers which don't accept constructor parameters
        if provider_type in [ProviderType.OPENAI, ProviderType.TOGETHER, ProviderType.ANTHROPIC, ProviderType.DEEPSEEK, ProviderType.GEMINI, ProviderType.PERPLEXITY]:
            logger.debug(f"Creating {provider_type} provider without constructor parameters")
            return provider_cls()
            
        # Create provider instance with parameters for other providers
        logger.debug(f"Creating {provider_type} provider with parameters")
        return provider_cls(
            model=model,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            **kwargs
        )
    except Exception as e:
        logger.error(f"Error creating provider {provider_type}: {str(e)}")
        raise ProviderNotAvailableError(f"Failed to create provider {provider_type}: {str(e)}")

def register_provider(provider_type: ProviderType, provider_cls: Type[BaseLLMProvider]) -> None:
    """Register new provider.

    Args:
        provider_type: Type of provider
        provider_cls: Provider class
    """
    _PROVIDER_REGISTRY[provider_type] = provider_cls

def get_available_providers() -> List[ProviderType]:
    """Get list of available providers.

    Returns:
        List of available provider types
    """
    return list(_PROVIDER_REGISTRY.keys()) 