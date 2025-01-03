import os
import pytest
from unittest.mock import patch
from send_2_llm import LLMClient
from send_2_llm.types import ProviderType, StrategyType, LLMResponse, LLMMetadata
from send_2_llm.config import reload_config, load_config_with_cache
from send_2_llm.strategies.single import SingleProviderStrategy
from send_2_llm.strategies.fallback import FallbackStrategy

@pytest.fixture
def mock_env():
    """Фикстура для управления переменными окружения"""
    # Сохраняем оригинальные значения
    original_env = dict(os.environ)
    
    # Очищаем окружение
    os.environ.clear()
    
    # Очищаем кэш конфигурации
    load_config_with_cache.cache_clear()
    
    yield
    
    # Восстанавливаем оригинальное окружение
    os.environ.clear()
    os.environ.update(original_env)
    
    # Очищаем кэш конфигурации
    load_config_with_cache.cache_clear()

@pytest.mark.asyncio
async def test_strategy_switch_via_env():
    """Test switching strategies via environment variables."""
    # Test with single provider
    with patch.dict(os.environ, {
        "STRATEGY": "single",
        "DEFAULT_PROVIDER": "openai",
        "OPENAI_API_KEY": "test-key"
    }):
        client = LLMClient()
        assert isinstance(client.strategy, SingleProviderStrategy)
        assert client.provider_type == ProviderType.OPENAI
        
    # Test with fallback strategy
    with patch.dict(os.environ, {
        "STRATEGY": "fallback",
        "PROVIDER_LIST": "openai,anthropic",
        "OPENAI_API_KEY": "test-key",
        "ANTHROPIC_API_KEY": "test-key"
    }):
        client = LLMClient()
        assert isinstance(client.strategy, FallbackStrategy)
        assert client.providers == [ProviderType.OPENAI, ProviderType.ANTHROPIC]

@pytest.mark.asyncio
async def test_strategy_error_handling():
    """Test error handling in strategy switching."""
    # Test invalid strategy type
    with patch.dict(os.environ, {"STRATEGY": "invalid"}):
        with pytest.raises(StrategyError, match="Unknown strategy type"):
            LLMClient()
            
    # Test missing provider for single strategy
    with patch.dict(os.environ, {
        "STRATEGY": "single",
        "DEFAULT_PROVIDER": ""
    }):
        with pytest.raises(StrategyError, match="No provider specified"):
            LLMClient()
            
    # Test missing providers for fallback strategy
    with patch.dict(os.environ, {
        "STRATEGY": "fallback",
        "PROVIDER_LIST": ""
    }):
        with pytest.raises(StrategyError, match="No providers specified"):
            LLMClient() 