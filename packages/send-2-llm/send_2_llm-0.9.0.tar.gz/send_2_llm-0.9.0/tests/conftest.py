"""Test configuration and fixtures."""

import os
import pytest
from typing import Generator
from unittest.mock import patch

from send_2_llm.types import ProviderType


@pytest.fixture
def mock_env() -> Generator[None, None, None]:
    """Mock environment variables for testing."""
    with patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test-key',
        'OPENAI_MODEL': 'gpt-3.5-turbo',
        'OPENAI_TEMPERATURE': '0.7',
        'OPENAI_MAX_TOKENS': '1000',
        'TOGETHER_API_KEY': 'test-key',
        'TOGETHER_MODEL': 'meta-llama/Llama-Vision-Free',
        'TOGETHER_TEMPERATURE': '0.7',
        'TOGETHER_MAX_TOKENS': '1000'
    }):
        yield


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI API response."""
    return {
        "choices": [
            {
                "message": {"content": "Test response"},
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }


@pytest.fixture
def mock_together_response():
    """Mock Together AI API response."""
    return {
        "choices": [
            {
                "message": {"content": "Test response"},
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }


@pytest.fixture
def provider_types():
    """List of all provider types for parametrized tests."""
    return [
        ProviderType.OPENAI,
        ProviderType.TOGETHER,
        ProviderType.ANTHROPIC,
        ProviderType.PERPLEXITY,
        ProviderType.DEEPSEEK,
    ] 