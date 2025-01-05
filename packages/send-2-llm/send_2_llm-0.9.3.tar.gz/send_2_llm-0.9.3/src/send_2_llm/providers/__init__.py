"""Provider package."""

from .base import BaseLLMProvider
from .factory import ProviderFactory
from .manager import LLMManager

# Import only OpenAI provider by default
from .openai_provider import OpenAIProviderV2

__all__ = [
    "BaseLLMProvider",
    "ProviderFactory",
    "LLMManager",
    "OpenAIProviderV2",
]

def get_provider(provider_type: str):
    """Get provider instance by type."""
    if provider_type == "openai":
        from .openai_provider import OpenAIProviderV2
        return OpenAIProviderV2()
    elif provider_type == "anthropic":
        from .anthropic_provider import AnthropicProvider
        return AnthropicProvider()
    elif provider_type == "together":
        from .together_provider import TogetherProvider
        return TogetherProvider()
    elif provider_type == "perplexity":
        from .perplexity_provider import PerplexityProvider
        return PerplexityProvider()
    elif provider_type == "deepseek":
        from .deepseek_provider import DeepSeekProvider
        return DeepSeekProvider()
    elif provider_type == "gemini":
        from .gemini_provider import GeminiProvider
        return GeminiProvider()
    else:
        raise ValueError(f"Unknown provider type: {provider_type}") 