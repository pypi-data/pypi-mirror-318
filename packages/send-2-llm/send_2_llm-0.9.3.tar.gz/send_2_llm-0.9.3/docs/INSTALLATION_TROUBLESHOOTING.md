# Руководство по устранению проблем установки

## Известные проблемы

### 1. Конфликт с pyenv

**Симптомы:**
- Пакет устанавливается, но не импортируется
- `python -c "import send_2_llm"` выдает ModuleNotFoundError
- Путь к Python показывает на pyenv shims

**Решение:**
```bash
# 1. Используйте полный путь к Python
/home/almaz/.pyenv/versions/3.11.0/bin/python3.11 -m venv venv

# 2. Активируйте venv через точку
. venv/bin/activate  # вместо source venv/bin/activate

# 3. Используйте абсолютный путь к проекту
cd /полный/путь/к/проекту
pip install -e .
```

### 2. Проблемы с зависимостями

**Симптомы:**
- Конфликты между setup.py и pyproject.toml
- Предупреждения о перезаписи install_requires

**Решение:**
- Используйте только pyproject.toml
- Удалите setup.py если он существует
- Убедитесь, что все зависимости указаны в секции dependencies

### 3. Проблемы с кэшем pip

**Симптомы:**
- Старые версии пакетов устанавливаются
- Изменения в коде не отражаются

**Решение:**
```bash
# Очистка всех артефактов
rm -rf venv* build dist src/*.egg-info src/__pycache__ src/send_2_llm/__pycache__

# Установка без использования кэша
pip install --no-cache-dir -e .
```

### 4. Проблемы с версией Python

**Симптомы:**
- Ошибка: "Package requires Python version >=3.11"
- Неправильная версия Python используется

**Решение:**
- Проверьте версию Python: `python -V`
- Убедитесь, что используете Python 3.11+
- При необходимости установите нужную версию через pyenv:
  ```bash
  pyenv install 3.11.0
  pyenv local 3.11.0
  ```

### 5. Проблемы с правами доступа

**Симптомы:**
- Ошибки доступа при установке
- Permission denied

**Решение:**
- Не используйте sudo с pip
- Проверьте права доступа к директориям:
  ```bash
  chmod -R u+w .
  chown -R $USER:$USER .
  ```

## Процедура чистой установки

1. Очистка окружения:
```bash
deactivate 2>/dev/null || true
rm -rf venv* build dist src/*.egg-info src/__pycache__ src/send_2_llm/__pycache__
```

2. Создание нового окружения:
```bash
/полный/путь/к/python3.11 -m venv venv
. venv/bin/activate
```

3. Обновление инструментов:
```bash
pip install --upgrade pip setuptools wheel
```

4. Установка пакета:
```bash
pip install -e .
```

5. Проверка установки:
```bash
python -c "import send_2_llm; print(send_2_llm.__version__)"
```

## Советы по отладке

1. Проверяйте используемый Python:
```bash
which python
python -V
```

2. Проверяйте содержимое site-packages:
```bash
ls -la venv/lib/python3.11/site-packages/
```

3. Проверяйте PYTHONPATH:
```bash
python -c "import sys; print('\n'.join(sys.path))"
```

4. Проверяйте метаданные пакета:
```bash
ls -la src/send_2_llm.egg-info/
``` 