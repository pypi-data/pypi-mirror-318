"""
Tests for model pricing constants.
"""

import pytest
from send_2_llm.constants.model_pricing import (
    PERPLEXITY_MODEL_PRICES,
    PERPLEXITY_MODEL_LIMITS,
    DEFAULT_SYSTEM_PROMPTS
)

def test_perplexity_model_prices_structure():
    """Test structure and values of PERPLEXITY_MODEL_PRICES."""
    # Проверяем наличие основных моделей
    assert "llama-3.1-sonar-huge-128k-online" in PERPLEXITY_MODEL_PRICES
    assert "mixtral-8x7b-instruct" in PERPLEXITY_MODEL_PRICES
    assert "codellama-34b-instruct" in PERPLEXITY_MODEL_PRICES
    
    # Проверяем структуру цен для каждой модели
    for model, prices in PERPLEXITY_MODEL_PRICES.items():
        assert "prompt" in prices
        assert "completion" in prices
        assert isinstance(prices["prompt"], float)
        assert isinstance(prices["completion"], float)
        assert prices["prompt"] > 0
        assert prices["completion"] > 0

def test_perplexity_model_limits_structure():
    """Test structure and values of PERPLEXITY_MODEL_LIMITS."""
    # Проверяем наличие основных моделей
    assert "llama-3.1-sonar-huge-128k-online" in PERPLEXITY_MODEL_LIMITS
    assert "mixtral-8x7b-instruct" in PERPLEXITY_MODEL_LIMITS
    assert "codellama-34b-instruct" in PERPLEXITY_MODEL_LIMITS
    
    # Проверяем структуру лимитов для каждой модели
    for model, limits in PERPLEXITY_MODEL_LIMITS.items():
        assert "max_total_tokens" in limits
        assert "max_prompt_tokens" in limits
        assert "max_completion_tokens" in limits
        assert isinstance(limits["max_total_tokens"], int)
        assert isinstance(limits["max_prompt_tokens"], int)
        assert isinstance(limits["max_completion_tokens"], int)
        assert limits["max_total_tokens"] > 0
        assert limits["max_prompt_tokens"] > 0
        assert limits["max_completion_tokens"] > 0
        # Проверяем логику лимитов
        assert limits["max_total_tokens"] == limits["max_prompt_tokens"] + limits["max_completion_tokens"]

def test_model_consistency():
    """Test consistency between prices and limits."""
    # Проверяем, что все модели имеют и цены, и лимиты
    assert set(PERPLEXITY_MODEL_PRICES.keys()) == set(PERPLEXITY_MODEL_LIMITS.keys())

def test_default_system_prompts():
    """Test structure and content of DEFAULT_SYSTEM_PROMPTS."""
    # Проверяем наличие всех типов промптов
    expected_types = {"general", "code", "math", "writing", "research"}
    assert set(DEFAULT_SYSTEM_PROMPTS.keys()) == expected_types
    
    # Проверяем структуру и содержание промптов
    for prompt_type, prompt in DEFAULT_SYSTEM_PROMPTS.items():
        assert isinstance(prompt, str)
        assert len(prompt) > 0
        assert prompt.endswith((".", "!", "?"))
        assert "You are" in prompt
        assert prompt.strip() == prompt

def test_price_ranges():
    """Test that prices are within reasonable ranges."""
    for model, prices in PERPLEXITY_MODEL_PRICES.items():
        # Цены за миллион токенов должны быть в разумных пределах (0.1-10.0 USD)
        assert 0.1 <= prices["prompt"] <= 10.0, f"Unexpected prompt price for {model}"
        assert 0.1 <= prices["completion"] <= 10.0, f"Unexpected completion price for {model}"
        # Цена за completion обычно выше или равна цене за prompt
        assert prices["completion"] >= prices["prompt"], f"Unexpected price ratio for {model}"

def test_token_limit_ranges():
    """Test that token limits are within reasonable ranges."""
    for model, limits in PERPLEXITY_MODEL_LIMITS.items():
        # Проверяем, что лимиты в разумных пределах
        assert 1000 <= limits["max_total_tokens"] <= 1000000, f"Unexpected total tokens limit for {model}"
        assert limits["max_prompt_tokens"] <= limits["max_total_tokens"]
        assert limits["max_completion_tokens"] <= limits["max_total_tokens"]
        # Проверяем соотношение prompt/completion токенов
        assert limits["max_prompt_tokens"] >= limits["max_completion_tokens"]

def test_model_naming_convention():
    """Test that model names follow the expected convention."""
    for model in PERPLEXITY_MODEL_PRICES.keys():
        # Проверяем базовый формат имени модели
        assert "-" in model, f"Invalid model name format: {model}"
        assert model.islower(), f"Model name should be lowercase: {model}"
        # Проверяем специфичные префиксы
        assert any(model.startswith(prefix) for prefix in ["llama-", "mixtral-", "mistral-", "codellama-"]), \
            f"Unknown model prefix: {model}" 