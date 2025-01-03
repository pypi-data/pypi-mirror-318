"""Example script to generate formatted content using send_2_llm."""

import asyncio
from send_2_llm import LLMClient
from send_2_llm.config import load_config, reload_config
from send_2_llm.types import OutputFormat

# Clear config cache before loading
reload_config()

# Compact markdown formatting tail
MARKDOWN_TAIL = """

Format in markdown:
# for headers
- for lists
** for bold
` for inline code
``` for code blocks
> for quotes"""

async def generate_content():
    """Generate formatted content using the configured LLM provider."""
    # Load config once at start
    config = load_config()
    
    async with LLMClient() as client:
        # Example 1: Generate a simple structured text about space
        prompt = (
            "Напиши текст про космос, используя следующую структуру:\n"
            "1. Заголовок первого уровня\n"
            "2. Краткое описание с выделением важных частей\n"
            "3. Список из 3 интересных фактов\n"
            "4. Заключение с цитатой известного ученого"
            + MARKDOWN_TAIL
        )
        
        print("\n=== Prompt 1 ===")
        print(prompt)
        
        response = await client.generate(prompt, output_format=OutputFormat.MARKDOWN)
        
        print("\n=== Markdown текст про космос ===")
        print(response.text)
        print("\n=== Метаданные ===")
        print(f"Провайдер: {response.metadata.provider}")
        print(f"Модель: {response.metadata.model}")
        print(f"Токены: {response.metadata.usage.total_tokens}")
        print(f"Стоимость: ${response.metadata.usage.cost:.4f}")

        # Example 2: Generate a Python class documentation
        prompt = (
            "Напиши документацию для Python класса DataProcessor.\n"
            "Структура:\n"
            "1. Заголовок с названием класса\n"
            "2. Описание класса\n"
            "3. Основные методы (3-4 метода) в блоках кода\n"
            "4. Пример использования в блоке кода"
            + MARKDOWN_TAIL
        )
        
        print("\n=== Prompt 2 ===")
        print(prompt)
        
        response = await client.generate(prompt, output_format=OutputFormat.MARKDOWN)
        
        print("\n=== Markdown документация Python класса ===")
        print(response.text)
        print("\n=== Метаданные ===")
        print(f"Провайдер: {response.metadata.provider}")
        print(f"Модель: {response.metadata.model}")
        print(f"Токены: {response.metadata.usage.total_tokens}")
        print(f"Стоимость: ${response.metadata.usage.cost:.4f}")


if __name__ == "__main__":
    asyncio.run(generate_content()) 