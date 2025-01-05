"""Tests for LLMManager."""

import pytest
from unittest.mock import Mock, AsyncMock, patch
from send_2_llm.manager import LLMManager
from send_2_llm.types import (
    ProviderType,
    LLMResponse,
    LLMMetadata,
    TokenUsage
)

@pytest.fixture
def manager():
    """Create LLMManager instance with mocked components."""
    with patch('send_2_llm.manager.SecurityManager') as security_mock, \
         patch('send_2_llm.manager.InputValidator') as validator_mock, \
         patch('send_2_llm.manager.CircuitBreaker') as circuit_mock, \
         patch('send_2_llm.manager.RateLimiter') as limiter_mock, \
         patch('send_2_llm.manager.Monitoring') as monitoring_mock, \
         patch('send_2_llm.manager.ProviderFactory') as factory_mock:
        
        manager = LLMManager()
        
        # Configure mocks
        manager.security.validate_access = Mock(return_value=True)
        manager.security.validate_api_key = Mock(return_value=True)
        
        manager.validator.validate_prompt = Mock()
        manager.validator.validate_parameters = Mock()
        
        manager.circuit_breaker.is_available = Mock(return_value=True)
        manager.circuit_breaker.record_success = Mock()
        manager.circuit_breaker.record_error = Mock()
        
        manager.rate_limiter.acquire = AsyncMock()
        
        manager.monitoring.track_request = Mock()
        manager.monitoring.track_request.return_value.__enter__ = Mock()
        manager.monitoring.track_request.return_value.__exit__ = Mock()
        
        mock_provider = AsyncMock()
        mock_provider._generate = AsyncMock(return_value=LLMResponse(
            text="Test response",
            metadata=LLMMetadata(
                provider=ProviderType.OPENAI,
                model="test-model",
                usage=TokenUsage(
                    prompt_tokens=10,
                    completion_tokens=20,
                    total_tokens=30,
                    cost=0.001
                )
            )
        ))
        mock_provider.list_models = AsyncMock(return_value=["model-1", "model-2"])
        
        manager.provider_factory.create_provider = Mock(return_value=mock_provider)
        
        return manager

@pytest.mark.asyncio
async def test_generate_success(manager):
    """Test successful generation."""
    response = await manager.generate(
        prompt="Test prompt",
        provider=ProviderType.OPENAI,
        model="test-model"
    )
    
    assert response.text == "Test response"
    assert response.metadata.provider == ProviderType.OPENAI
    assert response.metadata.model == "test-model"
    
    # Verify all checks were called
    manager.security.validate_access.assert_called_once()
    manager.validator.validate_prompt.assert_called_once()
    manager.validator.validate_parameters.assert_called_once()
    manager.circuit_breaker.is_available.assert_called_once()
    manager.rate_limiter.acquire.assert_called_once()
    manager.circuit_breaker.record_success.assert_called_once()
    
@pytest.mark.asyncio
async def test_generate_security_error(manager):
    """Test generation with security error."""
    manager.security.validate_access.return_value = False
    
    with pytest.raises(SecurityError):
        await manager.generate(
            prompt="Test prompt",
            provider=ProviderType.OPENAI,
            model="test-model"
        )
        
@pytest.mark.asyncio
async def test_generate_circuit_breaker_error(manager):
    """Test generation with circuit breaker error."""
    manager.circuit_breaker.is_available.return_value = False
    
    with pytest.raises(ProviderError):
        await manager.generate(
            prompt="Test prompt",
            provider=ProviderType.OPENAI,
            model="test-model"
        )
        
@pytest.mark.asyncio
async def test_generate_provider_error(manager):
    """Test generation with provider error."""
    mock_provider = AsyncMock()
    mock_provider._generate = AsyncMock(side_effect=Exception("Provider error"))
    manager.provider_factory.create_provider.return_value = mock_provider
    
    with pytest.raises(ProviderError):
        await manager.generate(
            prompt="Test prompt",
            provider=ProviderType.OPENAI,
            model="test-model"
        )
    
    manager.circuit_breaker.record_error.assert_called_once()
    
@pytest.mark.asyncio
async def test_list_models_success(manager):
    """Test successful model listing."""
    models = await manager.list_models(ProviderType.OPENAI)
    
    assert models == ["model-1", "model-2"]
    manager.security.validate_api_key.assert_called_once()
    
@pytest.mark.asyncio
async def test_list_models_security_error(manager):
    """Test model listing with security error."""
    manager.security.validate_api_key.return_value = False
    
    with pytest.raises(SecurityError):
        await manager.list_models(ProviderType.OPENAI) 