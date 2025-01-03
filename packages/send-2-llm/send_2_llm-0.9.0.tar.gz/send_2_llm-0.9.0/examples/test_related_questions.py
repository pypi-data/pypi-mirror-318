"""
Test for follow-up questions generation with JSON output
"""

import asyncio
import json
from send_2_llm.providers import PerplexityProvider
from send_2_llm.types import (
    RelatedQuestionsRequest,
    RelatedQuestionsConfig,
    RelatedQuestionsGenerator
)

def print_json_response(data: dict):
    """Print JSON response in a readable format."""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def extract_question_text(text: str) -> str:
    """Extract clean question text from JSON string."""
    # Remove JSON formatting
    text = text.replace('"question": ', '')
    text = text.strip('",')
    # Remove extra quotes
    text = text.strip('"')
    return text

async def test_weather_question():
    """Test follow-up questions for weather query."""
    provider = PerplexityProvider()
    
    request = RelatedQuestionsRequest(
        original_question="Какая погода сегодня в Набережных Челнах?",
        max_questions=3
    )
    
    print("\n=== Testing Weather Question ===")
    print("Original question:", request.original_question)
    
    response = await provider.get_related_questions(request)
    print("\nResponse metadata:")
    print_json_response(response.metadata)
    
    print("\nFollow-up questions:")
    for i, q in enumerate(response.questions, 1):
        print(f"\nQuestion {i}:")
        print_json_response({
            "text": extract_question_text(q.text),
            "confidence": q.confidence,
            "source": q.source,
            "metadata": q.metadata
        })

async def test_custom_generator():
    """Test with custom generator configuration."""
    provider = PerplexityProvider()
    
    # Custom generator with specific prompt
    generator = RelatedQuestionsGenerator(
        system_prompt="""You are a follow-up question generator.
        
        Return questions in JSON format:
        {
          "follow_up_questions": [
            {
              "question": "question text?",
              "intent": "why this question is important",
              "exploration_path": "what new topics this opens"
            }
          ]
        }
        
        Make questions:
        1. Deeper dive into main topic
        2. Related context exploration
        3. Practical implications""",
        temperature=0.8
    )
    
    config = RelatedQuestionsConfig(
        enabled=True,
        generator=generator
    )
    
    request = RelatedQuestionsRequest(
        original_question="Как развивается IT индустрия в Татарстане?",
        config=config,
        max_questions=3
    )
    
    print("\n=== Testing Custom Generator ===")
    print("Original question:", request.original_question)
    
    response = await provider.get_related_questions(request)
    print("\nResponse metadata:")
    print_json_response(response.metadata)
    
    print("\nFollow-up questions:")
    for i, q in enumerate(response.questions, 1):
        print(f"\nQuestion {i}:")
        print_json_response({
            "text": extract_question_text(q.text),
            "confidence": q.confidence,
            "source": q.source,
            "metadata": q.metadata
        })

async def main():
    """Run all tests."""
    await test_weather_question()
    await test_custom_generator()

if __name__ == "__main__":
    asyncio.run(main()) 