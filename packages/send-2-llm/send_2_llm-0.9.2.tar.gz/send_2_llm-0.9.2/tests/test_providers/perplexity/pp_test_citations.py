"""
Тест обработки цитат Perplexity.
"""

import pytest
from send_2_llm.providers.perplexity import PerplexityProvider


def test_perplexity_citations():
    """
    Проверяем что провайдер правильно обрабатывает цитаты из ответа API
    """
    provider = PerplexityProvider()
    
    # Пример ответа от API
    api_response = {
        "choices": [{
            "message": {"content": "Test response"}
        }],
        "citations": [{"url": "https://example.com/1"}]
    }
    
    # Извлекаем цитаты напрямую
    citations = provider._extract_citations(api_response)
    
    # Проверяем что цитата правильно извлечена
    assert len(citations) == 1
    assert citations[0].url == "https://example.com/1" 