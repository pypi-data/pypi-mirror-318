# Руководство по развертыванию

## Требования к системе

- Python 3.8+
- PostgreSQL 12+
- Redis (опционально)
- Docker (опционально)

## Установка

### Через pip

```bash
pip install send2llm
```

### Через Docker

```bash
docker pull send2llm/send2llm
docker run -d -p 8000:8000 send2llm/send2llm
```

## Конфигурация

### Переменные окружения

```env
# Основные настройки
SEND2LLM_ENV=production
SEND2LLM_DEBUG=false
SEND2LLM_SECRET_KEY=your-secret-key

# База данных
SEND2LLM_DB_HOST=localhost
SEND2LLM_DB_PORT=5432
SEND2LLM_DB_NAME=send2llm
SEND2LLM_DB_USER=user
SEND2LLM_DB_PASSWORD=password

# Redis
SEND2LLM_REDIS_HOST=localhost
SEND2LLM_REDIS_PORT=6379

# API ключи для LLM сервисов
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

## Развертывание

### Локальное развертывание

1. Создайте и активируйте виртуальное окружение
2. Установите зависимости
3. Настройте переменные окружения
4. Запустите миграции
5. Запустите сервер

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn send2llm.main:app --host 0.0.0.0 --port 8000
```

### Docker Compose

```yaml
version: '3.8'
services:
  app:
    image: send2llm/send2llm
    ports:
      - "8000:8000"
    environment:
      - SEND2LLM_ENV=production
      - SEND2LLM_DB_HOST=db
    depends_on:
      - db
      - redis

  db:
    image: postgres:12
    environment:
      - POSTGRES_DB=send2llm
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password

  redis:
    image: redis:6
```

## Мониторинг

### Prometheus метрики

Доступны по адресу: `/metrics`

### Логирование

Логи сохраняются в:
- `/var/log/send2llm/app.log`
- `/var/log/send2llm/error.log`

## Масштабирование

### Горизонтальное масштабирование

1. Настройте балансировщик нагрузки
2. Добавьте новые инстансы
3. Настройте репликацию базы данных

### Вертикальное масштабирование

1. Увеличьте ресурсы сервера
2. Оптимизируйте настройки базы данных
3. Настройте кэширование

## Безопасность

1. Используйте HTTPS
2. Настройте файрвол
3. Регулярно обновляйте зависимости
4. Следите за уязвимостями

## Резервное копирование

### База данных

```bash
# Создание бэкапа
pg_dump -U user send2llm > backup.sql

# Восстановление
psql -U user send2llm < backup.sql
```

### Файлы конфигурации

Регулярно копируйте:
- `.env` файлы
- Конфигурационные файлы
- Сертификаты

## Обновление

1. Создайте резервную копию
2. Обновите код
3. Примените миграции
4. Перезапустите сервисы 