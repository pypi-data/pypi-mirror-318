"""Performance metrics logging module."""

import time
import asyncio
import logging
from functools import wraps
from typing import Any, Callable, Dict, Optional
from datetime import datetime

logger = logging.getLogger("send_2_llm.metrics")

class MetricsLogger:
    """Logger for performance metrics."""
    
    def __init__(self):
        self.logger = logger
    
    def log_duration(self, operation: str, duration: float, **extra: Any) -> None:
        """Log operation duration.
        
        Args:
            operation: Name of the operation
            duration: Duration in seconds
            **extra: Additional fields to log
        """
        self.logger.info(
            f"{operation} completed",
            extra={
                "metric_type": "duration",
                "operation": operation,
                "duration_seconds": duration,
                **extra
            }
        )
    
    def log_token_usage(
        self,
        provider: str,
        prompt_tokens: int,
        completion_tokens: int,
        total_tokens: int,
        cost: float,
        **extra: Any
    ) -> None:
        """Log token usage metrics.
        
        Args:
            provider: Provider name
            prompt_tokens: Number of prompt tokens
            completion_tokens: Number of completion tokens
            total_tokens: Total number of tokens
            cost: Cost in USD
            **extra: Additional fields to log
        """
        self.logger.info(
            f"Token usage for {provider}",
            extra={
                "metric_type": "token_usage",
                "provider": provider,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "cost_usd": cost,
                **extra
            }
        )
    
    def log_error(
        self,
        error_type: str,
        error_message: str,
        **extra: Any
    ) -> None:
        """Log error metrics.
        
        Args:
            error_type: Type of error
            error_message: Error message
            **extra: Additional fields to log
        """
        self.logger.error(
            error_message,
            extra={
                "metric_type": "error",
                "error_type": error_type,
                **extra
            }
        )

def timing_decorator(operation: str):
    """Decorator to measure and log function execution time.
    
    Args:
        operation: Name of the operation being timed
    """
    def decorator(func: Callable):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time
                metrics_logger.log_duration(operation, duration)
                return result
            except Exception as e:
                duration = time.time() - start_time
                metrics_logger.log_duration(
                    operation,
                    duration,
                    error=str(e)
                )
                raise
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                metrics_logger.log_duration(operation, duration)
                return result
            except Exception as e:
                duration = time.time() - start_time
                metrics_logger.log_duration(
                    operation,
                    duration,
                    error=str(e)
                )
                raise
        
        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    return decorator

# Create global metrics logger instance
metrics_logger = MetricsLogger() 