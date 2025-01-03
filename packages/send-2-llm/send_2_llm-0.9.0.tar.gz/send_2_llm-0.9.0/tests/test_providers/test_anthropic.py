"""
STABLE COMPONENT - DO NOT MODIFY WITHOUT PERMISSION

This file contains stable tests for the Anthropic provider integration.
Tag: stable_anthropic_v1

Protected Tests:
- test_anthropic_init: Basic provider initialization
- test_anthropic_wrong_model: Error handling for invalid models
- test_anthropic_generate_russian_haiku_live: Live API testing

Coverage: 95%+

To run tests:
PYTHONPATH=src pytest tests/test_providers/test_anthropic.py -v

Recovery:
git checkout stable_anthropic_v1
"""

import os
import pytest
from datetime import datetime
from unittest.mock import patch, AsyncMock, MagicMock
from send_2_llm.types import LLMRequest, LLMResponse, ProviderType, ProviderAPIError, StrategyType, StrategyError
from send_2_llm.providers.anthropic import AnthropicProvider
from send_2_llm.config import load_config, reload_config
from send_2_llm.client import LLMClient

# !!! STABLE TESTS - DO NOT MODIFY !!!
# Базовые тесты Anthropic провайдера
# ==============================

@pytest.mark.asyncio
async def test_anthropic_init():
    """Test provider initialization."""
    reload_config()
    provider = AnthropicProvider()
    assert provider.provider_type == ProviderType.ANTHROPIC


