"""Simplified pytest configuration."""

import pytest
from dotenv import load_dotenv

def pytest_configure(config):
    """Configure pytest."""
    # Load environment variables
    load_dotenv()
    
    # Register custom markers
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "openai: mark test as OpenAI API test"
    )

@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    """Setup test environment."""
    # Set test API keys
    monkeypatch.setenv('OPENAI_API_KEY', 'test-key')
    monkeypatch.setenv('ANTHROPIC_API_KEY', 'test-key')
    
    # Set test models
    monkeypatch.setenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    monkeypatch.setenv('ANTHROPIC_MODEL', 'claude-2')
    
    # Set test parameters
    monkeypatch.setenv('MAX_RETRIES', '3')
    monkeypatch.setenv('TIMEOUT_SECONDS', '30') 