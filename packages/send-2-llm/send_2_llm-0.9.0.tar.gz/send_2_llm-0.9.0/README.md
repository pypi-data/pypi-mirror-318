# send_2_llm

Гибкая Python библиотека для работы с различными LLM провайдерами.

## Установка

```bash
pip install send_2_llm  # Базовая установка
pip install send_2_llm[openai]  # С конкретным провайдером
pip install send_2_llm[all]  # Со всеми провайдерами
```

## Простое использование

```python
from send_2_llm import send_2_llm_sync

# Простой вызов
response = send_2_llm_sync("Привет!")
print(response.text)

# С параметрами
response = send_2_llm_sync(
    "Напиши креативное хайку",
    temperature=0.9,
    output_format="markdown"
)
print(response.text)
```

## Асинхронное использование

```python
from send_2_llm import send_2_llm

async def main():
    response = await send_2_llm("Привет!")
    print(response.text)
```

## Основные возможности

- Поддержка множества провайдеров:
  - OpenAI
  - Together AI
  - Anthropic
  - Perplexity
  - DeepSeek
  - Gemini
- Простое переключение между провайдерами
- Стратегии использования:
  - Single: один провайдер
  - Fallback: автоматическое переключение при ошибках
  - Parallel: параллельные запросы
  - Cost-optimized: оптимизация по стоимости
- Форматирование ответов (markdown, html, json)
- Генерация связанных вопросов
- Кэширование
- Поддержка прокси
- Подробное логирование
- Типизация
- Асинхронность

## Документация

Полная документация доступна в директории `/docs`:
- [API Reference](docs/API.md)
- [Стратегии](docs/STRATEGIES.md)
- [Архитектура](docs/ARCHITECTURE.md)
- [Развертывание](docs/DEPLOYMENT.md)

## Лицензия

MIT 