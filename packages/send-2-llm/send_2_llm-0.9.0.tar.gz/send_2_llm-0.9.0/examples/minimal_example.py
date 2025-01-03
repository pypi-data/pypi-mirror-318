"""Minimal example using send_2_llm."""

import asyncio
from dotenv import load_dotenv
from send_2_llm import LLMClient


async def main():
    """Simple example of using send_2_llm."""
    load_dotenv()  # Load environment variables from .env
    
    async with LLMClient() as client:
        response = await client.generate("Расскажи анекдот про программиста")
        print(response.text)


if __name__ == "__main__":
    asyncio.run(main()) 