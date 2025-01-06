# Руководство по устранению проблем

## Общие проблемы

### 1. Проблемы с Python

#### Ошибка: Python 3.11 не найден
```
Error: Python 3.11 is required but not found
```

**Решение:**
1. Установите Python 3.11:
   ```bash
   # Ubuntu/Debian
   sudo apt install python3.11
   
   # macOS
   brew install python@3.11
   ```

2. Проверьте установку:
   ```bash
   python3.11 --version
   ```

### 2. Проблемы с виртуальным окружением

#### Ошибка: Не удается создать venv
```
Error: Command 'python3.11 -m venv venv' failed
```

**Решение:**
1. Установите venv:
   ```bash
   # Ubuntu/Debian
   sudo apt install python3.11-venv
   ```

2. Проверьте права доступа:
   ```bash
   sudo chown -R $USER:$USER .
   ```

### 3. Проблемы с установкой пакета

#### Ошибка: Не удается установить зависимости
```
ERROR: Failed building wheel for [package]
```

**Решение:**
1. Обновите pip:
   ```bash
   pip install --upgrade pip
   ```

2. Установите системные зависимости:
   ```bash
   # Ubuntu/Debian
   sudo apt install python3.11-dev build-essential
   ```

### 4. Проблемы с API ключами

#### Ошибка: API ключ не найден
```
Error: OPENAI_API_KEY not found in environment variables
```

**Решение:**
1. Проверьте наличие файла .env:
   ```bash
   ls -la .env
   ```

2. Проверьте содержимое .env:
   ```bash
   # Должно быть в .env
   OPENAI_API_KEY=your_key_here
   ```

3. Проверьте загрузку переменных:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   print(os.getenv("OPENAI_API_KEY"))
   ```

### 5. Проблемы с импортом

#### Ошибка: Модуль не найден
```
ModuleNotFoundError: No module named 'send_2_llm'
```

**Решение:**
1. Проверьте активацию venv:
   ```bash
   source venv/bin/activate
   ```

2. Проверьте установку пакета:
   ```bash
   pip list | grep send_2_llm
   ```

3. Переустановите пакет:
   ```bash
   pip install -e .
   ```

## Чистая установка

Если у вас возникли проблемы, попробуйте чистую установку:

```bash
# 1. Удалите старые файлы
rm -rf venv
rm -rf *.egg-info
rm -rf build dist

# 2. Создайте новое окружение
python3.11 -m venv venv
source venv/bin/activate

# 3. Установите пакет
./install.sh
```

## Проверка установки

Запустите тестовый скрипт:
```bash
python examples/test_openai_simple.py
```

## Логирование

Для отладки включите логирование:
```bash
export DEBUG=1
python your_script.py
```

## Поддержка

Если проблема не решена:
1. Проверьте [известные проблемы](https://github.com/your-repo/issues)
2. Создайте issue с:
   - Версией Python
   - Операционной системой
   - Полным текстом ошибки
   - Шагами для воспроизведения 