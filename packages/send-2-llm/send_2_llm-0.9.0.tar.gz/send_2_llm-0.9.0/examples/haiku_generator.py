"""Simple script to generate haiku using send_2_llm."""

import asyncio
from send_2_llm import LLMClient
from send_2_llm.config import load_config, reload_config

# Clear config cache before loading
reload_config()

async def generate_haiku():
    """Generate a haiku using the configured LLM provider."""
    # Load config once at start
    config = load_config()
    
    async with LLMClient() as client:
        prompt = (
            "Напиши креативное хайку на русском языке postmodern humor meta in meta. not trivial, highly creative,originality\n"
            "Формат: 5-7-5 слогов." 
        )
        
        response = await client.generate(prompt)
        
        print("\n=== Сгенерированное хайку ===")
        print(response.text)
        print("\n=== Метаданные ===")
        print(f"Провайдер: {response.metadata.provider}")
        print(f"Модель: {response.metadata.model}")
        print(f"Токены: {response.metadata.usage.total_tokens}")
        print(f"Стоимость: ${response.metadata.usage.cost:.4f}")


if __name__ == "__main__":
    asyncio.run(generate_haiku()) 