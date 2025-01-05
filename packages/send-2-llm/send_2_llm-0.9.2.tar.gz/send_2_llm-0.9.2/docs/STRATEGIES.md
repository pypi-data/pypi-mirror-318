# Стратегии Send2LLM

## Обзор

Send2LLM поддерживает различные стратегии обработки запросов к LLM:

### Basic Strategy
- Прямая отправка запросов к провайдеру
- Базовая валидация и обработка ошибок
- Подходит для простых случаев

### Retry Strategy
- Автоматические повторные попытки при ошибках
- Экспоненциальная задержка
- Настраиваемое количество попыток

### Fallback Strategy
- Автоматическое переключение между провайдерами
- Приоритезация провайдеров
- Обработка специфичных ошибок

### Chain Strategy
- Последовательное выполнение запросов
- Агрегация результатов
- Условная логика

## Использование

### Basic Strategy
```python
from send_2_llm.strategies import BasicStrategy
from send_2_llm.providers import OpenAIProvider

provider = OpenAIProvider(api_key="your_key")
strategy = BasicStrategy(provider=provider)

response = await strategy.execute("Your prompt")
```

### Retry Strategy
```python
from send_2_llm.strategies import RetryStrategy

strategy = RetryStrategy(
    provider=provider,
    max_retries=3,
    delay=1.0,
    exponential=True,
    retry_on=[
        "RateLimitError",
        "TimeoutError",
        "ServiceUnavailableError"
    ]
)

response = await strategy.execute("Your prompt")
```

### Fallback Strategy
```python
from send_2_llm.strategies import FallbackStrategy
from send_2_llm.providers import (
    OpenAIProvider,
    PerplexityProvider,
    AnthropicProvider
)

providers = [
    OpenAIProvider(api_key="key1"),
    PerplexityProvider(api_key="key2"),
    AnthropicProvider(api_key="key3")
]

strategy = FallbackStrategy(
    providers=providers,
    fallback_on_errors=True,
    max_attempts=3
)

response = await strategy.execute("Your prompt")
```

### Chain Strategy
```python
from send_2_llm.strategies import ChainStrategy

def aggregate_results(responses):
    return "\n".join(r.text for r in responses)

strategy = ChainStrategy(
    providers=[provider1, provider2],
    aggregation=aggregate_results,
    parallel=True
)

response = await strategy.execute("Your prompt")
```

## Конфигурация

### Basic Strategy
```python
BasicStrategy(
    provider: BaseProvider,
    timeout: float = 30.0,
    validate_input: bool = True,
    validate_output: bool = True
)
```

### Retry Strategy
```python
RetryStrategy(
    provider: BaseProvider,
    max_retries: int = 3,
    delay: float = 1.0,
    exponential: bool = True,
    retry_on: List[str] = None,
    jitter: bool = True
)
```

### Fallback Strategy
```python
FallbackStrategy(
    providers: List[BaseProvider],
    fallback_on_errors: bool = True,
    max_attempts: int = 3,
    provider_timeout: float = 30.0,
    total_timeout: float = 90.0
)
```

### Chain Strategy
```python
ChainStrategy(
    providers: List[BaseProvider],
    aggregation: Callable = None,
    parallel: bool = False,
    max_parallel: int = 3,
    timeout: float = 60.0
)
```

## Обработка ошибок

### Типы ошибок
```python
class StrategyError(Exception):
    """Base class for strategy errors."""
    pass

class RetryError(StrategyError):
    """Error when all retries failed."""
    pass

class FallbackError(StrategyError):
    """Error when all fallbacks failed."""
    pass

class ChainError(StrategyError):
    """Error in chain execution."""
    pass
```

### Обработка
```python
try:
    response = await strategy.execute("Your prompt")
except RetryError as e:
    print(f"All retries failed: {e}")
except FallbackError as e:
    print(f"All providers failed: {e}")
except ChainError as e:
    print(f"Chain execution failed: {e}")
```

## Метрики

### Retry Strategy
```python
strategy.metrics
{
    'total_retries': 5,
    'successful_retries': 3,
    'failed_retries': 2,
    'average_retry_delay': 2.5,
    'total_time': 10.5
}
```

### Fallback Strategy
```python
strategy.metrics
{
    'total_attempts': 3,
    'successful_provider': 'openai',
    'failed_providers': ['anthropic'],
    'total_time': 15.2
}
```

### Chain Strategy
```python
strategy.metrics
{
    'total_providers': 2,
    'successful_providers': 2,
    'execution_time': 8.5,
    'parallel_batches': 1
}
```

## Логирование

### Настройка
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('send2llm.strategies')
```

### Примеры логов
```
INFO:send2llm.strategies.retry:Attempt 1 failed, retrying in 1.0s
INFO:send2llm.strategies.fallback:Provider openai failed, falling back to anthropic
INFO:send2llm.strategies.chain:Starting parallel execution with 2 providers
```

## Рекомендации

### Выбор стратегии

1. **Basic Strategy**
   - Простые запросы
   - Надежный провайдер
   - Низкая латентность

2. **Retry Strategy**
   - Нестабильная сеть
   - Rate limiting
   - Временные ошибки

3. **Fallback Strategy**
   - Критичные запросы
   - Разные провайдеры
   - Высокая доступность

4. **Chain Strategy**
   - Сложные запросы
   - Агрегация ответов
   - Параллельная обработка

### Оптимизация

1. **Производительность**
   - Используйте параллельное выполнение
   - Настройте таймауты
   - Оптимизируйте retry delay

2. **Надежность**
   - Добавьте мониторинг
   - Логируйте ошибки
   - Используйте метрики

3. **Стоимость**
   - Приоритезируйте провайдеров
   - Контролируйте retry
   - Оптимизируйте токены 