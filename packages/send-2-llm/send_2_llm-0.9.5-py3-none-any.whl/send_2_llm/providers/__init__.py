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
    from ..types import ProviderType
    
    # Convert string to ProviderType
    try:
        provider_enum = ProviderType(provider_type)
    except ValueError:
        raise ValueError(f"Unknown provider type: {provider_type}")
    
    # Create factory and get provider
    factory = ProviderFactory()
    return factory.create_provider(provider_enum) 