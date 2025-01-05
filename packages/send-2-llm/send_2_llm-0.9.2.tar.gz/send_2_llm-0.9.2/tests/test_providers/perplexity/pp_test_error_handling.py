"""
Тест обработки ошибок Perplexity провайдера.
"""

import pytest
from send_2_llm.providers.perplexity import PerplexityProvider
from send_2_llm.types import LLMRequest


def test_parameter_validation(monkeypatch):
    """
    Проверяем валидацию входных параметров
    """
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    provider = PerplexityProvider()
    
    # Тест на пустой промпт
    with pytest.raises(ValueError) as exc_info:
        request = LLMRequest(prompt="")
        provider.validate_request(request)
    assert "Empty prompt" in str(exc_info.value)
    
    # Тест на некорректную temperature
    with pytest.raises(ValueError) as exc_info:
        request = LLMRequest(prompt="test", temperature=2.0)
        provider.validate_request(request)
    assert "Temperature must be between 0 and 1" in str(exc_info.value)
    
    # Тест на отрицательное значение max_tokens
    with pytest.raises(ValueError) as exc_info:
        request = LLMRequest(prompt="test", max_tokens=-1)
        provider.validate_request(request)
    assert "max_tokens must be positive" in str(exc_info.value) 