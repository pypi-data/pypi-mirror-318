"""
Пример использования API для получения связанных вопросов.
"""

import asyncio
import json
from typing import List

from send_2_llm.providers import PerplexityProvider
from send_2_llm.types import (
    RelatedQuestionsRequest,
    RelatedQuestionsConfig,
    RelatedQuestionsGenerator
)

async def print_related_questions(questions_response):
    """Красиво печатаем ответ с вопросами."""
    print("\n=== Связанные вопросы ===")
    for i, q in enumerate(questions_response.questions, 1):
        print(f"{i}. {q.text} (confidence: {q.confidence}, source: {q.source})")
    
    print("\n=== Метаданные ===")
    print(json.dumps(questions_response.metadata, indent=2, ensure_ascii=False))

async def example_1():
    """Простой пример - получение связанных вопросов с дефолтными настройками."""
    provider = PerplexityProvider()
    
    request = RelatedQuestionsRequest(
        original_question="Какая погода сегодня в Казани?"
    )
    
    response = await provider.get_related_questions(request)
    await print_related_questions(response)

async def example_2():
    """Пример с кастомной конфигурацией генератора вопросов."""
    provider = PerplexityProvider()
    
    # Создаем кастомный генератор вопросов
    generator = RelatedQuestionsGenerator(
        system_prompt="""Сгенерируй 3 вопроса о погоде:
        1. Один про прогноз на завтра
        2. Один про осадки
        3. Один про ветер""",
        max_questions=3,
        temperature=0.8
    )
    
    # Создаем конфиг с нашим генератором
    config = RelatedQuestionsConfig(
        enabled=True,
        generator=generator
    )
    
    # Создаем запрос
    request = RelatedQuestionsRequest(
        original_question="Какая погода сегодня в Набережных Челнах?",
        config=config,
        max_questions=3,
        min_confidence=0.7
    )
    
    response = await provider.get_related_questions(request)
    await print_related_questions(response)

async def example_3():
    """Пример с фильтрацией результатов."""
    provider = PerplexityProvider()
    
    request = RelatedQuestionsRequest(
        original_question="Какая погода в Татарстане?",
        max_questions=2,  # Получим только 2 вопроса
        min_confidence=0.8  # С высокой уверенностью
    )
    
    response = await provider.get_related_questions(request)
    await print_related_questions(response)

async def main():
    """Запускаем все примеры."""
    print("\n=== Пример 1: Базовое использование ===")
    await example_1()
    
    print("\n=== Пример 2: Кастомная конфигурация ===")
    await example_2()
    
    print("\n=== Пример 3: Фильтрация результатов ===")
    await example_3()

if __name__ == "__main__":
    asyncio.run(main()) 