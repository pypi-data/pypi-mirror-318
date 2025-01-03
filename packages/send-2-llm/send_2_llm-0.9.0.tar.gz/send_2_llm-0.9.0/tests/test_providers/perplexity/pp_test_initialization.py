"""
Тест инициализации Perplexity провайдера.
"""

import os
import pytest
from send_2_llm.providers.perplexity import PerplexityProvider
from send_2_llm.types import ProviderType, ProviderAPIError


def test_provider_initialization(monkeypatch):
    """
    Проверяем базовую инициализацию провайдера
    """
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    provider = PerplexityProvider()
    
    # Проверяем только критичные параметры
    assert provider.provider_type == ProviderType.PERPLEXITY
    assert provider.api_key == "test_key"
    assert "Bearer test_key" in provider.headers["Authorization"]


def test_provider_initialization_no_api_key(monkeypatch):
    """
    Проверяем что без API ключа провайдер не создается
    """
    monkeypatch.delenv("PERPLEXITY_API_KEY", raising=False)
    
    with pytest.raises(ProviderAPIError) as exc_info:
        PerplexityProvider()
    
    assert "PERPLEXITY_API_KEY environment variable not set" in str(exc_info.value) 