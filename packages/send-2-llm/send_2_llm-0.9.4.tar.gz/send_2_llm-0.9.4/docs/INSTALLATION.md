# Установка Send2LLM

## Быстрая установка для конкретного провайдера

### OpenAI
```bash
./scripts/install_openai.sh
```

### Anthropic
```bash
./scripts/install_anthropic.sh  # Скоро будет доступно
```

### Together AI
```bash
./scripts/install_together.sh   # Скоро будет доступно
```

## Ручная установка

### 1. Создание виртуального окружения
```bash
python3.11 -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install --upgrade pip
```

### 2. Установка базового пакета
```bash
pip install -e .
```

### 3. Установка провайдеров
```bash
# Только OpenAI
pip install -e ".[openai]"

# Только Anthropic
pip install -e ".[anthropic]"

# Все провайдеры
pip install -e ".[providers]"
```

### 4. Установка для разработки
```bash
pip install -e ".[dev]"
```

### 5. Полная установка
```bash
pip install -e ".[all]"
```

## Требования к системе
- Python 3.11+
- pip 21.0+
- venv (обычно входит в Python)

## Проверка установки

### OpenAI
```bash
python examples/test_openai_install.py
```

### Anthropic
```bash
python examples/test_anthropic_install.py  # Скоро будет доступно
```

## Решение проблем

### Проблемы с установкой
1. Убедитесь, что используете Python 3.11+
2. Обновите pip: `pip install --upgrade pip`
3. Проверьте, что все зависимости установлены: `pip list`

### Проблемы с импортом
1. Убедитесь, что находитесь в правильном виртуальном окружении
2. Проверьте установку пакета: `pip show send_2_llm`

### Проблемы с API
1. Проверьте наличие файла .env
2. Убедитесь, что API ключи правильно установлены
3. Проверьте доступ к API провайдера 