# Send 2 LLM

Гибкая библиотека для работы с различными LLM провайдерами.

## Установка

Выберите удобный способ:

```bash
# Способ 1: Прямая установка
pip install send-2-llm

# Способ 2: Через requirements.txt
pip install -r requirements.txt
```

## Быстрый старт

```python
from send_2_llm import LLMClient

async def main():
    # Создаем клиент
    client = LLMClient()
    
    # Отправляем запрос
    response = await client.generate("Напиши короткое хайку о программировании")
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Требования
- Python 3.11+
- API ключи провайдеров (см. документацию)

## Поддерживаемые провайдеры
- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude)
- Together AI
- Google Gemini

## Документация
Полная документация доступна в [docs/](docs/).

## Примеры
Больше примеров в [examples/](examples/):
- Базовые примеры
- Работа с разными провайдерами
- Асинхронная обработка
- Стратегии отказоустойчивости 