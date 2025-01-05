# Стабильные компоненты

## Механизмы защиты стабильных компонентов

### Файл .cursorrules
Все стабильные компоненты защищены через файл `.cursorrules`, который требует:
- Тройного подтверждения перед изменением защищенных файлов
- Предотвращения автоматических изменений
- Явного разрешения на модификацию
- Поддержания покрытия тестами >95%
- Сохранения предупреждающих заголовков
- Сохранения тегов стабильности

### Защитные комментарии
Все методы стабильных провайдеров содержат:
- Предупреждающие заголовки о стабильности
- Описание защищенной функциональности
- Требования к зависимостям
- Правила модификации

### Версионный контроль
- Отслеживание стабильных тегов
- Сохранение истории коммитов
- Обязательная документация изменений
- Обновление CHANGELOG.md при изменениях

### Процесс изменения защищенных файлов
1. Получить тройное подтверждение от пользователя
2. Проверить наличие предупреждающих комментариев
3. Убедиться в сохранении тестового покрытия
4. Обновить документацию
5. Создать новый тег версии
6. Обновить CHANGELOG.md

## Общие стабильные компоненты

### Защищенные файлы
- `.env` - Критические настройки и API ключи
- `.cursorrules` - Правила защиты файлов
- `requirements.txt` - Зависимости проекта
- `setup.py` - Конфигурация установки
- `src/send_2_llm/types.py` - Базовые типы
- `src/send_2_llm/client.py` - Клиентский интерфейс
- `src/send_2_llm/providers/factory.py` - Фабрика провайдеров

### Тестовая инфраструктура
- `t.sh` - Основной скрипт тестирования
- `tests/conftest.py` - Конфигурация тестов
- `tests/test_factory.py` - Тесты фабрики
- `tests/test_client.py` - Тесты клиента

## OpenAI Integration (Tag: stable_openai_v1)

### Защищенные файлы
- `src/send_2_llm/providers/openai.py`
- `tests/test_providers/test_openai.py`
- `tests/test_openai_connection.py`

### Критическая функциональность
- OpenAI provider initialization
- Chat completion generation
- Error handling
- Token usage tracking
- Response metadata handling

### Защищенные зависимости
- openai>=1.12.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- python-dotenv>=1.0.0
- pydantic>=2.0.0

### Инструкции по восстановлению
1. Восстановить стабильную версию:
   ```bash
   git checkout stable_openai_v1
   ```
2. Запустить тесты:
   ```bash
   ./t.sh openai
   ```
3. Проверить покрытие тестами (должно быть >95%)

## Together AI Integration (Tag: stable_together_v1)

### Защищенные файлы
- `src/send_2_llm/providers/together.py`
- `tests/test_providers/test_together.py`
- `docs/STRATEGIES.md` (Together AI related sections)

### Критическая функциональность
- Together AI provider initialization
- Chat completion generation via OpenAI SDK
- System prompt handling via extra_params
- Error handling
- Token usage tracking
- Response metadata handling
- Default model configuration (meta-llama/Llama-Vision-Free)

### Защищенные зависимости
- openai>=1.12.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

### Инструкции по восстановлению
1. Восстановить стабильную версию:
   ```bash
   git checkout stable_together_v1
   ```
2. Запустить тесты:
   ```bash
   ./t.sh together
   ```
3. Проверить покрытие тестами (должно быть >95%)

## Anthropic Integration (Tag: stable_anthropic_v1)

### Защищенные файлы
- `src/send_2_llm/providers/anthropic.py`
- `tests/test_providers/test_anthropic.py`
- `docs/STRATEGIES.md` (Anthropic related sections)

### Критическая функциональность
- Anthropic provider initialization
- Chat completion generation
- Error handling and fallback strategy
- Token usage tracking
- Response metadata handling
- Default model configuration (claude-3-haiku-20240307)
- Russian haiku generation
- Multi-model support:
  - claude-3-haiku-20240307
  - claude-3-5-sonnet-latest
  - claude-3-5-haiku-latest

### Защищенные зависимости
- anthropic>=0.18.1
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

### Инструкции по восстановлению
1. Восстановить стабильную версию:
   ```bash
   git checkout stable_anthropic_v1
   ```
2. Запустить тесты:
   ```bash
   ./t.sh anthropic
   ```
3. Проверить покрытие тестами (должно быть >95%)

## DeepSeek Integration (Tag: stable_deepseek_v1)

### Защищенные файлы
- `src/send_2_llm/providers/deepseek.py`
- `tests/test_providers/test_deepseek.py`
- `docs/STRATEGIES.md` (DeepSeek related sections)

### Критическая функциональность
- DeepSeek provider initialization
- Chat completion generation
- Error handling and fallback strategy
- Token usage tracking
- Response metadata handling
- Default model configuration (deepseek-chat)
- Chat model support

### Защищенные зависимости
- deepseek>=0.1.0
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

### Инструкции по восстановлению
1. Восстановить стабильную версию:
   ```bash
   git checkout stable_deepseek_v1
   ```
2. Запустить тесты:
   ```bash
   ./t.sh deepseek
   ```
3. Проверить покрытие тестами (должно быть >95%)

## Gemini Integration (Tag: stable_gemini_v1)

### Защищенные файлы
- `src/send_2_llm/providers/gemini.py`
- `tests/test_providers/test_gemini.py`
- `docs/STRATEGIES.md` (Gemini related sections)

### Критическая функциональность
- Gemini provider initialization
- Chat completion generation
- Error handling and fallback strategy
- Response metadata handling
- Default model configuration (gemini-1.5-flash)
- Russian haiku generation
- Raw response handling
- Temperature и top_p control

### Защищенные зависимости
- google-generativeai>=0.3.2
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- pydantic>=2.0.0

### Инструкции по восстановлению
1. Восстановить стабильную версию:
   ```bash
   git checkout stable_gemini_v1
   ```
2. Запустить тесты:
   ```bash
   ./t.sh gemini
   ```
3. Проверить покрытие тестами (должно быть >95%)

## Процесс внесения изменений

### 1. Подготовка
- Создать новую ветку от стабильной версии
- Документировать планируемые изменения
- Получить разрешение на изменения
- Создать резервную копию файлов

### 2. Разработка
- Создавать новые файлы вместо изменения существующих
- Следовать шаблонам из стабильной версии
- Поддерживать совместимость с существующими тестами
- Сохранять все предупреждающие комментарии

### 3. Тестирование
- Запустить все тесты через t.sh
- Проверить покрытие кода
- Убедиться в обратной совместимости
- Проверить интеграционные тесты

### 4. Документация
- Обновить CHANGELOG.md
- Обновить PROGRESS.md
- Обновить STRATEGIES.md
- Обновить API.md при необходимости
- Создать новый тег версии 