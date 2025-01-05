"""Tests for Perplexity provider configuration integration."""

import pytest
from unittest.mock import patch, MagicMock
from send_2_llm.providers.perplexity import PerplexityProvider
from send_2_llm.constants import PriceConfig
from send_2_llm.types import ProviderType


@pytest.fixture
def mock_config_manager():
    """Mock ConfigManager for testing."""
    mock = MagicMock()
    mock.get_model_price.return_value = PriceConfig(
        prompt=0.5,
        completion=1.0
    )
    mock.get_model_features.return_value = {
        "streaming": True,
        "function_calling": False
    }
    mock.get_system_prompt.return_value = "You are a helpful assistant."
    return mock


def test_provider_initialization_with_config(monkeypatch, mock_config_manager):
    """Test provider initialization with configuration."""
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    
    with patch("send_2_llm.providers.perplexity.config_manager", mock_config_manager):
        provider = PerplexityProvider()
        
        # Check that config was loaded
        assert provider.features == {
            "streaming": True,
            "function_calling": False
        }
        assert provider.price_config.prompt == 0.5
        assert provider.price_config.completion == 1.0


def test_provider_initialization_with_invalid_model(monkeypatch, mock_config_manager):
    """Test provider initialization with invalid model."""
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    
    # Configure mock to raise ValueError for invalid model
    mock_config_manager.get_model_features.side_effect = ValueError("Invalid model")
    mock_config_manager.get_model_price.side_effect = ValueError("Invalid model")
    
    with patch("send_2_llm.providers.perplexity.config_manager", mock_config_manager):
        provider = PerplexityProvider()
        
        # Check that default values were used
        assert provider.features == {}
        assert provider.price_config is None


@pytest.mark.asyncio
async def test_cost_calculation_with_config(monkeypatch, mock_config_manager, async_client_session):
    """Test cost calculation using configuration."""
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    
    # Mock API response
    mock_response = {
        "choices": [{
            "message": {"content": "Test response"}
        }],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }
    
    with patch("send_2_llm.providers.perplexity.config_manager", mock_config_manager):
        provider = PerplexityProvider()
        
        # Mock aiohttp.ClientSession
        mock_session = async_client_session(mock_response)
        with patch("aiohttp.ClientSession", return_value=mock_session):
            response = await provider.generate(request=MagicMock(prompt="Test"))
            
            # Check cost calculation
            # prompt: 10 tokens * $0.5/MTok = $0.000005
            # completion: 20 tokens * $1.0/MTok = $0.00002
            # total: $0.000025
            assert response.metadata.usage.cost == pytest.approx(0.000025)


@pytest.mark.asyncio
async def test_system_prompt_integration(monkeypatch, mock_config_manager, async_client_session):
    """Test system prompt integration."""
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test_key")
    
    # Mock API response
    mock_response = {
        "choices": [{
            "message": {"content": "Test response"}
        }],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }
    
    with patch("send_2_llm.providers.perplexity.config_manager", mock_config_manager):
        provider = PerplexityProvider()
        
        # Mock aiohttp.ClientSession
        mock_session = async_client_session(mock_response)
        with patch("aiohttp.ClientSession", return_value=mock_session):
            # Create request with system prompt type
            request = MagicMock(
                prompt="Test",
                system_prompt_type="general"
            )
            
            await provider.generate(request=request)
            
            # Check that system prompt was requested
            mock_config_manager.get_system_prompt.assert_called_once_with("general") 