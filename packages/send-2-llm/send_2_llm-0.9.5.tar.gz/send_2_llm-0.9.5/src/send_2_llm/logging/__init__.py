"""
Logging system for send_2_llm.

Features:
- Structured logging with JSON format
- Configurable log levels per component
- Automatic log rotation
- Performance logging
- Security event logging
- API request/response logging
"""

import os
import logging
import logging.handlers
import json
from typing import Any, Dict, Optional
from datetime import datetime

# Default log format for structured logging
DEFAULT_LOG_FORMAT = {
    "timestamp": "%(asctime)s",
    "level": "%(levelname)s",
    "module": "%(module)s",
    "function": "%(funcName)s",
    "line": "%(lineno)d",
    "message": "%(message)s"
}

class StructuredJsonFormatter(logging.Formatter):
    """JSON formatter for structured logging."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        # Base log record
        log_obj = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage()
        }
        
        # Add extra fields if present
        if hasattr(record, "extra"):
            log_obj.update(record.extra)
            
        # Add exception info if present
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_obj)

def setup_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    max_bytes: int = 10_485_760,  # 10MB
    backup_count: int = 5,
    json_format: bool = True
) -> None:
    """Setup logging configuration.
    
    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file. If None, logs to console only
        max_bytes: Maximum size of log file before rotation
        backup_count: Number of backup files to keep
        json_format: Whether to use JSON formatting
    """
    # Get root logger
    logger = logging.getLogger("send_2_llm")
    logger.setLevel(level)
    
    # Clear existing handlers
    logger.handlers = []
    
    # Create formatter
    if json_format:
        formatter = StructuredJsonFormatter()
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler if log_file specified
    if log_file:
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

# Create default logger
logger = logging.getLogger("send_2_llm")

# Setup default configuration from environment
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE")
LOG_JSON = os.getenv("LOG_JSON", "true").lower() == "true"

setup_logging(
    level=LOG_LEVEL,
    log_file=LOG_FILE,
    json_format=LOG_JSON
) 