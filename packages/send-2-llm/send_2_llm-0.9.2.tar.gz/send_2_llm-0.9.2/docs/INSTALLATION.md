# Установка Send2LLM

## Системные требования

- Python 3.11+
- pip 21.0+
- venv (рекомендуется)
- git

## Быстрая установка

1. Клонирование репозитория:
```bash
git clone https://github.com/yourusername/send2llm.git
cd send2llm
```

2. Создание виртуального окружения:
```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
.\venv\Scripts\activate  # Windows
```

3. Установка зависимостей:
```bash
pip install -r requirements.txt
```

4. Настройка окружения:
```bash
cp .env.example .env
# Отредактируйте .env файл, добавив необходимые API ключи
```

## Конфигурация провайдеров

### OpenAI
```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4  # или другая модель
```

### Perplexity
```env
PERPLEXITY_API_KEY=your_api_key
PERPLEXITY_MODEL=sonar-medium-online
```

### Anthropic
```env
ANTHROPIC_API_KEY=your_api_key
ANTHROPIC_MODEL=claude-2
```

## Проверка установки

1. Активация окружения:
```bash
source venv/bin/activate  # Linux/Mac
# или
.\venv\Scripts\activate  # Windows
```

2. Проверка конфигурации:
```bash
send2llm config
```

3. Тестовый запрос:
```bash
send2llm "Hello, world!"
```

## Дополнительные компоненты

### Логирование
По умолчанию логи сохраняются в:
```
~/.send_2_llm/logs/
├── cli.log
├── requests.log
└── errors.log
```

Управление логами:
```bash
# Просмотр статуса
send2llm logs

# Ротация логов
send2llm logs --action rotate

# Очистка старых логов
send2llm logs --action cleanup

# Анализ использования
send2llm logs --action analyze
```

## Обновление

1. Получение последних изменений:
```bash
git pull origin main
```

2. Обновление зависимостей:
```bash
pip install -r requirements.txt --upgrade
```

## Устранение проблем

### Проблемы с зависимостями
```bash
# Очистка кэша pip
pip cache purge

# Переустановка зависимостей
pip install -r requirements.txt --no-cache-dir
```

### Проблемы с правами доступа
```bash
# Проверка прав на директорию логов
ls -la ~/.send_2_llm/logs/

# Исправление прав
chmod -R 755 ~/.send_2_llm/logs/
```

### Проблемы с API ключами
1. Проверьте наличие файла `.env`
2. Убедитесь, что ключи действительны
3. Проверьте формат ключей
4. Попробуйте экспортировать ключи в окружение:
```bash
export OPENAI_API_KEY=your_api_key
``` 