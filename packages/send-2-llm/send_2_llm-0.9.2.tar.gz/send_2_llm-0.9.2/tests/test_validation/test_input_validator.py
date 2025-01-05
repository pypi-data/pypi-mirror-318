"""Tests for InputValidator."""

import pytest
from send_2_llm.validation.input_validator import InputValidator
from send_2_llm.types import ProviderType

def test_validate_prompt_empty():
    """Test validation of empty prompt."""
    validator = InputValidator()
    assert not validator.validate_prompt("")
    assert not validator.validate_prompt(None)

def test_validate_prompt_too_long():
    """Test validation of too long prompt."""
    validator = InputValidator()
    long_prompt = "x" * (validator._max_prompt_length + 1)
    assert not validator.validate_prompt(long_prompt)

def test_validate_prompt_valid():
    """Test validation of valid prompt."""
    validator = InputValidator()
    assert validator.validate_prompt("Generate a haiku")

def test_sanitize_prompt():
    """Test prompt sanitization."""
    validator = InputValidator()
    prompt = "Hello\x00World\n  Multiple   Spaces  "
    sanitized = validator.sanitize_prompt(prompt)
    assert sanitized == "Hello World Multiple Spaces"

def test_validate_parameters_missing_model():
    """Test validation with missing model."""
    validator = InputValidator()
    assert not validator.validate_parameters(ProviderType.OPENAI, "")

def test_validate_parameters_invalid_temperature():
    """Test validation with invalid temperature."""
    validator = InputValidator()
    assert not validator.validate_parameters(
        ProviderType.OPENAI,
        "gpt-3.5-turbo",
        temperature=2.5
    )

def test_validate_parameters_invalid_top_p():
    """Test validation with invalid top_p."""
    validator = InputValidator()
    assert not validator.validate_parameters(
        ProviderType.OPENAI,
        "gpt-3.5-turbo",
        top_p=1.5
    )

def test_validate_parameters_invalid_max_tokens():
    """Test validation with invalid max_tokens."""
    validator = InputValidator()
    assert not validator.validate_parameters(
        ProviderType.OPENAI,
        "gpt-3.5-turbo",
        max_tokens=0
    )

def test_validate_parameters_valid():
    """Test validation with valid parameters."""
    validator = InputValidator()
    assert validator.validate_parameters(
        ProviderType.OPENAI,
        "gpt-3.5-turbo",
        temperature=0.7,
        top_p=0.9,
        max_tokens=100
    ) 