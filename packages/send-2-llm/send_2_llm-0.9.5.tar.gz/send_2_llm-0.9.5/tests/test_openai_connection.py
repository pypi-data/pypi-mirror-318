"""
!!! WARNING - STABLE CONNECTION TESTS !!!
These are stable connection tests for OpenAI API.
DO NOT MODIFY without explicit permission.
Commit: b25d24a
Tag: stable_openai_v1

Test suite includes:
- Basic API connection
- Error handling for invalid API key

To run these tests:
PYTHONPATH=src pytest tests/test_openai_connection.py -v

Required dependencies:
- pytest>=7.0.0
- pytest-asyncio>=0.20.0
- openai>=1.12.0
- python-dotenv>=1.0.0
!!! WARNING !!!
"""

import pytest
from openai import OpenAI
import os
from dotenv import load_dotenv

# !!! STABLE TESTS - DO NOT MODIFY !!!
@pytest.fixture(scope="module")
def openai_client():
    """Фикстура для создания клиента OpenAI"""
    load_dotenv()
    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def test_openai_connection(openai_client):
    """Тест базового подключения к OpenAI API"""
    response = openai_client.chat.completions.create(
        model=os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo'),
        messages=[
            {"role": "user", "content": "Say 'test connection successful'"}
        ],
        temperature=float(os.getenv('OPENAI_TEMPERATURE', 0.7)),
        max_tokens=int(os.getenv('OPENAI_MAX_TOKENS', 1000))
    )
    
    assert response.choices[0].message.content is not None
    print(f"\nOpenAI ответ: {response.choices[0].message.content}")

@pytest.mark.asyncio
async def test_openai_error_handling(openai_client):
    """Тест обработки ошибок при неверном API ключе"""
    with pytest.raises(Exception):
        invalid_client = OpenAI(api_key="invalid_key")
        await invalid_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "test"}]
        ) 