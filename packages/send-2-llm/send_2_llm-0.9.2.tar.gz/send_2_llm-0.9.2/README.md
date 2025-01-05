# Send2LLM

[![PyPI version](https://badge.fury.io/py/send-2-llm.svg)](https://badge.fury.io/py/send-2-llm)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Гибкая библиотека для работы с различными LLM провайдерами

## Особенности

- 🔄 Единый интерфейс для всех LLM провайдеров
- 🚀 Асинхронная работа из коробки
- 📊 Мониторинг использования и стоимости
- 🎨 Красивый CLI интерфейс
- 🔌 Легкое добавление новых провайдеров

## Быстрая установка

### Через pip

```bash
pip install send-2-llm  # Базовая установка
```

### С дополнительными провайдерами:

```bash
pip install "send-2-llm[openai]"    # Только OpenAI
pip install "send-2-llm[anthropic]"  # Только Anthropic
pip install "send-2-llm[gemini]"     # Только Gemini
pip install "send-2-llm[all]"        # Все провайдеры + инструменты разработки
```

### Через установочные скрипты

```bash
# Установка Gemini провайдера
./scripts/install/gemini.sh
```

## Простой пример

```python
from send_2_llm import LLMClient
from send_2_llm.types import ProviderType, LLMRequest

async def main():
    client = LLMClient(provider_type=ProviderType.OPENAI)
    
    response = await client.generate(
        LLMRequest(
            prompt="Привет, как дела?",
            max_tokens=100
        )
    )
    
    print(response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Документация

Полная документация доступна на [GitHub Pages](https://ai-tools-team.github.io/send_2_llm)

## Разработка

Для разработки установите дополнительные зависимости:

```bash
pip install "send-2-llm[dev]"
```

## Структура проекта

```
send_2_llm/
├── docs/              # Документация
├── examples/          # Примеры использования
├── requirements/      # Зависимости по группам
│   └── providers/    # Зависимости провайдеров
├── scripts/          # Скрипты проекта
│   └── install/      # Установочные скрипты
├── src/              # Исходный код
└── tests/            # Тесты
```

## Лицензия

MIT License - см. файл [LICENSE](LICENSE) 