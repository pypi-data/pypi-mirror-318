"""Tests for SecurityManager."""

import os
import pytest
from send_2_llm.security.manager import SecurityManager
from send_2_llm.types import ProviderType

@pytest.fixture(autouse=True)
def clear_env():
    """Clear environment variables before each test."""
    for provider in ProviderType:
        key_name = f"{provider.value.upper()}_API_KEY"
        if key_name in os.environ:
            del os.environ[key_name]

def test_validate_api_key_missing():
    """Test validation when API key is missing."""
    manager = SecurityManager()
    assert not manager.validate_api_key(ProviderType.OPENAI)

def test_validate_api_key_exists(monkeypatch):
    """Test validation when API key exists."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    manager = SecurityManager()
    assert manager.validate_api_key(ProviderType.OPENAI)

def test_get_api_key_missing():
    """Test getting missing API key."""
    manager = SecurityManager()
    assert manager.get_api_key(ProviderType.OPENAI) is None

def test_get_api_key_exists(monkeypatch):
    """Test getting existing API key."""
    test_key = "test-key"
    monkeypatch.setenv("OPENAI_API_KEY", test_key)
    manager = SecurityManager()
    assert manager.get_api_key(ProviderType.OPENAI) == test_key

def test_validate_access(monkeypatch):
    """Test access validation."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    manager = SecurityManager()
    assert manager.validate_access(ProviderType.OPENAI, "gpt-3.5-turbo") 