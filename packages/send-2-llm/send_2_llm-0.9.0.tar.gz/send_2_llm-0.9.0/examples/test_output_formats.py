"""
Example of using different output formats with send_2_llm.
Shows how to use RAW, TEXT, JSON and TELEGRAM_MARKDOWN formats.
"""

import asyncio
from send_2_llm import send_2_llm
from send_2_llm.types import OutputFormat, ProviderType

async def test_raw_output():
    """Test raw output format from Perplexity API"""
    question = "Какая погода сегодня в городе Набережные Челны?"
    
    # Get raw response
    response = await send_2_llm(
        question,
        provider=ProviderType.PERPLEXITY,
        output_format=OutputFormat.RAW
    )
    
    print("\n=== RAW OUTPUT ===")
    print(response)
    print("\n=== END RAW OUTPUT ===")

async def test_text_output():
    """Test text output format"""
    question = "Какая погода сегодня в городе Набережные Челны?"
    
    # Get text response
    response = await send_2_llm(
        question,
        provider=ProviderType.PERPLEXITY,
        output_format=OutputFormat.TEXT
    )
    
    print("\n=== TEXT OUTPUT ===")
    print(response)
    print("\n=== END TEXT OUTPUT ===")

async def main():
    """Run all format tests"""
    await test_raw_output()
    await test_text_output()

if __name__ == "__main__":
    asyncio.run(main()) 