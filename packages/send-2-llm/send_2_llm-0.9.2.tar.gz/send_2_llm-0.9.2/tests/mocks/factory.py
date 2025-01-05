"""Mock provider factory for testing."""

from typing import Dict, Type, Optional, Any

from send_2_llm.types import ProviderType, ProviderNotAvailableError
from send_2_llm.providers.base import BaseLLMProvider
from .providers import MockTogetherProvider, MockOpenAIProvider

# Registry of mock providers
_MOCK_PROVIDER_REGISTRY: Dict[ProviderType, Type[BaseLLMProvider]] = {
    ProviderType.TOGETHER: MockTogetherProvider,
    ProviderType.OPENAI: MockOpenAIProvider,
}

def create_mock_provider(
    provider_type: ProviderType,
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    max_tokens: Optional[int] = None,
    **kwargs: Any
) -> BaseLLMProvider:
    """Create mock provider instance.

    Args:
        provider_type: Type of provider to create
        model: Model name to use
        temperature: Sampling temperature
        top_p: Nucleus sampling parameter
        max_tokens: Maximum tokens in response
        **kwargs: Additional provider-specific parameters

    Returns:
        Provider instance

    Raises:
        ProviderNotAvailableError: If provider not found
    """
    # Get provider class
    provider_cls = _MOCK_PROVIDER_REGISTRY.get(provider_type)
    if not provider_cls:
        raise ProviderNotAvailableError(
            f"Provider {provider_type} not found. Available providers: {list(_MOCK_PROVIDER_REGISTRY.keys())}"
        )
    
    # Create provider instance
    return provider_cls(
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        **kwargs
    ) 