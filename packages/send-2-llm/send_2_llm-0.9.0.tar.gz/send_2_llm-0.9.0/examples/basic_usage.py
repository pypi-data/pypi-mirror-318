"""Basic usage example of send_2_llm."""

import asyncio
from dotenv import load_dotenv
from send_2_llm import send_2_llm
from send_2_llm.config import reload_config


async def main():
    """Basic usage example."""
    # Load environment variables from .env
    load_dotenv()
    
    # Clear config cache (optional)
    reload_config()
    
    print("\n=== Базовый пример использования send_2_llm ===")
    
    # Simple prompt
    prompt = "Напиши хайку про весну"
    print(f"\nЗапрос: {prompt}")
    
    # Generate response
    response = await send_2_llm(prompt)
    
    # Print response
    print("\nОтвет:")
    print(response.text)
    
    # Print metadata
    print("\nМетаданные:")
    print(f"Провайдер: {response.metadata.provider}")
    print(f"Модель: {response.metadata.model}")
    print(f"Токены: {response.metadata.usage.total_tokens}")
    print(f"Стоимость: ${response.metadata.usage.cost:.6f}")
    
    # More complex prompt
    prompt = """Сгенерируй три варианта названия для:
    - Научно-фантастического рассказа о первом контакте с инопланетянами
    - Действие происходит в Сибири
    - Атмосфера должна быть загадочной и немного тревожной
    - Названия должны быть на русском языке
    """
    print(f"\nЗапрос: {prompt}")
    
    # Generate response with different parameters
    response = await send_2_llm(
        prompt,
        max_tokens=200,  # Longer response
        temperature=0.8  # More creative
    )
    
    # Print response
    print("\nОтвет:")
    print(response.text)
    
    # Print metadata
    print("\nМетаданные:")
    print(f"Провайдер: {response.metadata.provider}")
    print(f"Модель: {response.metadata.model}")
    print(f"Токены: {response.metadata.usage.total_tokens}")
    print(f"Стоимость: ${response.metadata.usage.cost:.6f}")


if __name__ == "__main__":
    asyncio.run(main()) 