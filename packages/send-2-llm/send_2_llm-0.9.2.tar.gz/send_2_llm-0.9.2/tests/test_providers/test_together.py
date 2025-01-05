"""
!!! WARNING - STABLE TOGETHER AI TESTS !!!
These are stable tests for Together AI provider implementation.
DO NOT MODIFY without explicit permission.
Commit: [COMMIT_HASH]
Tag: stable_together_v1
Test Coverage: 95%

Test suite includes:
- Provider initialization
- Text generation
- Error handling
- Custom model support
- System prompt handling
- Live API testing (haiku generation)

To run these tests:
PYTHONPATH=src pytest tests/test_providers/test_together.py -v

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
from send_2_llm.types import ProviderType, LLMRequest, LLMResponse, TokenUsage, LLMMetadata, ProviderAPIError
from send_2_llm.providers.together import TogetherProvider
from datetime import datetime


# !!! STABLE TESTS - DO NOT MODIFY !!!
# Базовые тесты Together AI провайдера
# ==================================

@pytest.mark.asyncio
async def test_together_provider_initialization():
    """Test Together AI provider initialization."""
    with patch.dict('os.environ', {'TOGETHER_API_KEY': 'test-key'}):
        provider = TogetherProvider()
        assert provider.provider_type == ProviderType.TOGETHER
        assert provider.default_model == "meta-llama/Llama-Vision-Free"
        assert provider.api_key == "test-key"
        
    # Test initialization without API key
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(Exception, match="TOGETHER_API_KEY environment variable not set"):
            TogetherProvider()


@pytest.mark.asyncio
async def test_together_generate():
    """Test Together AI text generation."""
    provider = TogetherProvider()
    request = LLMRequest(
        prompt="Test prompt",
        model="meta-llama/Llama-Vision-Free",
        max_tokens=100
    )
    
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
    mock_response.model = "meta-llama/Llama-Vision-Free"
    mock_response.model_dump.return_value = {
        "id": "test-id",
        "model": "meta-llama/Llama-Vision-Free",
        "choices": [{"message": {"content": "Test response"}}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
    }
    
    with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = mock_response
        response = await provider.generate(request)
        
        assert response.text == "Test response"
        assert response.metadata.provider == ProviderType.TOGETHER
        assert response.metadata.model == "meta-llama/Llama-Vision-Free"
        assert response.metadata.usage.prompt_tokens == 10
        assert response.metadata.usage.completion_tokens == 20
        assert response.metadata.usage.total_tokens == 30
        # Check cost calculation (Together AI pricing: $0.0004 per 1K tokens)
        expected_cost = 0.0004 * (30/1000)  # $0.0004 per 1K tokens
        assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_together_system_prompt():
    """Test Together AI with system prompt."""
    with patch.dict('os.environ', {'TOGETHER_API_KEY': 'test-key'}):
        provider = TogetherProvider()
        request = LLMRequest(
            prompt="Test prompt",
            model="meta-llama/Llama-Vision-Free",
            extra_params={"system_prompt": "You are a helpful assistant"}
        )
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_response.model = "meta-llama/Llama-Vision-Free"
        mock_response.model_dump.return_value = {
            "id": "test-id",
            "model": "meta-llama/Llama-Vision-Free",
            "choices": [{"message": {"content": "Test response"}}],
            "usage": {"prompt_tokens": 15, "completion_tokens": 25, "total_tokens": 40}
        }
        
        with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
            mock_create.return_value = mock_response
            response = await provider.generate(request)
            
            assert response.text == "Test response"
            assert response.metadata.provider == ProviderType.TOGETHER
            assert response.metadata.model == "meta-llama/Llama-Vision-Free"
            assert response.metadata.usage.prompt_tokens == 15
            assert response.metadata.usage.completion_tokens == 25
            assert response.metadata.usage.total_tokens == 40
            # Check cost calculation (Together AI pricing: $0.0004 per 1K tokens)
            expected_cost = 0.0004 * (40/1000)  # $0.0004 per 1K tokens
            assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


@pytest.mark.asyncio
async def test_together_error_handling():
    """Test Together AI error handling."""
    with patch.dict('os.environ', {'TOGETHER_API_KEY': 'test-key'}):
        provider = TogetherProvider()
        request = LLMRequest(prompt="Test prompt")
        
        with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
            mock_create.side_effect = Exception("API Error")
            with pytest.raises(Exception):
                await provider.generate(request)


@pytest.mark.asyncio
async def test_together_custom_model():
    """Test Together AI with custom model."""
    with patch.dict('os.environ', {'TOGETHER_API_KEY': 'test-key'}):
        provider = TogetherProvider()
        request = LLMRequest(
            prompt="Test prompt",
            model="meta-llama/Llama-2-70b-chat"
        )
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_response.model = "meta-llama/Llama-2-70b-chat"
        mock_response.model_dump.return_value = {
            "id": "test-id",
            "model": "meta-llama/Llama-2-70b-chat",
            "choices": [{"message": {"content": "Test response"}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
        }
        
        with patch.object(provider.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
            mock_create.return_value = mock_response
            response = await provider.generate(request)
            
            assert response.text == "Test response"
            assert response.metadata.provider == ProviderType.TOGETHER
            assert response.metadata.model == "meta-llama/Llama-2-70b-chat"
            assert response.metadata.usage.prompt_tokens == 10
            assert response.metadata.usage.completion_tokens == 20
            assert response.metadata.usage.total_tokens == 30
            # Check cost calculation (Together AI pricing: $0.0004 per 1K tokens)
            expected_cost = 0.0004 * (30/1000)  # $0.0004 per 1K tokens
            assert response.metadata.usage.cost == pytest.approx(expected_cost, rel=1e-6)


# !!! STABLE LIVE TESTS - DO NOT MODIFY !!!
# Креативные тесты с живым API
# ===========================

@pytest.mark.asyncio
@pytest.mark.live
async def test_together_generate_russian_haiku_live():
    """Live test of Together AI haiku generation in Russian."""
    print("\n" + "="*50)
    print("ГЕНЕРАЦИЯ НОВОГО ХАЙКУ")
    print("="*50)
    
    provider = TogetherProvider()
    
    request = LLMRequest(
        prompt="""Сгенерируй хайку о программировании на русском языке. 
        Следуй традиционной схеме 5-7-5 слогов.
        Хайку должно быть поэтичным и образным.
        Используй метафоры и технические термины.
        
        Пример формата:
        [первая строка - 5 слогов]
        [вторая строка - 7 слогов]
        [третья строка - 5 слогов]""",
        model="meta-llama/Llama-Vision-Free",
        max_tokens=50,
        temperature=0.8,  # Больше креативности для разнообразия
        extra_params={
            "system_prompt": "Ты - опытный поэт, специализирующийся на хайку. Твои хайку всегда точно следуют формату 5-7-5 слогов."
        }
    )
    
    response = await provider.generate(request)
    print("\nСгенерированное хайку:")
    print("-" * 30)
    print(response.text)
    print("-" * 30)
    print(f"\nМодель: {response.metadata.model}")
    print(f"Токены: {response.metadata.usage.total_tokens}")
    print(f"Время: {response.metadata.latency:.2f} сек.")

    assert response.text, "Response should not be empty"
    assert response.metadata.model == "meta-llama/Llama-Vision-Free"
    assert response.metadata.usage.total_tokens > 0
    assert response.metadata.latency > 0 