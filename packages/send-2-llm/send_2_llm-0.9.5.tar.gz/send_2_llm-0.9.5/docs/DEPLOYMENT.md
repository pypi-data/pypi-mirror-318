# Развертывание Send2LLM

## Требования

### Системные требования
- Python 3.11+
- pip 21.0+
- git
- 2GB RAM минимум
- 10GB свободного места

### Зависимости
- OpenAI SDK
- Rich
- Click
- PyYAML
- Pydantic
- python-dotenv

## Установка

### Из PyPI
```bash
pip install send2llm
```

### Из исходников
```bash
git clone https://github.com/yourusername/send2llm.git
cd send2llm
pip install -e .
```

## Конфигурация

### Основная конфигурация
1. Создайте `.env` файл:
```bash
cp .env.example .env
```

2. Настройте API ключи:
```env
OPENAI_API_KEY=your_key
PERPLEXITY_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
```

3. Настройте модели по умолчанию:
```env
DEFAULT_PROVIDER=openai
OPENAI_MODEL=gpt-4
PERPLEXITY_MODEL=sonar-medium-online
ANTHROPIC_MODEL=claude-2
```

### Логирование
1. Создайте директорию для логов:
```bash
mkdir -p ~/.send_2_llm/logs
```

2. Настройте права:
```bash
chmod 755 ~/.send_2_llm/logs
```

3. Проверьте логирование:
```bash
send2llm logs
```

## Развертывание

### Локальное
1. Активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Проверьте установку:
```bash
send2llm config
```

### Docker
1. Соберите образ:
```bash
docker build -t send2llm .
```

2. Запустите контейнер:
```bash
docker run -it --env-file .env send2llm
```

### Systemd сервис
1. Создайте сервис:
```ini
[Unit]
Description=Send2LLM Service
After=network.target

[Service]
Type=simple
User=send2llm
WorkingDirectory=/opt/send2llm
Environment=PYTHONPATH=/opt/send2llm
ExecStart=/opt/send2llm/venv/bin/python -m send2llm
Restart=always

[Install]
WantedBy=multi-user.target
```

2. Установите сервис:
```bash
sudo cp send2llm.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable send2llm
sudo systemctl start send2llm
```

## Мониторинг

### Логи
- CLI логи: `~/.send_2_llm/logs/cli.log`
- Запросы: `~/.send_2_llm/logs/requests.log`
- Ошибки: `~/.send_2_llm/logs/errors.log`

### Статистика
```bash
# Общая статистика
send2llm logs --action analyze

# Статистика за период
send2llm logs --action analyze --days 30
```

### Ротация логов
```bash
# Автоматическая ротация
send2llm logs --action rotate

# Очистка старых логов
send2llm logs --action cleanup --days 30
```

## Обновление

### Из PyPI
```bash
pip install --upgrade send2llm
```

### Из исходников
```bash
git pull origin main
pip install -e .
```

### Миграция данных
1. Сохраните конфигурацию:
```bash
cp .env .env.backup
cp -r ~/.send_2_llm/logs ~/logs_backup
```

2. Обновите пакет
3. Восстановите конфигурацию:
```bash
cp .env.backup .env
cp -r ~/logs_backup/* ~/.send_2_llm/logs/
```

## Безопасность

### API ключи
- Храните в `.env`
- Регулярно обновляйте
- Ограничивайте доступ

### Логи
- Не логируйте чувствительные данные
- Регулярно очищайте
- Защищайте доступ

### Сеть
- Используйте HTTPS
- Настройте файрвол
- Ограничьте доступ

## Устранение проблем

### Проблемы с API
1. Проверьте ключи
2. Проверьте квоты
3. Проверьте доступность API

### Проблемы с логами
1. Проверьте права доступа
2. Проверьте место на диске
3. Проверьте ротацию

### Системные проблемы
1. Проверьте память
2. Проверьте CPU
3. Проверьте диск 