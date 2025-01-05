"""
Тест генерации текста через send_2_llm API.
"""

import pytest
from send_2_llm import LLMClient
from send_2_llm.types import ProviderType


@pytest.mark.asyncio
async def test_text_generation(monkeypatch):
    """
    Проверяем генерацию текста через send_2_llm API
    """
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    monkeypatch.setenv("LLM_PROVIDER", "perplexity")
    
    async with LLMClient() as client:
        response = await client.generate("Test prompt")
        
        # Проверяем основные поля
        assert response.text  # Текст должен быть не пустым
        assert response.metadata.provider == ProviderType.PERPLEXITY
        assert response.metadata.model  # Модель должна быть указана
        assert response.metadata.usage.total_tokens > 0  # Должны быть использованы токены
        assert response.metadata.finish_reason in ["stop", "length"]  # Причина остановки должна быть валидной 