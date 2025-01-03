"""Tests for API logging functionality."""

import json
import logging
from unittest.mock import patch, MagicMock
from datetime import datetime

import pytest

from send_2_llm.logging.api import APILogger, api_logger

@pytest.fixture
def mock_logger():
    """Mock logger for testing."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        yield mock_logger

def test_sanitize_data():
    """Test data sanitization."""
    logger = APILogger()
    
    # Test data with sensitive fields
    data = {
        "api_key": "secret123",
        "user": {
            "password": "pass123",
            "name": "test",
            "token": {
                "access_token": "token123",
                "refresh_token": "refresh123"
            }
        },
        "safe_field": "visible"
    }
    
    sanitized = logger.sanitize_data(data)
    
    # Check sanitization
    assert sanitized["api_key"] == "***REDACTED***"
    assert sanitized["user"]["password"] == "***REDACTED***"
    assert sanitized["user"]["name"] == "test"
    assert sanitized["user"]["token"]["access_token"] == "***REDACTED***"
    assert sanitized["user"]["token"]["refresh_token"] == "***REDACTED***"
    assert sanitized["safe_field"] == "visible"

def test_log_request(mock_logger):
    """Test logging API request."""
    logger = APILogger()
    
    # Test request data
    payload = {
        "api_key": "secret123",
        "prompt": "test prompt",
        "parameters": {
            "temperature": 0.7
        }
    }
    
    # Log request
    logger.log_request(
        provider="test_provider",
        endpoint="/generate",
        method="POST",
        request_id="123",
        payload=payload,
        custom_field="value"
    )
    
    # Check log call
    mock_logger.info.assert_called_once()
    args, kwargs = mock_logger.info.call_args
    
    assert args[0] == "API Request: POST /generate"
    assert kwargs["extra"]["event_type"] == "api_request"
    assert kwargs["extra"]["provider"] == "test_provider"
    assert kwargs["extra"]["endpoint"] == "/generate"
    assert kwargs["extra"]["method"] == "POST"
    assert kwargs["extra"]["request_id"] == "123"
    assert kwargs["extra"]["custom_field"] == "value"
    
    # Check payload sanitization
    assert kwargs["extra"]["payload"]["api_key"] == "***REDACTED***"
    assert kwargs["extra"]["payload"]["prompt"] == "test prompt"
    assert kwargs["extra"]["payload"]["parameters"]["temperature"] == 0.7

def test_log_response_success(mock_logger):
    """Test logging successful API response."""
    logger = APILogger()
    
    # Test response data
    response_data = {
        "id": "resp123",
        "text": "Generated text",
        "token_usage": {
            "total": 50
        }
    }
    
    # Log response
    logger.log_response(
        provider="test_provider",
        endpoint="/generate",
        method="POST",
        request_id="123",
        status_code=200,
        response_time=0.5,
        response_data=response_data,
        custom_field="value"
    )
    
    # Check log call
    mock_logger.info.assert_called_once()
    args, kwargs = mock_logger.info.call_args
    
    assert args[0] == "API Response: 200 POST /generate"
    assert kwargs["extra"]["event_type"] == "api_response"
    assert kwargs["extra"]["provider"] == "test_provider"
    assert kwargs["extra"]["endpoint"] == "/generate"
    assert kwargs["extra"]["method"] == "POST"
    assert kwargs["extra"]["request_id"] == "123"
    assert kwargs["extra"]["status_code"] == 200
    assert kwargs["extra"]["response_time"] == 0.5
    assert kwargs["extra"]["custom_field"] == "value"
    assert kwargs["extra"]["response"] == response_data

def test_log_response_error(mock_logger):
    """Test logging API error response."""
    logger = APILogger()
    
    # Log error response
    logger.log_response(
        provider="test_provider",
        endpoint="/generate",
        method="POST",
        request_id="123",
        status_code=400,
        response_time=0.5,
        error="Bad Request",
        custom_field="value"
    )
    
    # Check log call
    mock_logger.error.assert_called_once()
    args, kwargs = mock_logger.error.call_args
    
    assert args[0] == "API Error: 400 POST /generate"
    assert kwargs["extra"]["event_type"] == "api_response"
    assert kwargs["extra"]["provider"] == "test_provider"
    assert kwargs["extra"]["endpoint"] == "/generate"
    assert kwargs["extra"]["method"] == "POST"
    assert kwargs["extra"]["request_id"] == "123"
    assert kwargs["extra"]["status_code"] == 400
    assert kwargs["extra"]["response_time"] == 0.5
    assert kwargs["extra"]["error"] == "Bad Request"
    assert kwargs["extra"]["custom_field"] == "value"

def test_log_response_with_sensitive_data(mock_logger):
    """Test logging response with sensitive data."""
    logger = APILogger()
    
    # Test response with sensitive data
    response_data = {
        "id": "resp123",
        "token": {
            "access_token": "token123",
            "refresh_token": "refresh123"
        }
    }
    
    # Log response
    logger.log_response(
        provider="test_provider",
        endpoint="/auth",
        method="POST",
        request_id="123",
        status_code=200,
        response_time=0.5,
        response_data=response_data
    )
    
    # Check log call
    mock_logger.info.assert_called_once()
    args, kwargs = mock_logger.info.call_args
    
    # Check response sanitization
    assert kwargs["extra"]["response"]["token"]["access_token"] == "***REDACTED***"
    assert kwargs["extra"]["response"]["token"]["refresh_token"] == "***REDACTED***" 