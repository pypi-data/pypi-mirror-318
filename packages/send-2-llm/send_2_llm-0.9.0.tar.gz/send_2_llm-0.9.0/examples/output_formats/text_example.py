#!/usr/bin/env python3
"""Example of using send_2_llm with plain text output format."""

import asyncio
from send_2_llm import send_2_llm
from send_2_llm.types import OutputFormat

async def main():
    """Run text format example."""
    # Simple text response
    response = await send_2_llm(
        "Напиши короткое стихотворение про осень",
        output_format=OutputFormat.TEXT
    )
    print("\nPlain text response:")
    print(response.text)
    
    # Text with specific formatting request
    response = await send_2_llm(
        "Напиши рецепт борща. Используй только текст, без специального форматирования",
        output_format=OutputFormat.TEXT
    )
    print("\nFormatted text response:")
    print(response.text)

if __name__ == "__main__":
    asyncio.run(main()) 