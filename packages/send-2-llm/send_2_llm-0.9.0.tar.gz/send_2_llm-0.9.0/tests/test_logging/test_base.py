"""Tests for base logging functionality."""

import os
import json
import logging
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from send_2_llm.logging import (
    setup_logging,
    StructuredJsonFormatter
)

def test_json_formatter():
    """Test JSON formatter."""
    formatter = StructuredJsonFormatter()
    
    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None
    )
    
    # Format record
    formatted = formatter.format(record)
    log_dict = json.loads(formatted)
    
    # Check required fields
    assert "timestamp" in log_dict
    assert log_dict["level"] == "INFO"
    assert log_dict["module"] == "test"
    assert log_dict["message"] == "Test message"
    assert log_dict["line"] == 1

def test_json_formatter_with_extra():
    """Test JSON formatter with extra fields."""
    formatter = StructuredJsonFormatter()
    
    # Create record with extra fields
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="Test message",
        args=(),
        exc_info=None
    )
    record.extra = {"custom_field": "custom_value"}
    
    # Format record
    formatted = formatter.format(record)
    log_dict = json.loads(formatted)
    
    # Check extra field
    assert log_dict["custom_field"] == "custom_value"

def test_json_formatter_with_exception():
    """Test JSON formatter with exception info."""
    formatter = StructuredJsonFormatter()
    
    try:
        raise ValueError("Test error")
    except ValueError:
        # Create record with exception
        record = logging.LogRecord(
            name="test",
            level=logging.ERROR,
            pathname="test.py",
            lineno=1,
            msg="Error occurred",
            args=(),
            exc_info=True
        )
    
    # Format record
    formatted = formatter.format(record)
    log_dict = json.loads(formatted)
    
    # Check exception info
    assert "exception" in log_dict
    assert "ValueError: Test error" in log_dict["exception"]

def test_setup_logging_console():
    """Test logging setup with console output."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        
        # Setup logging
        setup_logging(level="DEBUG", log_file=None)
        
        # Check logger configuration
        assert mock_logger.setLevel.called_with(logging.DEBUG)
        assert len(mock_logger.handlers) == 1
        assert isinstance(mock_logger.handlers[0], logging.StreamHandler)

def test_setup_logging_file():
    """Test logging setup with file output."""
    with tempfile.TemporaryDirectory() as temp_dir:
        log_file = Path(temp_dir) / "test.log"
        
        with patch("logging.getLogger") as mock_get_logger:
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            
            # Setup logging
            setup_logging(
                level="INFO",
                log_file=str(log_file),
                max_bytes=1000,
                backup_count=3
            )
            
            # Check logger configuration
            assert mock_logger.setLevel.called_with(logging.INFO)
            assert len(mock_logger.handlers) == 2
            assert isinstance(mock_logger.handlers[0], logging.StreamHandler)
            assert isinstance(
                mock_logger.handlers[1],
                logging.handlers.RotatingFileHandler
            )

def test_setup_logging_environment():
    """Test logging setup from environment variables."""
    with tempfile.TemporaryDirectory() as temp_dir:
        log_file = Path(temp_dir) / "test.log"
        
        with patch.dict(os.environ, {
            "LOG_LEVEL": "DEBUG",
            "LOG_FILE": str(log_file),
            "LOG_JSON": "true"
        }):
            with patch("logging.getLogger") as mock_get_logger:
                mock_logger = MagicMock()
                mock_get_logger.return_value = mock_logger
                
                # Import to trigger environment setup
                from send_2_llm import logging
                
                # Check logger configuration
                assert mock_logger.setLevel.called_with(logging.DEBUG)
                assert len(mock_logger.handlers) == 2 