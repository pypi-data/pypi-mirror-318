# Руководство для контрибьюторов

## Начало работы

1. Форкните репозиторий
2. Клонируйте свой форк:
```bash
git clone https://github.com/your-username/send2llm.git
cd send2llm
```

3. Создайте виртуальное окружение:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

4. Установите зависимости для разработки:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Структура проекта

```
send_2_llm/
├── docs/              # Документация
├── examples/          # Примеры использования
├── src/              # Исходный код
│   └── send_2_llm/
│       ├── cli/      # CLI интерфейс
│       ├── config/   # Конфигурация
│       ├── providers/ # Провайдеры LLM
│       ├── strategies/ # Стратегии
│       └── types/    # Типы данных
├── tests/            # Тесты
└── tools/            # Инструменты разработки
```

## Рабочий процесс

1. Создайте ветку для новой функциональности:
```bash
git checkout -b feature/your-feature
```

2. Внесите изменения, следуя стандартам:
- Используйте типизацию
- Добавляйте документацию
- Следуйте PEP 8
- Пишите тесты

3. Запустите проверки:
```bash
# Линтер
ruff check .

# Типы
mypy src tests

# Тесты
pytest
```

4. Создайте коммит:
```bash
git add .
git commit -m "feat: add your feature"
```

5. Отправьте изменения:
```bash
git push origin feature/your-feature
```

6. Создайте Pull Request

## Стандарты кода

### Форматирование
- Используйте black для форматирования
- Максимальная длина строки: 88 символов
- Сортируйте импорты с isort

### Документация
- Docstrings в формате Google
- Актуализируйте README.md
- Обновляйте CHANGELOG.md

### Типизация
- Используйте type hints
- Проверяйте с mypy
- Избегайте Any

### Тестирование
- Покрытие кода > 90%
- Используйте pytest
- Моки для внешних сервисов

## Коммиты

### Типы
- feat: Новая функциональность
- fix: Исправление бага
- docs: Документация
- style: Форматирование
- refactor: Рефакторинг
- test: Тесты
- chore: Обслуживание

### Формат
```
type: short description

Long description if needed

Closes #123
```

## CI/CD

### GitHub Actions
- Линтинг
- Проверка типов
- Тесты
- Сборка документации

### Релизы
1. Обновите версию в pyproject.toml
2. Обновите CHANGELOG.md
3. Создайте тег:
```bash
git tag v1.2.3
git push origin v1.2.3
```

## Защищенные компоненты

См. [PROTECTED_FILES.md](PROTECTED_FILES.md)

## Логирование

### CLI логи
- ~/.send_2_llm/logs/cli.log
- Ротация по размеру
- Уровни: INFO, DEBUG

### Запросы
- ~/.send_2_llm/logs/requests.log
- Структурированный JSON
- Метрики использования

### Ошибки
- ~/.send_2_llm/logs/errors.log
- Полный стектрейс
- Контекст ошибки

## Конфигурация

### Файлы
- .env: API ключи
- config/*.yaml: Настройки

### Валидация
- Проверка типов
- Значения по умолчанию
- Документация полей

## Безопасность

### API ключи
- Только через .env
- Не коммитить в git
- Ротация при утечке

### Данные
- Санитизация ввода
- Безопасное логирование
- Защита токенов

## Вопросы

- GitHub Issues
- Discussions
- Pull Requests 