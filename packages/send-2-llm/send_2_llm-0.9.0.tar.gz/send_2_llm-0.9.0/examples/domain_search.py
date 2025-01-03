"""
Domain search example using Perplexity AI provider.
Shows how to use web search capabilities with domain filtering.
"""

import asyncio
from datetime import datetime
from dotenv import load_dotenv
from send_2_llm import LLMClient
from send_2_llm.config import reload_config
from send_2_llm.types import ProviderType


async def chat():
    """Chat with domain-filtered web search."""
    load_dotenv()  # Load environment variables from .env
    reload_config()  # Clear config cache
    
    # Define allowed domains
    domains = [
        "wikipedia.org",
        "arxiv.org",
        "nature.com",
        "science.org",
        "sciencedirect.com",
        "springer.com",
        "ieee.org"
    ]
    
    print("\n=== Чат с поиском по научным доменам ===")
    print("Провайдер использует поиск только по научным сайтам:")
    print(", ".join(domains))
    print("\nВведите ваш текст (или 'exit' для выхода)")
    print("=" * 40)
    
    # Initialize session stats
    session_start = datetime.now()
    total_messages = 0
    total_tokens = 0
    total_cost = 0.0
    
    # Create client with Perplexity provider
    async with LLMClient(provider_type=ProviderType.PERPLEXITY) as client:
        while True:
            try:
                # Get user input
                user_input = input("\nВы: ").strip()
                if user_input.lower() == 'exit':
                    break
                
                if not user_input:
                    continue
                
                # Generate response with domain-filtered web search
                response = await client.generate(
                    user_input,
                    web_search=True,
                    return_citations=True,
                    allowed_domains=domains
                )
                total_messages += 1
                
                # Print response
                print("\nLLM:", response.text)
                
                # Print citations if available
                if response.metadata.citations:
                    print("\nИсточники:")
                    for citation in response.metadata.citations:
                        print(f"- {citation}")
                
                # Print metadata
                print("\nМетаданные:")
                print(f"Провайдер: {response.metadata.provider}")
                print(f"Модель: {response.metadata.model}")
                print(f"Токены: {response.metadata.usage.total_tokens}")
                print(f"Стоимость: ${response.metadata.usage.cost:.6f}")
                print("-" * 40)
                
                # Update totals
                total_tokens += response.metadata.usage.total_tokens
                total_cost += response.metadata.usage.cost
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"\nОшибка: {str(e)}")
                continue
    
    # Print session summary
    session_duration = (datetime.now() - session_start).total_seconds()
    print("\nИтоги сессии:")
    print(f"Длительность: {session_duration:.1f} сек")
    print(f"Сообщений: {total_messages}")
    print(f"Всего токенов: {total_tokens}")
    print(f"Общая стоимость: ${total_cost:.6f}")
    if total_messages > 0:
        print(f"В среднем:")
        print(f"- {total_tokens/total_messages:.1f} токенов на сообщение")
        print(f"- ${total_cost/total_messages:.6f} на сообщение")
    print("\nДо свидания!")


if __name__ == "__main__":
    asyncio.run(chat()) 