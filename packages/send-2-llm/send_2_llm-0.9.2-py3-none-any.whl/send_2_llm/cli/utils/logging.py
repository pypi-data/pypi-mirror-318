"""Logging utilities for CLI."""

import os
import sys
import logging
import json
from datetime import datetime
from typing import Any, Dict, Optional
from pathlib import Path
from rich.logging import RichHandler

# Configure logging directory
LOG_DIR = Path.home() / '.send_2_llm' / 'logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure file names
CLI_LOG = LOG_DIR / 'cli.log'
REQUEST_LOG = LOG_DIR / 'requests.log'
ERROR_LOG = LOG_DIR / 'errors.log'

# Create formatters
CONSOLE_FORMAT = "%(message)s"
FILE_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logging(debug: bool = False) -> None:
    """Setup logging configuration.
    
    Args:
        debug: Whether to enable debug logging
    """
    # Set log level
    level = logging.DEBUG if debug else logging.INFO
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        format=CONSOLE_FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    
    # Create file handlers
    cli_handler = logging.FileHandler(CLI_LOG)
    cli_handler.setFormatter(logging.Formatter(FILE_FORMAT))
    
    request_handler = logging.FileHandler(REQUEST_LOG)
    request_handler.setFormatter(logging.Formatter(FILE_FORMAT))
    
    error_handler = logging.FileHandler(ERROR_LOG)
    error_handler.setFormatter(logging.Formatter(FILE_FORMAT))
    
    # Configure loggers
    cli_logger = logging.getLogger('cli')
    cli_logger.addHandler(cli_handler)
    cli_logger.setLevel(level)
    
    request_logger = logging.getLogger('requests')
    request_logger.addHandler(request_handler)
    request_logger.setLevel(level)
    
    error_logger = logging.getLogger('errors')
    error_logger.addHandler(error_handler)
    error_logger.setLevel(logging.ERROR)


def log_command(command: str, args: Dict[str, Any]) -> None:
    """Log CLI command execution.
    
    Args:
        command: Command name
        args: Command arguments
    """
    logger = logging.getLogger('cli')
    logger.info(f"Executing command: {command}")
    logger.debug(f"Arguments: {json.dumps(args, default=str)}")


def log_request(provider: str,
                model: str,
                text: str,
                format: Optional[str] = None,
                json: bool = False) -> None:
    """Log LLM request.
    
    Args:
        provider: Provider name
        model: Model name
        text: Input text
        format: Output format
        json: Whether JSON output was requested
    """
    logger = logging.getLogger('requests')
    logger.info(f"Request to {provider}/{model}")
    logger.debug(
        json.dumps({
            'provider': provider,
            'model': model,
            'text': text,
            'format': format,
            'json': json,
            'timestamp': datetime.now().isoformat()
        })
    )


def log_error(error: Exception, context: Dict[str, Any]) -> None:
    """Log error with context.
    
    Args:
        error: Exception that occurred
        context: Error context
    """
    logger = logging.getLogger('errors')
    logger.error(
        f"Error: {str(error)}",
        extra={
            'error_type': type(error).__name__,
            'context': json.dumps(context, default=str)
        },
        exc_info=True
    ) 