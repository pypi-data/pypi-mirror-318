# Send 2 LLM

Гибкая библиотека для работы с различными LLM провайдерами.

## Быстрый старт

```bash
# Установка
./install.sh

# Запуск примера
python examples/test_openai_simple.py
```

## Требования
- Python 3.11+
- API ключи (см. .env.example)

## Установка

### Простая установка (рекомендуется)
```bash
# Базовая установка
./install.sh

# Установка для разработки
./install.sh -d
```

Скрипт автоматически:
- Находит Python 3.11
- Создает виртуальное окружение
- Устанавливает все зависимости
- Создает .env файл из шаблона
- Проверяет установку

### Ручная установка
```bash
# 1. Создайте виртуальное окружение
python3.11 -m venv venv
. venv/bin/activate

# 2. Установите пакет
pip install -e .         # базовая установка
pip install -e .[dev]    # для разработки

# 3. Создайте .env файл
cp .env.example .env
```

## Примеры

### Базовое использование
```python
import asyncio
from dotenv import load_dotenv
from send_2_llm import LLMClient
from send_2_llm.types import ProviderType

async def main():
    # Загрузка переменных окружения
    load_dotenv()
    
    # Инициализация клиента
    client = LLMClient(provider_type=ProviderType.OPENAI)
    
    # Генерация ответа
    response = await client.generate(
        prompt="Generate a short haiku about programming",
        max_tokens=50
    )
    
    print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### Больше примеров
См. [examples/README.md](examples/README.md) для:
- Базовых примеров
- Работы с разными провайдерами
- Асинхронной обработки
- Стратегий отказоустойчивости

## Поддерживаемые провайдеры
- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude)
- Together AI
- Google Gemini 