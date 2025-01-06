# Тестирование Send2LLM

## Структура тестов

```
tests/
├── unit/                 # Модульные тесты
│   ├── cli/             # Тесты CLI
│   ├── providers/       # Тесты провайдеров
│   ├── strategies/      # Тесты стратегий
│   └── types/          # Тесты типов
├── integration/         # Интеграционные тесты
│   ├── providers/      # Тесты интеграции с LLM
│   └── strategies/     # Тесты стратегий
└── e2e/                # End-to-end тесты
    └── cli/            # Тесты CLI
```

## Запуск тестов

### Все тесты
```bash
pytest
```

### Конкретные тесты
```bash
# Модульные тесты
pytest tests/unit

# Тесты CLI
pytest tests/unit/cli

# Тесты провайдеров
pytest tests/unit/providers
```

### С покрытием
```bash
pytest --cov=send_2_llm
```

## Конфигурация тестов

### pytest.ini
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
```

### conftest.py
```python
import pytest
from typing import Generator
from pathlib import Path

@pytest.fixture
def temp_log_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """Create temporary log directory."""
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    yield log_dir

@pytest.fixture
def mock_openai():
    """Mock OpenAI API."""
    ...

@pytest.fixture
def mock_perplexity():
    """Mock Perplexity API."""
    ...
```

## Типы тестов

### Модульные тесты

```python
def test_log_rotation(temp_log_dir):
    """Test log rotation functionality."""
    # Setup
    log_file = temp_log_dir / "test.log"
    log_file.write_text("test" * 1000000)  # 4MB
    
    # Execute
    rotate_logs(max_size_mb=1, max_backups=2)
    
    # Assert
    assert log_file.exists()
    assert (temp_log_dir / "test.1.log").exists()
    assert (temp_log_dir / "test.2.log").exists()
```

### Интеграционные тесты

```python
@pytest.mark.integration
async def test_openai_provider():
    """Test OpenAI provider integration."""
    provider = OpenAIProvider(
        api_key="test_key",
        model="gpt-4"
    )
    
    response = await provider.generate("Test prompt")
    
    assert response.text
    assert response.metadata.provider == ProviderType.OPENAI
```

### E2E тесты

```python
@pytest.mark.e2e
def test_cli_send_command(cli_runner):
    """Test CLI send command."""
    result = cli_runner.invoke(cli, ["send", "Test prompt"])
    
    assert result.exit_code == 0
    assert "Response from" in result.output
```

## Моки и фикстуры

### API моки

```python
class MockOpenAI:
    """Mock OpenAI API responses."""
    
    def generate(self, prompt: str) -> dict:
        return {
            "text": "Mocked response",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30
            }
        }

@pytest.fixture
def mock_openai(monkeypatch):
    """Provide mock OpenAI API."""
    mock = MockOpenAI()
    monkeypatch.setattr("send_2_llm.providers.openai.OpenAI", mock)
    return mock
```

### Временные файлы

```python
@pytest.fixture
def temp_config(tmp_path):
    """Create temporary config file."""
    config = tmp_path / "config.yaml"
    config.write_text("""
    providers:
      openai:
        model: gpt-4
        price_per_1k_tokens: 0.01
    """)
    return config
```

## Параметризация

```python
@pytest.mark.parametrize("provider,model", [
    ("openai", "gpt-4"),
    ("perplexity", "sonar-medium-online"),
    ("anthropic", "claude-2")
])
async def test_provider_config(provider, model):
    """Test provider configuration."""
    config = Config.load()
    provider_config = config.get_provider_config(provider)
    
    assert provider_config.model == model
```

## Асинхронные тесты

```python
@pytest.mark.asyncio
async def test_async_function():
    """Test async function."""
    result = await async_function()
    assert result

@pytest.fixture
async def async_client():
    """Create async client."""
    client = AsyncClient()
    await client.connect()
    yield client
    await client.disconnect()
```

## CI интеграция

### GitHub Actions

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Run tests
        run: |
          pytest --cov=send_2_llm
          coverage xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
```

## Отчеты

### Coverage

```bash
# HTML отчет
pytest --cov=send_2_llm --cov-report=html

# XML отчет для CI
pytest --cov=send_2_llm --cov-report=xml
```

### JUnit

```bash
pytest --junitxml=test-results.xml
```

## Советы

1. **Изоляция тестов**
   - Используйте фикстуры
   - Очищайте состояние
   - Избегайте глобальных переменных

2. **Производительность**
   - Маркируйте медленные тесты
   - Используйте параллельный запуск
   - Минимизируйте I/O операции

3. **Поддерживаемость**
   - Следуйте AAA (Arrange-Act-Assert)
   - Документируйте сложные тесты
   - Группируйте связанные тесты 