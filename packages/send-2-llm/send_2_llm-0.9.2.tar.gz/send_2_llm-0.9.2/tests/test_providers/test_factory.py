"""Tests for the provider factory."""

import pytest
from typing import Type

from send_2_llm.types import ProviderType, ProviderAPIError
from send_2_llm.providers.factory import ProviderFactory, ProviderInfo
from send_2_llm.providers.base import BaseLLMProvider
from send_2_llm.providers.openai_v2 import OpenAIProviderV2

# Test provider for registration
class TestProvider(BaseLLMProvider):
    """Test provider implementation."""
    
    def __init__(self, **kwargs):
        super().__init__(provider_type=ProviderType.OPENAI)
        
    async def _generate(self, request):
        return None

def test_provider_factory_init():
    """Test provider factory initialization."""
    factory = ProviderFactory()
    
    # Check default providers are registered
    assert len(factory._providers) > 0
    assert ProviderType.OPENAI in factory._providers
    assert ProviderType.ANTHROPIC in factory._providers
    
    # Check provider info structure
    openai_info = factory._providers[ProviderType.OPENAI]
    assert isinstance(openai_info, ProviderInfo)
    assert openai_info.provider_class == OpenAIProviderV2
    assert openai_info.priority == 100
    assert not openai_info.is_fallback
    assert "OpenAI API provider" in openai_info.description

def test_register_provider():
    """Test provider registration."""
    factory = ProviderFactory()
    
    # Register new provider
    factory.register_provider(
        ProviderType.OPENAI,
        TestProvider,
        priority=50,
        is_fallback=True,
        description="Test provider",
        override=True
    )
    
    # Check registration
    provider_info = factory.get_provider_info(ProviderType.OPENAI)
    assert provider_info is not None
    assert provider_info.provider_class == TestProvider
    assert provider_info.priority == 50
    assert provider_info.is_fallback
    assert provider_info.description == "Test provider"

def test_register_provider_no_override():
    """Test provider registration without override."""
    factory = ProviderFactory()
    
    # Try to register without override
    with pytest.raises(ValueError) as exc:
        factory.register_provider(ProviderType.OPENAI, TestProvider)
    assert "already registered" in str(exc.value)

def test_register_invalid_provider():
    """Test registration of invalid provider."""
    factory = ProviderFactory()
    
    # Try to register invalid provider class
    class InvalidProvider:
        pass
    
    with pytest.raises(ValueError) as exc:
        factory.register_provider(ProviderType.OPENAI, InvalidProvider)
    assert "must inherit from BaseLLMProvider" in str(exc.value)

def test_list_providers():
    """Test listing providers."""
    factory = ProviderFactory()
    
    # Get sorted providers
    providers = factory.list_providers()
    
    # Check sorting by priority
    priorities = [info.priority for _, info in providers]
    assert priorities == sorted(priorities, reverse=True)
    
    # Check provider types
    provider_types = [pt.value for pt, _ in providers]
    assert "openai" in provider_types
    assert "anthropic" in provider_types

def test_get_fallback_providers():
    """Test getting fallback providers."""
    factory = ProviderFactory()
    
    # Register fallback provider
    factory.register_provider(
        ProviderType.OPENAI,
        TestProvider,
        priority=50,
        is_fallback=True,
        description="Fallback provider",
        override=True
    )
    
    # Get fallback providers
    fallbacks = factory.get_fallback_providers()
    
    # Check fallback providers
    assert len(fallbacks) > 0
    provider_type, info = fallbacks[0]
    assert provider_type == ProviderType.OPENAI
    assert info.is_fallback
    assert info.description == "Fallback provider"

def test_create_provider():
    """Test provider creation."""
    factory = ProviderFactory()
    
    # Create provider
    provider = factory.create_provider(ProviderType.OPENAI)
    assert isinstance(provider, OpenAIProviderV2)
    assert provider.provider_type == ProviderType.OPENAI

def test_create_invalid_provider():
    """Test creation of invalid provider."""
    factory = ProviderFactory()
    
    # Try to create non-existent provider
    with pytest.raises(ProviderAPIError) as exc:
        factory.create_provider(ProviderType("invalid"))
    assert "not registered" in str(exc.value)
    assert "Available providers" in str(exc.value)

def test_create_provider_type_mismatch():
    """Test provider creation with type mismatch."""
    factory = ProviderFactory()
    
    # Create provider class with wrong type
    class WrongTypeProvider(BaseLLMProvider):
        def __init__(self, **kwargs):
            super().__init__(provider_type=ProviderType.ANTHROPIC)
        
        async def _generate(self, request):
            return None
    
    # Register provider with wrong type
    factory.register_provider(
        ProviderType.OPENAI,
        WrongTypeProvider,
        override=True
    )
    
    # Try to create provider
    with pytest.raises(ProviderAPIError) as exc:
        factory.create_provider(ProviderType.OPENAI)
    assert "Provider type mismatch" in str(exc.value)
    assert "Expected openai" in str(exc.value)
    assert "got anthropic" in str(exc.value) 