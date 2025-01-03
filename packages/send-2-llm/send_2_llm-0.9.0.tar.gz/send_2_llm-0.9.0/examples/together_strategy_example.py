"""
Together AI Strategy Example
==========================

This example demonstrates how to use the Together AI strategy
with OpenAI-compatible API.

Requirements:
- TOGETHER_API_KEY environment variable must be set
- Python 3.8+
- Dependencies from requirements.txt

Models available:
- mistralai/Mixtral-8x7B-Instruct-v0.1 (recommended)
- meta-llama/Llama-2-70b-chat-hf
- meta-llama/Llama-2-13b-chat-hf
- meta-llama/Llama-2-7b-chat-hf
- NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
"""

import os
import asyncio
from dotenv import load_dotenv
from send_2_llm.strategies.together_strategy import TogetherStrategy

# Load environment variables
load_dotenv()

async def main():
    # Initialize Together AI strategy
    strategy = TogetherStrategy(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,  # Higher temperature for more creative responses
        max_tokens=512,   # Limit response length
        system_prompt="You are a helpful assistant that speaks Russian.",
    )
    
    try:
        # Generate a response
        response = await strategy.generate(
            "Напиши хайку о программировании с искусственным интеллектом"
        )
        
        # Print the response
        print("\nСгенерированный текст:")
        print("-" * 50)
        print(response.text)
        print("-" * 50)
        
        # Print metadata
        print("\nМетаданные:")
        print(f"Провайдер: {response.metadata.provider}")
        print(f"Модель: {response.metadata.model}")
        print(f"Использование токенов:")
        print(f"  - Токены промпта: {response.metadata.usage.prompt_tokens}")
        print(f"  - Токены ответа: {response.metadata.usage.completion_tokens}")
        print(f"  - Всего токенов: {response.metadata.usage.total_tokens}")
        
    finally:
        # Cleanup
        await strategy.close()

if __name__ == "__main__":
    # Check for API key
    if not os.getenv("TOGETHER_API_KEY"):
        print("Ошибка: Переменная окружения TOGETHER_API_KEY не установлена")
        exit(1)
        
    # Run the example
    asyncio.run(main()) 