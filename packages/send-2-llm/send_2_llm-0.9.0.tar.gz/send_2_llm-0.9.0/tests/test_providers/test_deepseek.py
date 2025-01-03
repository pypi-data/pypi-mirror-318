"""Tests for DeepSeek provider.

This test suite verifies the functionality of the DeepSeek provider implementation.
The provider uses OpenAI-compatible API to interact with DeepSeek's models.

Key aspects tested:
1. Provider initialization
2. Environment configuration
3. Error handling for missing API keys
4. Live generation testing with Russian language support
"""

import os
import pytest
from unittest.mock import patch
from openai.types.chat import ChatCompletion

from send_2_llm.types import (
    ProviderType,
    LLMRequest,
    LLMResponse,
    ProviderAPIError
)
from send_2_llm.providers.deepseek import DeepSeekProvider


@pytest.fixture
def mock_env(monkeypatch):
    """Mock environment variables.
    
    This fixture ensures that tests have access to required environment variables
    without needing actual API keys.
    """
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")


@pytest.fixture
def provider(mock_env):
    """Create DeepSeek provider instance.
    
    Returns a configured provider instance with mocked credentials.
    """
    return DeepSeekProvider()


@pytest.mark.asyncio
async def test_deepseek_init():
    """Test provider initialization.
    
    Verifies that:
    1. Provider type is set correctly
    2. Default model is configured
    3. API key is properly loaded from environment
    """
    with patch.dict('os.environ', {'DEEPSEEK_API_KEY': 'test-key'}):
        provider = DeepSeekProvider()
        assert provider.provider_type == ProviderType.DEEPSEEK
        assert provider.default_model == "deepseek-chat"
        assert provider.api_key == "test-key"


@pytest.mark.asyncio
async def test_init_no_api_key():
    """Test initialization without API key.
    
    Verifies that:
    1. Provider raises appropriate error when API key is missing
    2. Error message is descriptive
    """
    with patch.dict(os.environ, clear=True):
        with pytest.raises(ProviderAPIError) as exc:
            DeepSeekProvider()
        assert "DEEPSEEK_API_KEY environment variable not set" in str(exc.value)


@pytest.mark.asyncio
@pytest.mark.live
async def test_deepseek_generate_russian_haiku_live():
    """Live test of DeepSeek haiku generation in Russian.
    
    This test requires:
    1. Valid DEEPSEEK_API_KEY in environment
    2. Active internet connection
    3. DeepSeek API availability
    
    Verifies:
    1. Basic response structure and generation
    2. Russian language capability
    3. Token usage tracking
    4. Latency measurement
    5. Metadata handling
    6. Model configuration
    """
    print("\n" + "="*50)
    print("ГЕНЕРАЦИЯ НОВОГО ХАЙКУ ЧЕРЕЗ DEEPSEEK")
    print("="*50)
    
    provider = DeepSeekProvider()
    
    request = LLMRequest(
        prompt="""Сгенерируй хайку о программировании на русском языке. 
        Следуй традиционной схеме 5-7-5 слогов.
        Хайку должно быть поэтичным и образным.
        Используй метафоры и технические термины.""",
        max_tokens=50,
        temperature=0.8
    )
    
    response = await provider.generate(request)
    
    print("\n=== Новое хайку от DeepSeek ===")
    print(response.text)
    print("="*30)
    print(f"Модель: {response.metadata.model}")
    print(f"Использовано токенов: {response.metadata.usage.total_tokens}")
    print(f"Время: {response.metadata.latency:.2f} сек.")
    print("="*30 + "\n")
    
    # Проверяем базовую структуру
    assert isinstance(response, LLMResponse)
    assert response.text, "Response should not be empty"
    assert len(response.text.split()) >= 3, "Response should be at least 3 words"
    
    # Проверяем, что текст на русском (содержит кириллицу)
    assert any(ord('а') <= ord(c) <= ord('я') for c in response.text.lower()), "Текст должен содержать русские буквы"
    
    # Проверяем метаданные
    assert response.metadata.provider == ProviderType.DEEPSEEK
    assert response.metadata.model == "deepseek-chat"
    assert response.metadata.usage.total_tokens > 0
    assert response.metadata.latency > 0
    assert response.metadata.raw_response is not None 