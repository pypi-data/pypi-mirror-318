"""Tests for response formatter."""

import json
from datetime import datetime

import pytest

from send_2_llm.types import (
    LLMResponse,
    LLMMetadata,
    OutputFormat,
    ProviderType,
    TokenUsage,
)
from send_2_llm.response_formatter import ResponseFormatter


@pytest.fixture
def sample_response():
    """Create sample LLM response for testing."""
    return LLMResponse(
        text="Hello  world\n\n*bold*",
        metadata=LLMMetadata(
            provider=ProviderType.OPENAI,
            model="test-model",
            created_at=datetime(2024, 4, 7),
            usage=TokenUsage(
                prompt_tokens=10,
                completion_tokens=5,
                total_tokens=15,
                cost=0.001
            )
        )
    )


def test_raw_format(sample_response):
    """Test RAW format returns unmodified response."""
    formatted = ResponseFormatter.format_response(
        sample_response,
        OutputFormat.RAW
    )
    assert formatted.text == sample_response.text
    assert formatted.metadata == sample_response.metadata


def test_text_format(sample_response):
    """Test TEXT format normalizes whitespace."""
    formatted = ResponseFormatter.format_response(
        sample_response,
        OutputFormat.TEXT
    )
    assert formatted.text == "Hello world\n\n*bold*"
    assert formatted.metadata == sample_response.metadata


def test_json_format(sample_response):
    """Test JSON format includes metadata."""
    formatted = ResponseFormatter.format_response(
        sample_response,
        OutputFormat.json
    )
    
    # Parse JSON response
    data = json.loads(formatted.text)
    
    # Check structure
    assert "text" in data
    assert "metadata" in data
    
    # Check content
    assert data["text"] == "Hello world\n\n*bold*"
    assert data["metadata"]["provider"] == "openai"
    assert data["metadata"]["model"] == "test-model"


def test_telegram_format(sample_response):
    """Test TELEGRAM_MARKDOWN format escapes special chars."""
    formatted = ResponseFormatter.format_response(
        sample_response,
        OutputFormat.TELEGRAM_MARKDOWN
    )
    assert r"\*bold\*" in formatted.text
    assert formatted.metadata == sample_response.metadata


def test_no_format(sample_response):
    """Test None format returns unmodified response."""
    formatted = ResponseFormatter.format_response(sample_response, None)
    assert formatted == sample_response 