@pytest.mark.asyncio
async def test_anthropic_generate():
    """Test Anthropic text generation with token usage and cost calculation."""
    reload_config()
    provider = AnthropicProvider()
    request = LLMRequest(
        prompt="Test prompt",
        model="claude-3-haiku-20240307",
        max_tokens=100
    )
    
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Test response")]
    mock_response.model = "claude-3-haiku-20240307"
    mock_response.model_dump.return_value = {
        "id": "test-id",
        "model": "claude-3-haiku-20240307",
        "content": [{"text": "Test response"}],
        "usage": {"input_tokens": 10, "output_tokens": 20}
    }
    
    with patch.object(provider.client.messages, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = mock_response
        response = await provider.generate(request)
        
        assert response.text == "Test response"
        assert response.metadata.provider == ProviderType.ANTHROPIC
        assert response.metadata.model == "claude-3-haiku-20240307"
        assert response.metadata.usage.prompt_tokens == 10
        assert response.metadata.usage.completion_tokens == 20
        assert response.metadata.usage.total_tokens == 30
        # Check cost calculation for claude-3-haiku
        expected_cost = (0.00025 * 10/1000) + (0.00125 * 20/1000)  # $0.00025 per 1K input, $0.00125 per 1K output
        assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_anthropic_sonnet_cost():
    """Test Anthropic Sonnet cost calculation."""
    reload_config()
    provider = AnthropicProvider()
    request = LLMRequest(
        prompt="Test prompt",
        model="claude-3-sonnet-20240229",
        max_tokens=100
    )
    
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Test response")]
    mock_response.model = "claude-3-sonnet-20240229"
    mock_response.model_dump.return_value = {
        "id": "test-id",
        "model": "claude-3-sonnet-20240229",
        "content": [{"text": "Test response"}],
        "usage": {"input_tokens": 10, "output_tokens": 20}
    }
    
    with patch.object(provider.client.messages, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = mock_response
        response = await provider.generate(request)
        
        assert response.text == "Test response"
        assert response.metadata.provider == ProviderType.ANTHROPIC
        assert response.metadata.model == "claude-3-sonnet-20240229"
        assert response.metadata.usage.prompt_tokens == 10
        assert response.metadata.usage.completion_tokens == 20
        assert response.metadata.usage.total_tokens == 30
        # Check cost calculation for claude-3-sonnet
        expected_cost = (0.003 * 10/1000) + (0.015 * 20/1000)  # $0.003 per 1K input, $0.015 per 1K output
        assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_anthropic_opus_cost():
    """Test Anthropic Opus cost calculation."""
    reload_config()
    provider = AnthropicProvider()
    request = LLMRequest(
        prompt="Test prompt",
        model="claude-3-opus-20240229",
        max_tokens=100
    )
    
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Test response")]
    mock_response.model = "claude-3-opus-20240229"
    mock_response.model_dump.return_value = {
        "id": "test-id",
        "model": "claude-3-opus-20240229",
        "content": [{"text": "Test response"}],
        "usage": {"input_tokens": 10, "output_tokens": 20}
    }
    
    with patch.object(provider.client.messages, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = mock_response
        response = await provider.generate(request)
        
        assert response.text == "Test response"
        assert response.metadata.provider == ProviderType.ANTHROPIC
        assert response.metadata.model == "claude-3-opus-20240229"
        assert response.metadata.usage.prompt_tokens == 10
        assert response.metadata.usage.completion_tokens == 20
        assert response.metadata.usage.total_tokens == 30
        # Check cost calculation for claude-3-opus
        expected_cost = (0.015 * 10/1000) + (0.075 * 20/1000)  # $0.015 per 1K input, $0.075 per 1K output
        assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_anthropic_wrong_model():
    """Test error on wrong model with SingleProviderStrategy."""
    reload_config()
    
    client = LLMClient(
        strategy_type=StrategyType.SINGLE,
        provider_type=ProviderType.ANTHROPIC,
        model="wrong-model"
    )
    
    with pytest.raises(StrategyError) as exc:
        await client.generate("тест")
    assert "not_found_error" in str(exc.value)
    assert "wrong-model" in str(exc.value)


@pytest.mark.asyncio
async def test_anthropic_fallback():
    """Test fallback to next provider when model is wrong."""
    reload_config()
    
    client = LLMClient(
        strategy_type=StrategyType.FALLBACK,
        providers=[ProviderType.ANTHROPIC, ProviderType.OPENAI],
        models=["wrong-model", None]  # wrong Anthropic model, default OpenAI model
    )
    
    response = await client.generate("тест")
    assert response.text  # Should get response from OpenAI
    assert response.metadata.provider == ProviderType.OPENAI  # Verify it came from OpenAI


# Креативные тесты с живым API
# ===========================

@pytest.mark.asyncio
@pytest.mark.live
async def test_anthropic_generate_russian_haiku_live():
    """Live test of Anthropic haiku generation in Russian."""
    print("\n" + "="*50)
    print("ГЕНЕРАЦИЯ НОВОГО ХАЙКУ ЧЕРЕЗ ANTHROPIC")
    print("="*50)
    
    provider = AnthropicProvider()
    
    request = LLMRequest(
        prompt="Хайку о весне на русском",  # Короткий и четкий промпт
        max_tokens=50,
        temperature=0.8  # Больше креативности для разнообразия
    )
    
    response = await provider.generate(request)
    
    print("\n=== Новое хайку от Anthropic ===")
    print(response.text)
    print("="*30)
    print(f"Использовано токенов: {response.metadata.usage.total_tokens}")
    print(f"Стоимость: ${response.metadata.usage.cost:.6f}")
    print("="*30 + "\n")
    
    # Проверяем базовую структуру
    assert isinstance(response, LLMResponse)
    assert response.metadata.usage.total_tokens > 0
    assert response.metadata.usage.cost > 0
    
    # Проверяем, что текст на русском (содержит кириллицу)
    assert any(ord('а') <= ord(c) <= ord('я') for c in response.text.lower()), "Текст должен содержать русские буквы"
    
    # Проверяем метаданные
    assert response.metadata.provider == ProviderType.ANTHROPIC
    
    # Сохраняем сгенерированное хайку в файл для истории
    with open("tests/generated_haiku_history.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (Anthropic) ===\n")
        f.write(response.text)
        f.write("\n") 