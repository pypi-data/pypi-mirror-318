# Стратегии LLM и их конфигурация

## Поддерживаемые и планируемые провайдеры

### Текущие провайдеры
1. Together AI [STABLE]
   - Модели:
     * meta-llama/Llama-Vision-Free (default)
     * mistralai/Mixtral-8x7B-Instruct-v0.1
     * meta-llama/Llama-2-70b-chat-hf
     * meta-llama/Llama-2-13b-chat-hf
   - Особенности:
     * OpenAI-совместимый API
     * Высокая стабильность
     * Поддержка многоходовых диалогов

2. OpenAI [STABLE]
   - Модели:
     * gpt-4o-mini-2024-07-18
     * gpt-4
   - Особенности:
     * Высокая точность
     * Надежный API
     * Предсказуемая стоимость

### Планируемые провайдеры
1. Anthropic
   - Модели:
     * claude-3-opus
     * claude-3-sonnet
     * claude-2.1
   - Особенности:
     * Высокая точность
     * Большой контекст
     * Анализ изображений (claude-3)

2. Google Gemini
   - Модели:
     * gemini-pro
     * gemini-ultra
   - Особенности:
     * Мультимодальность
     * Интеграция с Google API
     * Высокая производительность

3. OpenRouter
   - Особенности:
     * Единый API для множества моделей
     * Автоматическое переключение
     * Оптимизация стоимости
   - Доступные модели:
     * anthropic/claude-3
     * google/gemini-pro
     * meta/llama-2
     * mistral/mixtral-8x7b

4. DeepSeek
   - Модели:
     * deepseek-chat
     * deepseek-coder
   - Особенности:
     * Специализация на коде
     * Низкая стоимость
     * Высокая производительность

5. Perplexity
   - Модели:
     * pplx-7b-online
     * pplx-70b-online
     * pplx-7b-chat
     * pplx-70b-chat
   - Особенности:
     * Онлайн-поиск и анализ
     * Актуальная информация
     * Высокая точность ответов
     * Интеграция с веб-источниками
     * RAG (Retrieval-Augmented Generation)

## Основной метод: send_2_llm

Основной метод для взаимодействия с LLM:
```python
response = await client.generate("текст для отправки")
```

## Конфигурация через .env

Поведение метода определяется настройками в файле `.env`:

### 1. Выбор стратегии
```env
LLM_STRATEGY=single  # Доступные опции: single, fallback, parallel, cost_optimized
```

### 2. Настройка провайдера по умолчанию
```env
DEFAULT_PROVIDER=openai  # Используется для single strategy
```

### 3. Настройка модели по умолчанию
```env
OPENAI_MODEL=gpt-4o-mini-2024-07-18  # Модель по умолчанию для OpenAI
TOGETHER_MODEL=meta-llama/Llama-Vision-Free  # Модель по умолчанию для Together
```

## Стратегии

### Single Provider Strategy
- Использует один провайдер
- Конфигурация:
  ```env
  LLM_STRATEGY=single
  DEFAULT_PROVIDER=openai
  OPENAI_MODEL=gpt-4o-mini-2024-07-18
  ```
- Пример использования:
  ```python
  response = await client.generate("Какой сегодня день?")
  # Использует OpenAI gpt-4o-mini по умолчанию
  ```

### Fallback Strategy
- Пробует несколько провайдеров по очереди
- Конфигурация:
  ```env
  LLM_STRATEGY=fallback
  LLM_PROVIDERS=openai,together,anthropic
  DEFAULT_MODELS=gpt-4o-mini,mixtral-8x7b,claude-2
  ```
- Пример использования:
  ```python
  response = await client.generate("Сложный вопрос")
  # Пробует провайдеров по очереди, пока не получит ответ
  ```

## Приоритеты конфигурации

1. Параметры в вызове метода:
```python
response = await client.generate(
    "текст",
    provider_type=ProviderType.OPENAI,
    model="gpt-4"
)
```

2. Переменные окружения в `.env`
3. Значения по умолчанию в коде

## Примеры использования

### Базовое использование
```python
from send_2_llm import LLMClient

async with LLMClient() as client:
    response = await client.generate("Какой сегодня день?")
    print(response.text)
```

### Переопределение настроек
```python
from send_2_llm import LLMClient, ProviderType

async with LLMClient() as client:
    # Использование другого провайдера для конкретного запроса
    response = await client.generate(
        "Сложный вопрос",
        provider_type=ProviderType.TOGETHER,
        model="mistralai/Mixtral-8x7B-Instruct-v0.1"
    )
    print(response.text)
```

## Обработка ошибок

- Если провайдер недоступен:
  ```python
  try:
      response = await client.generate("текст")
  except ProviderAPIError as e:
      print(f"Ошибка провайдера: {e}")
  ```

- Если стратегия не поддерживается:
  ```python
  try:
      client = LLMClient(strategy_type="unsupported")
  except ValueError as e:
      print(f"Неверная стратегия: {e}")
  ```

## Рекомендации

1. Всегда указывайте модель по умолчанию для каждого провайдера в `.env`
2. Для production используйте fallback стратегию с несколькими провайдерами
3. Используйте single стратегию для тестирования и разработки
4. Регулярно проверяйте доступность и стоимость моделей 