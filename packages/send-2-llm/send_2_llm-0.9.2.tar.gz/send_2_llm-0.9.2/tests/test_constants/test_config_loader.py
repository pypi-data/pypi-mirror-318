"""
Tests for configuration loader.
"""

import pytest
from send_2_llm.constants.config_loader import (
    load_model_configs,
    get_provider_config,
    get_model_config,
    get_model_price,
    get_model_limits,
    get_model_features,
    get_system_prompts,
    list_providers,
    list_models
)

def test_load_model_configs():
    """Test loading full configuration."""
    configs = load_model_configs()
    assert isinstance(configs, dict)
    assert "perplexity" in configs
    assert "openai" in configs
    assert "anthropic" in configs
    assert "system_prompts" in configs

def test_get_provider_config():
    """Test getting provider configuration."""
    config = get_provider_config("perplexity")
    assert isinstance(config, dict)
    assert "models" in config
    
    with pytest.raises(ValueError):
        get_provider_config("nonexistent_provider")

def test_get_model_config():
    """Test getting model configuration."""
    config = get_model_config("openai", "gpt-4")
    assert isinstance(config, dict)
    assert "prices" in config
    assert "limits" in config
    assert "features" in config
    
    with pytest.raises(ValueError):
        get_model_config("openai", "nonexistent_model")

def test_get_model_price():
    """Test getting model price information."""
    prices = get_model_price("anthropic", "claude-3-opus")
    assert isinstance(prices, dict)
    assert "prompt" in prices
    assert "completion" in prices
    assert isinstance(prices["prompt"], float)
    assert isinstance(prices["completion"], float)

def test_get_model_limits():
    """Test getting model token limits."""
    limits = get_model_limits("openai", "gpt-4")
    assert isinstance(limits, dict)
    assert "max_total_tokens" in limits
    assert "max_prompt_tokens" in limits
    assert "max_completion_tokens" in limits
    assert isinstance(limits["max_total_tokens"], int)

def test_get_model_features():
    """Test getting model feature support."""
    features = get_model_features("gemini", "gemini-pro-vision")
    assert isinstance(features, dict)
    assert "streaming" in features
    assert "function_calling" in features
    assert "vision" in features
    assert isinstance(features["vision"], bool)

def test_get_system_prompts():
    """Test getting system prompts."""
    prompts = get_system_prompts()
    assert isinstance(prompts, dict)
    assert "general" in prompts
    assert "code" in prompts
    assert "math" in prompts
    assert isinstance(prompts["general"], str)

def test_list_providers():
    """Test listing available providers."""
    providers = list_providers()
    assert isinstance(providers, list)
    assert "perplexity" in providers
    assert "openai" in providers
    assert "anthropic" in providers
    assert "system_prompts" not in providers

def test_list_models():
    """Test listing available models for provider."""
    models = list_models("mistral")
    assert isinstance(models, list)
    assert "mistral-large" in models
    assert "mistral-medium" in models
    assert "mistral-small" in models
    
    empty_models = list_models("nonexistent_provider")
    assert isinstance(empty_models, list)
    assert len(empty_models) == 0

def test_price_ranges():
    """Test that prices are within reasonable ranges."""
    for provider in list_providers():
        for model in list_models(provider):
            prices = get_model_price(provider, model)
            assert 0.1 <= prices["prompt"] <= 100.0, f"Unexpected prompt price for {provider}/{model}"
            assert 0.1 <= prices["completion"] <= 100.0, f"Unexpected completion price for {provider}/{model}"
            assert prices["completion"] >= prices["prompt"], f"Unexpected price ratio for {provider}/{model}"

def test_token_limit_ranges():
    """Test that token limits are within reasonable ranges."""
    for provider in list_providers():
        for model in list_models(provider):
            limits = get_model_limits(provider, model)
            assert 1000 <= limits["max_total_tokens"] <= 1000000, \
                f"Unexpected total tokens limit for {provider}/{model}"
            assert limits["max_prompt_tokens"] <= limits["max_total_tokens"]
            assert limits["max_completion_tokens"] <= limits["max_total_tokens"]
            assert limits["max_prompt_tokens"] >= limits["max_completion_tokens"]

def test_feature_consistency():
    """Test that feature flags are consistent."""
    for provider in list_providers():
        for model in list_models(provider):
            features = get_model_features(provider, model)
            assert isinstance(features["streaming"], bool)
            assert isinstance(features["function_calling"], bool)
            assert isinstance(features["vision"], bool) 