"""Tests for base provider functionality."""

import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from typing import Optional

from send_2_llm.types import (
    LLMRequest,
    LLMResponse,
    LLMMetadata,
    ProviderType,
    TokenUsage
)
from send_2_llm.providers.base import BaseLLMProvider

class TestProvider(BaseLLMProvider):
    """Test provider implementation."""
    
    def _get_provider_type(self) -> ProviderType:
        return ProviderType.OPENAI
    
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        return LLMResponse(
            text="Test response",
            metadata=LLMMetadata(
                provider=ProviderType.OPENAI,
                model="test-model",
                usage=TokenUsage(
                    prompt_tokens=10,
                    completion_tokens=20,
                    total_tokens=30,
                    cost=0.05
                )
            )
        )

@pytest.fixture
def provider():
    """Test provider instance."""
    return TestProvider()

@pytest.fixture
def mock_loggers():
    """Mock logging components."""
    with patch("send_2_llm.providers.base.api_logger") as mock_api_logger, \
         patch("send_2_llm.providers.base.metrics_logger") as mock_metrics_logger:
        yield {
            "api": mock_api_logger,
            "metrics": mock_metrics_logger
        }

@pytest.mark.asyncio
async def test_generate_success(provider, mock_loggers):
    """Test successful generation with logging."""
    request = LLMRequest(prompt="Test prompt")
    
    # Generate response
    response = await provider.generate(request)
    
    # Check response
    assert response.text == "Test response"
    assert response.metadata.provider == ProviderType.OPENAI
    assert response.metadata.model == "test-model"
    assert response.metadata.usage.prompt_tokens == 10
    assert response.metadata.usage.completion_tokens == 20
    assert response.metadata.usage.total_tokens == 30
    assert response.metadata.usage.cost == 0.05
    
    # Check API request logging
    mock_loggers["api"].log_request.assert_called_once()
    request_args = mock_loggers["api"].log_request.call_args[1]
    assert request_args["provider"] == "openai"
    assert request_args["endpoint"] == "/generate"
    assert request_args["method"] == "POST"
    assert request_args["payload"]["prompt"] == "Test prompt"
    
    # Check API response logging
    mock_loggers["api"].log_response.assert_called_once()
    response_args = mock_loggers["api"].log_response.call_args[1]
    assert response_args["provider"] == "openai"
    assert response_args["endpoint"] == "/generate"
    assert response_args["method"] == "POST"
    assert response_args["status_code"] == 200
    assert isinstance(response_args["response_time"], float)
    assert response_args["response_data"]["text"] == "Test response"
    
    # Check metrics logging
    mock_loggers["metrics"].log_token_usage.assert_called_once()
    metrics_args = mock_loggers["metrics"].log_token_usage.call_args[1]
    assert metrics_args["provider"] == "openai"
    assert metrics_args["prompt_tokens"] == 10
    assert metrics_args["completion_tokens"] == 20
    assert metrics_args["total_tokens"] == 30
    assert metrics_args["cost"] == 0.05
    assert metrics_args["model"] == "test-model"

@pytest.mark.asyncio
async def test_generate_error(provider, mock_loggers):
    """Test generation error with logging."""
    class ErrorProvider(TestProvider):
        async def _generate(self, request: LLMRequest) -> LLMResponse:
            raise ValueError("Test error")
    
    provider = ErrorProvider()
    request = LLMRequest(prompt="Test prompt")
    
    # Generate response and expect error
    with pytest.raises(ValueError, match="Test error"):
        await provider.generate(request)
    
    # Check API request logging
    mock_loggers["api"].log_request.assert_called_once()
    
    # Check API error logging
    mock_loggers["api"].log_response.assert_called_once()
    error_args = mock_loggers["api"].log_response.call_args[1]
    assert error_args["provider"] == "openai"
    assert error_args["endpoint"] == "/generate"
    assert error_args["method"] == "POST"
    assert error_args["status_code"] == 500
    assert error_args["error"] == "Test error"
    
    # Check error metrics logging
    mock_loggers["metrics"].log_error.assert_called_once()
    metrics_args = mock_loggers["metrics"].log_error.call_args[1]
    assert metrics_args["error_type"] == "ValueError"
    assert metrics_args["error_message"] == "Test error"
    assert metrics_args["provider"] == "openai"
    assert metrics_args["endpoint"] == "/generate" 