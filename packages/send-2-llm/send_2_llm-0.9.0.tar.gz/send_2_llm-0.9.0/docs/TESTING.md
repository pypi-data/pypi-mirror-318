# Testing Documentation

## Test Infrastructure

### t.sh Script
Основной инструмент для запуска тестов с улучшенным UX и отслеживанием прогресса.

#### Особенности
- Цветной вывод результатов
- Отслеживание прогресса для каждого провайдера
- Индивидуальный статус тестов
- Улучшенная отчетность
- Поддержка эмодзи для лучшего UX
- Нативная bash реализация
- Обновления статуса в реальном времени
- Четкие индикаторы успеха/неудачи
- Сводка по провайдерам
- Общая сводка тестов
- Счетчик неудачных тестов

#### Использование
```bash
# Запуск всех тестов
./t.sh

# Запуск тестов конкретного провайдера
./t.sh openai
./t.sh together
./t.sh anthropic
./t.sh deepseek
./t.sh gemini

# Запуск тестов с покрытием
./t.sh --coverage
```

#### Вывод
```
================================================================================
🚀 Starting test suite for send_2_llm
================================================================================

🔵 Testing OpenAI Provider
✅ Provider initialization: PASSED
✅ Chat completion: PASSED
✅ Error handling: PASSED
✅ Token tracking: PASSED

🔵 Testing Together AI Provider
✅ Provider initialization: PASSED
✅ Chat completion: PASSED
✅ System prompts: PASSED
✅ Model switching: PASSED

...

📊 Test Summary
================================================================================
✅ Total tests: 45
✅ Passed: 45
❌ Failed: 0
📈 Coverage: 96%
================================================================================
```

## Strategy Switching Tests

### Overview
Система поддерживает динамическое переключение между различными LLM провайдерами через переменные окружения.
Основной механизм - изменение `DEFAULT_PROVIDER` в файле `.env`.

### Тестируемые провайдеры
1. **OpenAI** (stable_openai_v1)
   - Chat completion
   - Token tracking
   - Error handling
   - Response metadata

2. **Together AI** (stable_together_v1)
   - OpenAI SDK compatibility
   - System prompts
   - Model switching
   - Token tracking

3. **Anthropic** (stable_anthropic_v1)
   - Claude 3 models
   - Russian haiku
   - Error handling
   - Multi-model support

4. **DeepSeek** (stable_deepseek_v1)
   - Chat model
   - Basic completion
   - Error handling
   - Token tracking

5. **Gemini** (stable_gemini_v1)
   - Chat completion
   - Temperature control
   - Russian haiku
   - Raw responses

### Test Structure
1. **Environment Management**
   - Save original environment state
   - Mock environment variables
   - Restore original state after tests

2. **Provider Verification**
   - Check correct provider selection
   - Verify metadata
   - Validate response format
   - Check model parameters

3. **Error Handling**
   - Invalid provider names
   - Missing API keys
   - Network issues
   - Invalid configurations
   - Fallback strategies

### Best Practices
1. **Environment Variables**
   - Всегда использовать `DEFAULT_PROVIDER` для переключения
   - Сохранять исходное состояние окружения
   - Использовать моки для тестов
   - Не модифицировать `.env` напрямую

2. **Test Cases**
   - Тестировать каждый переход между провайдерами
   - Проверять специфичные функции провайдеров
   - Проверять обработку ошибок
   - Валидировать метаданные ответов
   - Тестировать стратегии восстановления

3. **Maintenance**
   - Поддерживать актуальность тестов
   - Обновлять документацию
   - Следить за покрытием
   - Регулярно запускать тесты
   - Проверять стабильные компоненты

## Test Coverage Requirements

### Минимальные требования
- 95% покрытие для стабильных компонентов
- 90% покрытие для новых компонентов
- 100% покрытие критических путей
- Интеграционные тесты для всех провайдеров
- Тесты переключения стратегий

### Мониторинг покрытия
```bash
# Проверка покрытия всех тестов
./t.sh --coverage

# Проверка покрытия конкретного провайдера
./t.sh openai --coverage
```

## Future Improvements
1. **Additional Test Coverage**
   - [ ] Parallel strategy testing
   - [ ] Cost optimization testing
   - [ ] Performance benchmarking
   - [ ] Load testing
   - [ ] Multi-modal testing

2. **Monitoring**
   - [ ] Test metrics collection
   - [ ] Provider switching metrics
   - [ ] Error rate tracking
   - [ ] Response time monitoring
   - [ ] Cost tracking

3. **Infrastructure**
   - [ ] CI/CD integration
   - [ ] Automated test scheduling
   - [ ] Test result visualization
   - [ ] Coverage trend tracking
   - [ ] Performance regression detection 