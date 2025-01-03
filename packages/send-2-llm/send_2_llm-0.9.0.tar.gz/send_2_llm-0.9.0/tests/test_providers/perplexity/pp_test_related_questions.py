"""
Тест связанных вопросов Perplexity.
"""

import pytest
from send_2_llm.types import ProviderType


def test_extract_related_questions():
    """
    Проверяем извлечение связанных вопросов из ответа API
    """
    from send_2_llm.providers.perplexity import PerplexityProvider
    
    provider = PerplexityProvider()
    
    # Пример ответа от API
    api_response = {
        "choices": [{
            "message": {"content": "Test response"}
        }],
        "related_questions": [
            "Question 1?",
            "Question 2?",
            {"text": "Question 3?"}
        ]
    }
    
    # Извлекаем вопросы напрямую
    questions = provider._extract_related_questions(api_response)
    
    # Проверяем что вопросы правильно извлечены
    assert len(questions) == 3
    assert all(isinstance(q, str) for q in questions)
    assert "Question 1?" in questions
    assert "Question 2?" in questions
    assert "Question 3?" in questions 