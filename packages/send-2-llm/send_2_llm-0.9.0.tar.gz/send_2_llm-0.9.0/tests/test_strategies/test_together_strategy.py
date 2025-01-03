"""Tests for Together AI strategy."""

import os
import pytest
from send_2_llm.strategies.together_strategy import TogetherStrategy
from send_2_llm.types import ProviderType, StrategyType


@pytest.mark.asyncio
async def test_together_strategy():
    """Test Together AI strategy."""
    # Skip if no API key
    if not os.getenv("TOGETHER_API_KEY"):
        pytest.skip("TOGETHER_API_KEY not set")
        
    # Initialize strategy
    strategy = TogetherStrategy(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,
        max_tokens=128,
        system_prompt="You are a helpful assistant that speaks Russian.",
    )
    
    try:
        # Generate response
        response = await strategy.generate("Скажи 'Привет, мир!'")
        
        # Verify response
        assert response is not None
        assert response.text is not None
        assert len(response.text) > 0
        assert response.metadata is not None
        assert response.metadata.provider == ProviderType.TOGETHER
        assert response.metadata.model == "mistralai/Mixtral-8x7B-Instruct-v0.1"
        assert response.metadata.strategy == StrategyType.SINGLE
        assert response.metadata.usage is not None
        assert response.metadata.usage.prompt_tokens > 0
        assert response.metadata.usage.completion_tokens > 0
        assert response.metadata.usage.total_tokens > 0
        
    finally:
        # Cleanup
        await strategy.close() 