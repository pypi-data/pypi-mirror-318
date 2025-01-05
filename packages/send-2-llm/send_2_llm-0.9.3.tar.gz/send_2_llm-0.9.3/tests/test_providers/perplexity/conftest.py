"""
Common fixtures and utilities for Perplexity provider tests.
"""

import os
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from send_2_llm.providers.perplexity import PerplexityProvider
from send_2_llm.types import LLMRequest


@pytest.fixture
def mock_env():
    """Base environment configuration for tests."""
    with patch.dict('os.environ', {
        'PERPLEXITY_API_KEY': 'test_key'
    }):
        yield


@pytest.fixture
def provider(mock_env):
    """Initialized Perplexity provider instance."""
    return PerplexityProvider()


@pytest.fixture
def mock_response():
    """Base mock response from Perplexity API."""
    return {
        "choices": [{
            "message": {
                "content": "Test response"
            }
        }],
        "usage": {
            "prompt_tokens": 5,
            "completion_tokens": 10,
            "total_tokens": 15
        },
        "model": os.getenv("PERPLEXITY_MODEL"),
        "created": 1234567890,
        "finish_reason": "stop"
    }


@pytest.fixture
def async_client_session():
    """Mock aiohttp.ClientSession with configurable response."""
    def _create_session(response_data, status=200):
        # Создаем мок для ответа
        mock_response = AsyncMock()
        mock_response.status = status
        if status == 200:
            mock_response.json = AsyncMock(return_value=response_data)
        else:
            mock_response.text = AsyncMock(return_value="API Error")
        
        # Создаем мок для session.post
        mock_post = AsyncMock()
        mock_post.return_value = mock_response
        
        # Создаем мок для сессии
        mock_session = AsyncMock()
        mock_session.post = mock_post
        mock_session.__aenter__.return_value = mock_session
        mock_session.__aexit__.return_value = None
        
        return mock_session
    
    return _create_session


@pytest.fixture
def base_request():
    """Base LLMRequest instance."""
    return LLMRequest(
        prompt="Test prompt",
        max_tokens=50,
        temperature=0.7
    ) 