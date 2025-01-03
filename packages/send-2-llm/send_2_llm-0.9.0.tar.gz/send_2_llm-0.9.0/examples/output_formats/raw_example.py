#!/usr/bin/env python3
"""Example of using send_2_llm with raw output format."""

import asyncio
from send_2_llm import send_2_llm
from send_2_llm.types import OutputFormat

async def main():
    """Run raw format example."""
    # Raw response without any formatting
    response = await send_2_llm(
        "Напиши пример кода на Python",
        output_format=OutputFormat.RAW
    )
    print("\nRaw response (code):")
    print(response.text)
    
    # Raw response with mixed content
    response = await send_2_llm(
        "Напиши текст с разными стилями оформления (жирный, курсив, код)",
        output_format=OutputFormat.RAW
    )
    print("\nRaw response (mixed content):")
    print(response.text)

if __name__ == "__main__":
    asyncio.run(main()) 