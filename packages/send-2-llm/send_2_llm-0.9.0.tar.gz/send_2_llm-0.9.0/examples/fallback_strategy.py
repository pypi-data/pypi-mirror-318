"""Example of using fallback strategy."""

import asyncio
from dotenv import load_dotenv

from send_2_llm import LLMClient
from send_2_llm.types import ProviderType, StrategyType


async def main():
    """Run fallback strategy example."""
    # Load environment variables
    load_dotenv()
    
    # Create client with fallback strategy
    providers = [
        ProviderType.OPENAI,
        ProviderType.ANTHROPIC,
        ProviderType.TOGETHER,
    ]
    
    models = [
        "gpt-3.5-turbo",  # OpenAI model
        "claude-2",        # Anthropic model
        "meta-llama/Llama-2-70b-chat-hf",  # Together model
    ]
    
    async with LLMClient(
        strategy_type=StrategyType.FALLBACK,
        providers=providers,
        models=models,
        temperature=0.7,
    ) as client:
        # Try generating response
        try:
            response = await client.generate(
                "Explain the concept of quantum entanglement in simple terms"
            )
            print(f"\nResponse from {response.metadata.provider}:")
            print(f"Model: {response.metadata.model}")
            print(f"Text: {response.text}")
            print(f"Tokens: {response.metadata.usage.total_tokens}")
            print(f"Cost: ${response.metadata.usage.cost:.4f}")
            
        except Exception as e:
            print(f"All providers failed: {str(e)}")
            
    # Override providers on the fly
    async with LLMClient(
        strategy_type=StrategyType.FALLBACK,
        providers=[ProviderType.TOGETHER, ProviderType.OPENAI],
        models=["meta-llama/Llama-2-70b-chat-hf", "gpt-4"],
    ) as client:
        try:
            response = await client.generate(
                "What is the meaning of life?",
                providers=[ProviderType.ANTHROPIC, ProviderType.DEEPSEEK],
                models=["claude-2", "deepseek-chat"],
            )
            print(f"\nResponse from {response.metadata.provider}:")
            print(f"Model: {response.metadata.model}")
            print(f"Text: {response.text}")
            print(f"Tokens: {response.metadata.usage.total_tokens}")
            print(f"Cost: ${response.metadata.usage.cost:.4f}")
            
        except Exception as e:
            print(f"All providers failed: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main()) 