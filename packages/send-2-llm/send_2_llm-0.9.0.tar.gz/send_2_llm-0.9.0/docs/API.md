# API Reference

## Основные способы использования

### 1. Простой синхронный интерфейс

Самый простой способ использования библиотеки для базовых скриптов:

```python
from send_2_llm import send_2_llm_sync

# Простой вызов
response = send_2_llm_sync("Привет!")
print(response.text)

# С дополнительными параметрами
response = send_2_llm_sync(
    "Напиши хайку",
    temperature=0.9,
    output_format="markdown"
)
```

### 2. Асинхронный интерфейс

Рекомендуемый способ для асинхронных приложений:

```python
from send_2_llm import send_2_llm

async def main():
    response = await send_2_llm("Привет!")
    print(response.text)
```

### 3. Продвинутый интерфейс

Для полного контроля над процессом:

```python
from send_2_llm import LLMClient

async with LLMClient() as client:
    response = await client.generate("Привет!")
```

## Параметры

Все интерфейсы поддерживают следующие параметры:

- `text` (str): Текст для отправки в LLM
- `strategy_type` (StrategyType, optional): Тип стратегии
- `provider_type` (ProviderType, optional): Провайдер для single strategy
- `providers` (List[ProviderType], optional): Список провайдеров
- `model` (str, optional): Модель для single strategy
- `models` (List[str], optional): Список моделей
- `output_format` (OutputFormat, optional): Формат вывода
- `**kwargs`: Дополнительные параметры для провайдера

## Форматы вывода

Поддерживаемые форматы (OutputFormat):
- RAW (по умолчанию)
- MARKDOWN
- TELEGRAM_MARKDOWN
- HTML
- JSON

## Стратегии

Доступные стратегии (StrategyType):
- SINGLE: Один провайдер
- FALLBACK: Несколько провайдеров с фолбэком
- PARALLEL: Параллельный запрос к нескольким провайдерам
- COST_OPTIMIZED: Оптимизация по стоимости

## Провайдеры

Поддерживаемые провайдеры (ProviderType):
- OPENAI
- TOGETHER
- ANTHROPIC
- PERPLEXITY
- DEEPSEEK
- GEMINI

## Ответ

Все методы возвращают `LLMResponse` со следующими полями:
- `text`: Текст ответа
- `metadata`: Метаданные ответа
  - `provider`: Использованный провайдер
  - `model`: Использованная модель
  - `usage`: Информация об использовании токенов
  - `cost`: Стоимость запроса
  - `latency`: Время ответа

## Рекомендации по выбору интерфейса

1. **send_2_llm_sync**: 
   - Для простых скриптов
   - Когда не важна производительность
   - Для быстрого прототипирования

2. **send_2_llm**:
   - Для асинхронных приложений
   - Когда важна производительность
   - В веб-приложениях

3. **LLMClient**:
   - Для сложной логики
   - При необходимости переиспользования клиента
   - Для кастомных стратегий 