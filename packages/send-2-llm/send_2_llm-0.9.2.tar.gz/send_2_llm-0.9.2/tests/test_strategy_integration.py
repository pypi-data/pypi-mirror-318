"""Integration tests for strategy switching."""

import os
import pytest
from unittest.mock import patch
from send_2_llm import send_2_llm
from send_2_llm.types import ProviderType, StrategyType
from send_2_llm.providers.factory import register_provider
from .mocks.providers import MockTogetherProvider, MockOpenAIProvider

TEST_PROMPT = "Напиши короткое стихотворение про кота"

@pytest.fixture
def env_setup():
    """Сохраняем оригинальные переменные окружения."""
    original_env = {
        "LLM_STRATEGY": os.getenv("LLM_STRATEGY"),
        "DEFAULT_PROVIDER": os.getenv("DEFAULT_PROVIDER"),
        "TOGETHER_MODEL": os.getenv("TOGETHER_MODEL"),
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL"),
        "LLM_PROVIDERS": os.getenv("LLM_PROVIDERS")
    }
    yield
    # Восстанавливаем оригинальные значения
    for key, value in original_env.items():
        if value is not None:
            os.environ[key] = value
        elif key in os.environ:
            del os.environ[key]

@pytest.fixture
def mock_providers():
    """Подменяем реальных провайдеров на моки."""
    # Регистрируем моки провайдеров
    register_provider(ProviderType.TOGETHER, MockTogetherProvider)
    register_provider(ProviderType.OPENAI, MockOpenAIProvider)
    yield
    # Восстанавливаем оригинальные провайдеры после теста
    from send_2_llm.providers.together import TogetherProvider
    from send_2_llm.providers.openai import OpenAIProvider
    register_provider(ProviderType.TOGETHER, TogetherProvider)
    register_provider(ProviderType.OPENAI, OpenAIProvider)

@pytest.mark.asyncio
async def test_together_single_strategy(env_setup, mock_providers):
    """Тест стратегии Together AI через send_2_llm."""
    # Настраиваем окружение для Together
    os.environ["LLM_STRATEGY"] = "single"
    os.environ["DEFAULT_PROVIDER"] = "together"
    os.environ["TOGETHER_MODEL"] = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    
    # Используем send_2_llm без параметров - берет настройки из окружения
    response = await send_2_llm(TEST_PROMPT)
    
    # Проверяем результат
    assert response.metadata.provider == ProviderType.TOGETHER
    assert response.metadata.model == "mistralai/Mixtral-8x7B-Instruct-v0.1"
    assert response.metadata.strategy == StrategyType.SINGLE
    assert isinstance(response.text, str)
    assert len(response.text) > 0
    
    print("\nTogether AI Response (from env):")
    print(f"Text: {response.text}")
    print(f"Model: {response.metadata.model}")
    
    # Тест с явным указанием параметров
    response = await send_2_llm(
        TEST_PROMPT,
        strategy_type=StrategyType.SINGLE,
        provider_type=ProviderType.TOGETHER,
        model="mistralai/Mixtral-8x7B-Instruct-v0.1"
    )
    
    assert response.metadata.provider == ProviderType.TOGETHER
    print("\nTogether AI Response (explicit params):")
    print(f"Text: {response.text}")
    print(f"Model: {response.metadata.model}")

@pytest.mark.asyncio
async def test_fallback_strategy(env_setup, mock_providers):
    """Тест fallback стратегии через send_2_llm."""
    # Настраиваем окружение для fallback
    os.environ["LLM_STRATEGY"] = "fallback"
    os.environ["LLM_PROVIDERS"] = "together,openai"
    os.environ["TOGETHER_MODEL"] = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    os.environ["OPENAI_MODEL"] = "gpt-4o-mini-2024-07-18"
    
    # Используем send_2_llm с настройками из окружения
    response = await send_2_llm(TEST_PROMPT)
    
    # Проверяем результат
    assert response.metadata.provider in [ProviderType.TOGETHER, ProviderType.OPENAI]
    assert response.metadata.strategy == StrategyType.FALLBACK
    assert isinstance(response.text, str)
    assert len(response.text) > 0
    
    print("\nFallback Strategy Response (from env):")
    print(f"Text: {response.text}")
    print(f"Provider: {response.metadata.provider}")
    print(f"Model: {response.metadata.model}")

@pytest.mark.asyncio
async def test_strategy_switch_in_request(mock_providers):
    """Тест переключения стратегий между запросами."""
    # Первый запрос - Together single strategy
    response1 = await send_2_llm(
        TEST_PROMPT,
        strategy_type=StrategyType.SINGLE,
        provider_type=ProviderType.TOGETHER,
        model="mistralai/Mixtral-8x7B-Instruct-v0.1"
    )
    
    assert response1.metadata.provider == ProviderType.TOGETHER
    print("\nFirst Response (Together):")
    print(f"Text: {response1.text}")
    print(f"Model: {response1.metadata.model}")
    
    # Второй запрос - Fallback strategy
    response2 = await send_2_llm(
        TEST_PROMPT,
        strategy_type=StrategyType.FALLBACK,
        providers=[ProviderType.TOGETHER, ProviderType.OPENAI],
        models=["mistralai/Mixtral-8x7B-Instruct-v0.1", "gpt-4o-mini-2024-07-18"]
    )
    
    assert response2.metadata.strategy == StrategyType.FALLBACK
    print("\nSecond Response (Fallback):")
    print(f"Text: {response2.text}")
    print(f"Provider: {response2.metadata.provider}")
    print(f"Model: {response2.metadata.model}")

@pytest.mark.asyncio
async def test_error_handling(mock_providers):
    """Тест обработки ошибок."""
    # Тест с неверной стратегией
    with pytest.raises(ValueError, match="At least one provider must be specified for non-single strategy"):
        await send_2_llm(
            TEST_PROMPT,
            strategy_type="invalid_strategy"
        )
    
    # Тест fallback без провайдеров
    with pytest.raises(ValueError, match="At least one provider must be specified"):
        await send_2_llm(
            TEST_PROMPT,
            strategy_type=StrategyType.FALLBACK,
            providers=[]
        )

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"]) 