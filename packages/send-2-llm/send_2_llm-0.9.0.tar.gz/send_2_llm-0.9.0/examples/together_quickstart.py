"""
Together AI Quickstart Example
============================

This example demonstrates how to use Together AI
with OpenAI-compatible API.

Requirements:
- TOGETHER_API_KEY environment variable must be set
- Python 3.8+
- openai>=1.12.0
"""

import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

async def main():
    # Initialize client
    client = AsyncOpenAI(
        api_key=os.getenv("TOGETHER_API_KEY"),
        base_url="https://api.together.xyz/v1",
    )
    
    try:
        # Create chat completion
        response = await client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that speaks Russian."},
                {"role": "user", "content": "Напиши хайку о программировании с искусственным интеллектом"}
            ],
            temperature=0.7,
            max_tokens=128,
        )
        
        # Print response
        print("\nСгенерированный текст:")
        print("-" * 50)
        print(response.choices[0].message.content)
        print("-" * 50)
        
        # Print metadata
        print("\nМетаданные:")
        print(f"Использование токенов:")
        print(f"  - Токены промпта: {response.usage.prompt_tokens}")
        print(f"  - Токены ответа: {response.usage.completion_tokens}")
        print(f"  - Всего токенов: {response.usage.total_tokens}")
        
    finally:
        # Cleanup
        await client.close()

if __name__ == "__main__":
    # Check for API key
    if not os.getenv("TOGETHER_API_KEY"):
        print("Ошибка: Переменная окружения TOGETHER_API_KEY не установлена")
        exit(1)
        
    # Run the example
    asyncio.run(main()) 