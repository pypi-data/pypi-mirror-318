"""Tests for Gemini provider."""

import os
from datetime import datetime
import pytest
from unittest.mock import patch, MagicMock

from send_2_llm.types import (
    ProviderType,
    LLMRequest,
    LLMResponse,
    ProviderAPIError
)
from send_2_llm.providers.gemini import GeminiProvider


@pytest.fixture
def mock_genai():
    """Mock google.generativeai module."""
    with patch("send_2_llm.providers.gemini.genai") as mock:
        mock.configure = MagicMock()
        mock.GenerativeModel = MagicMock()
        mock.types = MagicMock()
        mock.types.GenerationConfig = MagicMock()
        yield mock


@pytest.fixture
def mock_response():
    """Create mock response."""
    response = MagicMock()
    response.text = "Test response"
    response.model_dump = MagicMock(return_value={"text": "Test response"})
    return response


@pytest.mark.asyncio
async def test_gemini_provider_initialization(mock_genai):
    """Test basic provider initialization."""
    with patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}):
        provider = GeminiProvider()
        
        # Check basic attributes
        assert provider.provider_type == ProviderType.GEMINI
        assert provider.default_model == "gemini-1.5-flash"
        
        # Verify API configuration
        mock_genai.configure.assert_called_once_with(api_key="test-key")
        
        # Verify model initialization
        mock_genai.GenerativeModel.assert_called_once_with(
            model_name="gemini-1.5-flash"
        )


@pytest.mark.asyncio
async def test_gemini_provider_no_api_key(mock_genai):
    """Test initialization without API key."""
    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(ProviderAPIError) as exc_info:
            GeminiProvider()
        assert "GEMINI_API_KEY environment variable not set" in str(exc_info.value)


@pytest.mark.asyncio
async def test_gemini_provider_generate(mock_genai, mock_response):
    """Test text generation."""
    with patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}):
        # Setup mock model
        mock_model = MagicMock()
        mock_model.generate_content = MagicMock(return_value=mock_response)
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Create provider and request
        provider = GeminiProvider()
        request = LLMRequest(prompt="Test prompt")
        
        # Generate response
        response = await provider.generate(request)
        
        # Verify response
        assert isinstance(response, LLMResponse)
        assert response.text == "Test response"
        assert response.metadata.provider == ProviderType.GEMINI
        assert response.metadata.model == "gemini-1.5-flash"
        assert response.metadata.raw_response == {"text": "Test response"}
        
        # Verify generate_content was called correctly
        mock_model.generate_content.assert_called_once_with(
            "Test prompt",
            generation_config={
                "temperature": request.temperature,
                "top_p": request.top_p,
                "top_k": 40,
                "max_output_tokens": request.max_tokens or 2048,
            }
        )


@pytest.mark.asyncio
async def test_gemini_provider_api_error(mock_genai):
    """Test API error handling."""
    with patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}):
        # Setup mock model with error
        mock_model = MagicMock()
        mock_model.generate_content = MagicMock(side_effect=Exception("API Error"))
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Create provider and request
        provider = GeminiProvider()
        request = LLMRequest(prompt="Test prompt")
        
        # Verify error handling
        with pytest.raises(ProviderAPIError) as exc_info:
            await provider.generate(request)
        assert "Gemini API error" in str(exc_info.value)


@pytest.mark.asyncio
@pytest.mark.live
async def test_gemini_generate_russian_haiku_live():
    """Live test of Gemini haiku generation in Russian."""
    print("\n" + "="*50)
    print("ГЕНЕРАЦИЯ НОВОГО ХАЙКУ ЧЕРЕЗ GEMINI")
    print("="*50)
    
    provider = GeminiProvider()
    
    request = LLMRequest(
        prompt="""Сгенерируй хайку о весне на русском языке. 
        Следуй традиционной схеме 5-7-5 слогов.
        Хайку должно быть поэтичным и образным.
        Используй метафоры и природные образы.
        
        Пример формата:
        [первая строка - 5 слогов]
        [вторая строка - 7 слогов]
        [третья строка - 5 слогов]""",
        temperature=0.8  # Больше креативности для разнообразия
    )
    
    response = await provider.generate(request)
    
    print("\n=== Новое хайку от Gemini ===")
    print(response.text)
    print("="*30)
    print("="*30 + "\n")
    
    # Проверяем базовую структуру
    assert isinstance(response, LLMResponse)
    
    # Проверяем формат хайку
    haiku_lines = response.text.strip().split('\n')
    assert len(haiku_lines) == 3, "Хайку должно состоять ровно из трёх строк"
    
    # Проверяем, что текст на русском (содержит кириллицу)
    assert any(ord('а') <= ord(c) <= ord('я') for c in response.text.lower()), "Текст должен содержать русские буквы"
    
    # Проверяем метаданные
    assert response.metadata.provider == ProviderType.GEMINI
    assert response.metadata.model == "gemini-1.5-flash"
    
    # Сохраняем сгенерированное хайку в файл для истории
    with open("tests/generated_haiku_history.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== GEMINI {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write(response.text)
        f.write("\n") 