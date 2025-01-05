"""Tests for provider selection strategies."""

import pytest
from typing import Optional

from send_2_llm.types import (
    ProviderType,
    ProviderAPIError,
    ErrorDetails,
    StrategyType,
    LLMRequest
)
from send_2_llm.providers.factory import ProviderFactory, ProviderInfo
from send_2_llm.providers.base import BaseLLMProvider
from send_2_llm.strategy.base import BaseStrategy, StrategyContext
from send_2_llm.strategy.single import SingleProviderStrategy
from send_2_llm.strategy.fallback import FallbackStrategy

# Test provider for registration
class TestProvider(BaseLLMProvider):
    """Test provider implementation."""
    
    def __init__(self, provider_type: ProviderType, **kwargs):
        super().__init__(provider_type=provider_type)
        
    async def _generate(self, request):
        return None

@pytest.fixture
def factory():
    """Create provider factory with test providers."""
    factory = ProviderFactory()
    
    # Clear existing providers
    factory._providers.clear()
    
    # Register test providers
    factory.register_provider(
        ProviderType.OPENAI,
        TestProvider,
        priority=100,
        description="Test OpenAI provider"
    )
    factory.register_provider(
        ProviderType.ANTHROPIC,
        TestProvider,
        priority=90,
        is_fallback=True,
        description="Test Anthropic provider"
    )
    factory.register_provider(
        ProviderType.GEMINI,
        TestProvider,
        priority=80,
        is_fallback=True,
        description="Test Gemini provider"
    )
    
    return factory

@pytest.fixture
def context(factory):
    """Create strategy context."""
    return StrategyContext(
        request=LLMRequest(prompt="test"),
        factory=factory
    )

class TestSingleProviderStrategy:
    """Tests for SingleProviderStrategy."""
    
    @pytest.mark.asyncio
    async def test_select_provider_from_request(self, context):
        """Test selecting provider specified in request."""
        strategy = SingleProviderStrategy()
        context.request.provider = ProviderType.OPENAI
        context.request.model = "gpt-4"
        
        provider_type, model = await strategy.select_provider(context)
        
        assert provider_type == ProviderType.OPENAI
        assert model == "gpt-4"
    
    @pytest.mark.asyncio
    async def test_select_provider_not_found(self, context):
        """Test error when provider not found."""
        strategy = SingleProviderStrategy()
        context.request.provider = ProviderType("invalid")
        
        with pytest.raises(ProviderAPIError) as exc:
            await strategy.select_provider(context)
        
        assert "not found" in str(exc.value)
        assert exc.value.error_details.error_type == "ProviderNotFound"
    
    @pytest.mark.asyncio
    async def test_select_highest_priority(self, context):
        """Test selecting highest priority provider when none specified."""
        strategy = SingleProviderStrategy()
        
        provider_type, model = await strategy.select_provider(context)
        
        assert provider_type == ProviderType.OPENAI
        assert model is None
    
    @pytest.mark.asyncio
    async def test_handle_error(self, context):
        """Test error handling (should just re-raise)."""
        strategy = SingleProviderStrategy()
        error = ProviderAPIError("Test error")
        
        with pytest.raises(ProviderAPIError) as exc:
            await strategy.handle_error(error, context)
        
        assert exc.value == error

class TestFallbackStrategy:
    """Tests for FallbackStrategy."""
    
    @pytest.mark.asyncio
    async def test_select_provider_from_request(self, context):
        """Test selecting provider specified in request."""
        strategy = FallbackStrategy()
        context.request.provider = ProviderType.OPENAI
        context.request.model = "gpt-4"
        
        provider_type, model = await strategy.select_provider(context)
        
        assert provider_type == ProviderType.OPENAI
        assert model == "gpt-4"
    
    @pytest.mark.asyncio
    async def test_select_fallback_after_error(self, context):
        """Test selecting fallback provider after error."""
        strategy = FallbackStrategy()
        context.request.provider = ProviderType.OPENAI
        
        # Add error for OpenAI
        error = ProviderAPIError(
            "Test error",
            error_details=ErrorDetails(
                error_type="TestError",
                message="Test error",
                retryable=True
            )
        )
        context.error_history[ProviderType.OPENAI] = [error]
        
        provider_type, model = await strategy.select_provider(context)
        
        assert provider_type == ProviderType.ANTHROPIC
        assert model is None
    
    @pytest.mark.asyncio
    async def test_handle_error_retry(self, context):
        """Test error handling with retry."""
        strategy = FallbackStrategy()
        context.request.provider = ProviderType.OPENAI
        
        error = ProviderAPIError(
            "Test error",
            error_details=ErrorDetails(
                error_type="TestError",
                message="Test error",
                retryable=True
            )
        )
        
        provider_type, model = await strategy.handle_error(error, context)
        
        assert provider_type == ProviderType.ANTHROPIC
        assert model is None
        assert context.attempt_count == 1
    
    @pytest.mark.asyncio
    async def test_handle_error_no_retry(self, context):
        """Test error handling without retry."""
        strategy = FallbackStrategy()
        context.request.provider = ProviderType.OPENAI
        
        error = ProviderAPIError(
            "Test error",
            error_details=ErrorDetails(
                error_type="TestError",
                message="Test error",
                retryable=False
            )
        )
        
        with pytest.raises(ProviderAPIError) as exc:
            await strategy.handle_error(error, context)
        
        assert exc.value == error
    
    @pytest.mark.asyncio
    async def test_handle_error_max_attempts(self, context):
        """Test error handling with max attempts reached."""
        strategy = FallbackStrategy()
        context.request.provider = ProviderType.OPENAI
        context.attempt_count = 3
        
        error = ProviderAPIError(
            "Test error",
            error_details=ErrorDetails(
                error_type="TestError",
                message="Test error",
                retryable=True
            )
        )
        
        with pytest.raises(ProviderAPIError) as exc:
            await strategy.handle_error(error, context)
        
        assert exc.value == error
    
    @pytest.mark.asyncio
    async def test_all_providers_error(self, context):
        """Test when all providers have errors."""
        strategy = FallbackStrategy()
        
        # Add errors for all providers
        error = ProviderAPIError("Test error")
        for provider_type in [ProviderType.OPENAI, ProviderType.ANTHROPIC, ProviderType.GEMINI]:
            context.error_history[provider_type] = [error]
        
        with pytest.raises(ProviderAPIError) as exc:
            await strategy.select_provider(context)
        
        assert "All providers have errors" in str(exc.value)
        assert exc.value.error_details.error_type == "AllProvidersError" 