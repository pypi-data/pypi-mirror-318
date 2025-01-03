"""Самый простой пример использования send_2_llm."""

from send_2_llm import send_2_llm_sync

# Простой вызов в одну строку
response = send_2_llm_sync("Привет! Расскажи анекдот")
print(response.text)

# Использование с дополнительными параметрами (опционально)
response = send_2_llm_sync(
    "Напиши хайку про программирование",
    temperature=0.9,  # Больше креативности
    output_format="markdown"  # Форматированный вывод
)
print("\nОтформатированное хайку:")
print(response.text) 