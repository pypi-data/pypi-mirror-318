"""Provider package."""

from .base import BaseLLMProvider
from .factory import ProviderFactory
from .manager import LLMManager

# Import all providers for registration
from .openai_provider import OpenAIProviderV2
from .anthropic_provider import AnthropicProvider
from .together_provider import TogetherProvider
from .perplexity_provider import PerplexityProvider
from .deepseek_provider import DeepSeekProvider
from .gemini_provider import GeminiProvider

__all__ = [
    "BaseLLMProvider",
    "ProviderFactory",
    "LLMManager",
    "OpenAIProviderV2",
    "AnthropicProvider",
    "TogetherProvider",
    "PerplexityProvider",
    "DeepSeekProvider",
    "GeminiProvider",
]

def get_provider(provider_type: str):
    """Get provider class by type."""
    factory = ProviderFactory()
    try:
        from ..types import ProviderType
        provider_enum = ProviderType(provider_type.lower())
        provider_info = factory.get_provider_info(provider_enum)
        if provider_info:
            return provider_info.provider_class
    except (ValueError, KeyError) as e:
        available = ", ".join(p.value for p in factory.list_providers())
        raise ValueError(f"Unknown provider type: {provider_type}. Available: {available}") from e 