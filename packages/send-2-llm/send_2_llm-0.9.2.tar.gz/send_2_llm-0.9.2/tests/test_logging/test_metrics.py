"""Tests for metrics logging functionality."""

import time
import asyncio
import logging
from unittest.mock import patch, MagicMock, AsyncMock

import pytest

from send_2_llm.logging.metrics import (
    MetricsLogger,
    timing_decorator,
    metrics_logger
)

@pytest.fixture
def mock_logger():
    """Mock logger for testing."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        yield mock_logger

def test_log_duration(mock_logger):
    """Test logging operation duration."""
    logger = MetricsLogger()
    
    # Log duration
    logger.log_duration("test_operation", 1.5, custom_field="value")
    
    # Check log call
    mock_logger.info.assert_called_once()
    args, kwargs = mock_logger.info.call_args
    
    assert args[0] == "test_operation completed"
    assert kwargs["extra"]["metric_type"] == "duration"
    assert kwargs["extra"]["operation"] == "test_operation"
    assert kwargs["extra"]["duration_seconds"] == 1.5
    assert kwargs["extra"]["custom_field"] == "value"

def test_log_token_usage(mock_logger):
    """Test logging token usage metrics."""
    logger = MetricsLogger()
    
    # Log token usage
    logger.log_token_usage(
        provider="test_provider",
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30,
        cost=0.05,
        model="test_model"
    )
    
    # Check log call
    mock_logger.info.assert_called_once()
    args, kwargs = mock_logger.info.call_args
    
    assert args[0] == "Token usage for test_provider"
    assert kwargs["extra"]["metric_type"] == "token_usage"
    assert kwargs["extra"]["provider"] == "test_provider"
    assert kwargs["extra"]["prompt_tokens"] == 10
    assert kwargs["extra"]["completion_tokens"] == 20
    assert kwargs["extra"]["total_tokens"] == 30
    assert kwargs["extra"]["cost_usd"] == 0.05
    assert kwargs["extra"]["model"] == "test_model"

def test_log_error(mock_logger):
    """Test logging error metrics."""
    logger = MetricsLogger()
    
    # Log error
    logger.log_error(
        error_type="validation_error",
        error_message="Invalid input",
        details={"field": "username"}
    )
    
    # Check log call
    mock_logger.error.assert_called_once()
    args, kwargs = mock_logger.error.call_args
    
    assert args[0] == "Invalid input"
    assert kwargs["extra"]["metric_type"] == "error"
    assert kwargs["extra"]["error_type"] == "validation_error"
    assert kwargs["extra"]["details"] == {"field": "username"}

@pytest.mark.asyncio
async def test_timing_decorator_async():
    """Test timing decorator with async function."""
    # Mock metrics logger
    with patch("send_2_llm.logging.metrics.metrics_logger") as mock_metrics:
        # Define test async function
        @timing_decorator("test_async_op")
        async def test_func():
            await asyncio.sleep(0.1)
            return "result"
        
        # Call function
        result = await test_func()
        
        # Check result
        assert result == "result"
        
        # Check metrics
        mock_metrics.log_duration.assert_called_once()
        args, kwargs = mock_metrics.log_duration.call_args
        
        assert args[0] == "test_async_op"
        assert isinstance(args[1], float)
        assert args[1] >= 0.1

def test_timing_decorator_sync():
    """Test timing decorator with sync function."""
    # Mock metrics logger
    with patch("send_2_llm.logging.metrics.metrics_logger") as mock_metrics:
        # Define test sync function
        @timing_decorator("test_sync_op")
        def test_func():
            time.sleep(0.1)
            return "result"
        
        # Call function
        result = test_func()
        
        # Check result
        assert result == "result"
        
        # Check metrics
        mock_metrics.log_duration.assert_called_once()
        args, kwargs = mock_metrics.log_duration.call_args
        
        assert args[0] == "test_sync_op"
        assert isinstance(args[1], float)
        assert args[1] >= 0.1

@pytest.mark.asyncio
async def test_timing_decorator_async_error():
    """Test timing decorator with async function that raises error."""
    # Mock metrics logger
    with patch("send_2_llm.logging.metrics.metrics_logger") as mock_metrics:
        # Define test async function
        @timing_decorator("test_error_op")
        async def test_func():
            await asyncio.sleep(0.1)
            raise ValueError("Test error")
        
        # Call function and expect error
        with pytest.raises(ValueError):
            await test_func()
        
        # Check metrics
        mock_metrics.log_duration.assert_called_once()
        args, kwargs = mock_metrics.log_duration.call_args
        
        assert args[0] == "test_error_op"
        assert isinstance(args[1], float)
        assert args[1] >= 0.1
        assert kwargs["error"] == "Test error" 