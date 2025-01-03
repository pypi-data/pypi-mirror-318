"""Tests for output formatters."""

import json
import pytest
from send_2_llm.types import OutputFormat
from send_2_llm.formatters import (
    normalize_whitespace,
    escape_telegram_markdown,
    format_telegram_markdown,
    format_as_json,
    convert_to_format,
    validate_format
)

@pytest.fixture
def sample_text():
    """Sample text for testing."""
    return "This is a *bold* and _italic_ text with `code`"

@pytest.fixture
def sample_markdown():
    """Sample markdown text for testing."""
    return "```python\nprint('Hello')\n```\n*bold* text"

def test_normalize_whitespace():
    """Test whitespace normalization."""
    test_cases = [
        ("hello   world", "hello world"),
        ("hello\r\nworld", "hello world"),
        ("para1\n\npara2\n\n\npara3", "para1\n\npara2\n\npara3"),
        ("  hello \t world  \n\n  new  \t para  ", "hello world\n\nnew para")
    ]
    
    for input_text, expected in test_cases:
        assert normalize_whitespace(input_text) == expected

def test_escape_telegram_markdown():
    """Test Telegram markdown escaping."""
    test_cases = [
        ("hello_world", r"hello\_world"),
        ("*bold*", r"\*bold\*"),
        ("**bold** _italic_", r"\*\*bold\*\* \_italic\_"),
        (r"already\_escaped", r"already\_escaped")
    ]
    
    for input_text, expected in test_cases:
        assert escape_telegram_markdown(input_text) == expected

def test_format_telegram_markdown(sample_text, sample_markdown):
    """Test Telegram markdown formatting."""
    # Test basic formatting
    formatted = format_telegram_markdown(sample_text)
    assert r"\*bold\*" in formatted
    assert r"\_italic\_" in formatted
    assert "`code`" in formatted
    
    # Test code blocks
    formatted = format_telegram_markdown(sample_markdown)
    assert "```python" in formatted
    assert "print('Hello')" in formatted
    assert r"\*bold\*" in formatted

def test_format_as_json():
    """Test JSON formatting."""
    # Test basic text
    result = format_as_json("hello world")
    data = json.loads(result)
    assert data["text"] == "hello world"
    
    # Test with metadata
    metadata = {"key": "value"}
    result = format_as_json("text", metadata)
    data = json.loads(result)
    assert data["text"] == "text"
    assert data["metadata"] == metadata

def test_convert_to_format(sample_text):
    """Test format conversion."""
    # Test RAW format
    assert convert_to_format(sample_text, OutputFormat.RAW) == sample_text
    
    # Test TEXT format
    text_result = convert_to_format(sample_text, OutputFormat.TEXT)
    assert text_result == normalize_whitespace(sample_text)
    
    # Test JSON format
    json_result = convert_to_format(sample_text, OutputFormat.json)
    assert json.loads(json_result)["text"] == normalize_whitespace(sample_text)
    
    # Test TELEGRAM_MARKDOWN format
    tg_result = convert_to_format(sample_text, OutputFormat.TELEGRAM_MARKDOWN)
    assert r"\*bold\*" in tg_result
    
    # Test invalid format
    with pytest.raises(ValueError):
        convert_to_format(sample_text, "invalid")

def test_validate_format():
    """Test format validation."""
    test_cases = [
        ("any text", OutputFormat.RAW, True),
        ("clean text", OutputFormat.TEXT, True),
        ("text  with  spaces", OutputFormat.TEXT, False),
        ('{"key": "value"}', OutputFormat.json, True),
        ("invalid json", OutputFormat.json, False),
        (r"escaped\_text", OutputFormat.TELEGRAM_MARKDOWN, True),
        ("unescaped_text", OutputFormat.TELEGRAM_MARKDOWN, False),
        ("```code_block```", OutputFormat.TELEGRAM_MARKDOWN, True)
    ]
    
    for text, format_type, expected in test_cases:
        assert validate_format(text, format_type) == expected 