# Защищенные файлы проекта

## Правила защиты
- Все перечисленные файлы требуют тройного подтверждения перед изменением
- Автоматические изменения запрещены
- Необходимо явное разрешение на модификацию
- Все изменения должны сохранять тестовое покрытие >95%
- Все файлы должны сохранять предупреждающие заголовки
- Все файлы должны сохранять теги стабильности
- Все изменения должны быть отражены в CHANGELOG.md

## Общие защищенные файлы
### Файлы
- `.env`
- `.cursorrules`
- `requirements.txt`
- `setup.py`
- `src/send_2_llm/types.py`
- `src/send_2_llm/client.py`
- `src/send_2_llm/providers/factory.py`

## OpenAI Integration (stable_openai_v1)
### Файлы
- `src/send_2_llm/providers/openai.py`
- `tests/test_providers/test_openai.py`
- `tests/test_openai_connection.py`

### Зависимости
- openai>=1.12.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- python-dotenv>=1.0.0
- pydantic>=2.0.0

## Together AI Integration (stable_together_v1)
### Файлы
- `src/send_2_llm/providers/together.py`
- `tests/test_providers/test_together.py`

### Зависимости
- openai>=1.12.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

## Anthropic Integration (stable_anthropic_v1)
### Файлы
- `src/send_2_llm/providers/anthropic.py`
- `tests/test_providers/test_anthropic.py`

### Зависимости
- anthropic>=0.18.1
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

## DeepSeek Integration (stable_deepseek_v1)
### Файлы
- `src/send_2_llm/providers/deepseek.py`
- `tests/test_providers/test_deepseek.py`

### Зависимости
- deepseek>=0.1.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

## Gemini Integration (stable_gemini_v1)
### Файлы
- `src/send_2_llm/providers/gemini.py`
- `tests/test_providers/test_gemini.py`

### Зависимости
- google-generativeai>=0.3.2
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

## Perplexity Integration (in development)
### Файлы
- `src/send_2_llm/providers/perplexity.py`
- `tests/test_providers/test_perplexity.py`

### Зависимости
- perplexity>=0.1.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

## Тестовая инфраструктура
### Файлы
- `t.sh`
- `tests/conftest.py`
- `tests/test_factory.py`
- `tests/test_client.py`

## Процесс изменения защищенных файлов

### 1. Подготовка
- Проверить файл в списке защищенных
- Получить тройное подтверждение от пользователя
- Создать резервную копию файла
- Проверить наличие актуальной документации

### 2. Проверки
- Убедиться в наличии предупреждающих комментариев
- Проверить наличие тегов стабильности
- Проверить зависимости
- Проверить совместимость с другими компонентами

### 3. Изменения
- Внести необходимые изменения
- Сохранить все предупреждающие комментарии
- Сохранить все теги стабильности
- Обновить версии в соответствующих файлах

### 4. Тестирование
- Запустить полный набор тестов
- Проверить покрытие кода (>95%)
- Убедиться в обратной совместимости
- Проверить интеграционные тесты

### 5. Документация
- Обновить CHANGELOG.md
- Обновить PROGRESS.md
- Создать новый тег версии
- Обновить список защищенных файлов
- Обновить документацию API при необходимости

## Восстановление стабильной версии

В случае проблем после изменений:
1. Восстановить из резервной копии
2. Или использовать git:
   ```bash
   git checkout [stable_tag]
   ```
3. Запустить полный набор тестов:
   ```bash
   ./t.sh
   ```
4. Проверить все зависимые компоненты:
   ```bash
   PYTHONPATH=src pytest tests/ -v
   ``` 