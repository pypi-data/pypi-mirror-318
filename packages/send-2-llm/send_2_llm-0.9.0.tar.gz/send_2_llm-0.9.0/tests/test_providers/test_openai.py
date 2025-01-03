"""
!!! WARNING - STABLE TESTS !!!
These are stable tests for OpenAI provider implementation.
DO NOT MODIFY without explicit permission.
Commit: b25d24a
Tag: stable_openai_v1
Test Coverage: 96%

Test suite includes:
- Provider initialization
- Text generation
- Error handling
- Custom model support
- Live API testing (haiku generation)

To run these tests:
PYTHONPATH=src pytest tests/test_providers/test_openai.py -v

Required dependencies:
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- openai>=1.12.0
!!! WARNING !!!
"""

import os
import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from openai.types.chat import ChatCompletion
from send_2_llm.types import ProviderType, LLMRequest, LLMResponse
from send_2_llm.providers.openai import OpenAIProvider
from datetime import datetime


# !!! STABLE TESTS - DO NOT MODIFY !!!
# Базовые тесты OpenAI провайдера
# ==============================

@pytest.mark.asyncio
async def test_openai_provider_initialization():
    """Test OpenAI provider initialization."""
    with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
        provider = OpenAIProvider()
        assert provider.provider_type == ProviderType.OPENAI
        assert provider.default_model == "gpt-3.5-turbo"
        

@pytest.mark.asyncio
async def test_openai_generate(mock_env):
    """Test OpenAI text generation."""
    provider = OpenAIProvider()
    request = LLMRequest(
        prompt="Test prompt",
        model="gpt-3.5-turbo",
        max_tokens=100
    )
    
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
    mock_response.model = "gpt-3.5-turbo"
    mock_response.model_dump.return_value = {
        "id": "test-id",
        "model": "gpt-3.5-turbo",
        "choices": [{"message": {"content": "Test response"}}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
    }
    
    with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = mock_response
        response = await provider.generate(request)
        
        assert isinstance(response, LLMResponse)
        assert response.text == "Test response"
        assert response.metadata.provider == ProviderType.OPENAI
        assert response.metadata.model == "gpt-3.5-turbo"
        assert response.metadata.usage.prompt_tokens == 10
        assert response.metadata.usage.completion_tokens == 20
        assert response.metadata.usage.total_tokens == 30
        # Check cost calculation for gpt-3.5-turbo
        expected_cost = (0.0015 * 10/1000) + (0.002 * 20/1000)  # $0.0015 per 1K input, $0.002 per 1K output
        assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_openai_gpt4_cost():
    """Test OpenAI GPT-4 cost calculation."""
    provider = OpenAIProvider()
    request = LLMRequest(
        prompt="Test prompt",
        model="gpt-4",
        max_tokens=100
    )
    
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
    mock_response.model = "gpt-4"
    mock_response.model_dump.return_value = {
        "id": "test-id",
        "model": "gpt-4",
        "choices": [{"message": {"content": "Test response"}}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
    }
    
    with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = mock_response
        response = await provider.generate(request)
        
        assert isinstance(response, LLMResponse)
        assert response.metadata.model == "gpt-4"
        assert response.metadata.usage.prompt_tokens == 10
        assert response.metadata.usage.completion_tokens == 20
        assert response.metadata.usage.total_tokens == 30
        # Check cost calculation for gpt-4
        expected_cost = (0.03 * 10/1000) + (0.06 * 20/1000)  # $0.03 per 1K input, $0.06 per 1K output
        assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_openai_error_handling():
    """Test OpenAI error handling."""
    with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
        provider = OpenAIProvider()
        request = LLMRequest(prompt="Test prompt")
        
        with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
            mock_create.side_effect = Exception("API Error")
            with pytest.raises(Exception):
                await provider.generate(request)


@pytest.mark.asyncio
async def test_openai_custom_model():
    """Test OpenAI with custom model."""
    with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
        provider = OpenAIProvider()
        request = LLMRequest(
            prompt="Test prompt",
            model="gpt-4-turbo"
        )
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_response.model = "gpt-4-turbo"
        mock_response.model_dump.return_value = {
            "id": "test-id",
            "model": "gpt-4-turbo",
            "choices": [{"message": {"content": "Test response"}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
        }
        
        with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
            mock_create.return_value = mock_response
            response = await provider.generate(request)
            
            assert isinstance(response, LLMResponse)
            assert response.metadata.model == "gpt-4-turbo"
            assert response.metadata.usage.prompt_tokens == 10
            assert response.metadata.usage.completion_tokens == 20
            assert response.metadata.usage.total_tokens == 30
            # Check cost calculation for gpt-4
            expected_cost = (0.03 * 10/1000) + (0.06 * 20/1000)  # $0.03 per 1K input, $0.06 per 1K output
            assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


# Креативные тесты с живым API
# ===========================

@pytest.mark.asyncio
@pytest.mark.live
async def test_openai_generate_russian_haiku_live():
    """Live test of OpenAI haiku generation in Russian."""
    print("\n" + "="*50)
    print("ГЕНЕРАЦИЯ НОВОГО ХАЙКУ")
    print("="*50)
    
    provider = OpenAIProvider()
    
    request = LLMRequest(
        prompt="""Сгенерируй хайку о весне на русском языке. 
        Следуй традиционной схеме 5-7-5 слогов.
        Хайку должно быть поэтичным и образным.
        Используй метафоры и природные образы.
        
        Пример формата:
        [первая строка - 5 слогов]
        [вторая строка - 7 слогов]
        [третья строка - 5 слогов]""",
        model="gpt-3.5-turbo",
        max_tokens=50,
        temperature=0.8  # Больше креативности для разнообразия
    )
    
    response = await provider.generate(request)
    
    print("\n=== Новое хайку от OpenAI ===")
    print(response.text)
    print("="*30)
    print(f"Использовано токенов: {response.metadata.usage.total_tokens}")
    print("="*30 + "\n")
    
    # Проверяем базовую структуру
    assert isinstance(response, LLMResponse)
    
    # Проверяем формат хайку
    haiku_lines = response.text.strip().split('\n')
    assert len(haiku_lines) == 3, "Хайку должно состоять ровно из трёх строк"
    
    # Проверяем, что текст на русском (содержит кириллицу)
    assert any(ord('а') <= ord(c) <= ord('я') for c in response.text.lower()), "Текст должен содержать русские буквы"
    
    # Проверяем метаданные
    assert response.metadata.provider == ProviderType.OPENAI
    assert response.metadata.model == "gpt-3.5-turbo"
    assert response.metadata.usage.total_tokens > 0
    
    # Сохраняем сгенерированное хайку в файл для истории
    with open("tests/generated_haiku_history.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write(response.text)
        f.write("\n") 