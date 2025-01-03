"""Tests for configuration management."""

import os
import pytest
from unittest.mock import patch

from send_2_llm.config import (
    load_config,
    ConfigurationError,
    _get_provider_from_env,
    _get_providers_list_from_env,
    _get_strategy_from_env
)
from send_2_llm.types import ProviderType, StrategyType

def test_load_config_basic():
    """Test basic configuration loading."""
    with patch.dict(os.environ, {
        "DEFAULT_PROVIDER": "openai",
        "LLM_STRATEGY": "single",
        "OPENAI_API_KEY": "test-key"
    }, clear=True):
        config = load_config(load_env=False)
        assert config["default_provider"] == ProviderType.OPENAI
        assert config["strategy"] == StrategyType.SINGLE

def test_provider_validation():
    """Test provider validation."""
    # Valid provider
    with patch.dict(os.environ, {"DEFAULT_PROVIDER": "openai"}, clear=True):
        provider = _get_provider_from_env()
        assert provider == ProviderType.OPENAI
    
    # Invalid provider
    with patch.dict(os.environ, {"DEFAULT_PROVIDER": "invalid"}, clear=True):
        with pytest.raises(ConfigurationError, match="Invalid provider type"):
            _get_provider_from_env()

def test_strategy_validation():
    """Test strategy validation."""
    # Valid strategy
    with patch.dict(os.environ, {"LLM_STRATEGY": "single"}, clear=True):
        strategy = _get_strategy_from_env()
        assert strategy == StrategyType.SINGLE
    
    # Invalid strategy
    with patch.dict(os.environ, {"LLM_STRATEGY": "invalid"}, clear=True):
        with pytest.raises(ConfigurationError, match="Invalid strategy type"):
            _get_strategy_from_env()

def test_providers_list():
    """Test providers list parsing."""
    # Valid list
    with patch.dict(os.environ, {"LLM_PROVIDERS": "openai,anthropic"}, clear=True):
        providers = _get_providers_list_from_env()
        assert providers == [ProviderType.OPENAI, ProviderType.ANTHROPIC]
    
    # Empty list
    with patch.dict(os.environ, {"LLM_PROVIDERS": ""}, clear=True):
        providers = _get_providers_list_from_env()
        assert providers == []
    
    # Invalid provider in list
    with patch.dict(os.environ, {"LLM_PROVIDERS": "openai,invalid"}, clear=True):
        with pytest.raises(ConfigurationError, match="Invalid provider type"):
            _get_providers_list_from_env()

def test_default_values():
    """Test default configuration values."""
    with patch.dict(os.environ, {}, clear=True):
        config = load_config(load_env=False)
        assert config["default_provider"] is None
        assert config["strategy"] == StrategyType.SINGLE
        assert config["max_input_tokens"] == 3072
        assert config["temperature"] == 0.7
        assert config["top_p"] == 0.95 