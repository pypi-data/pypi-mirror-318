"""API request/response logging module."""

import logging
import json
from typing import Any, Dict, Optional
from datetime import datetime

logger = logging.getLogger("send_2_llm.api")

class APILogger:
    """Logger for API requests and responses."""
    
    def __init__(self):
        self.logger = logger
    
    def sanitize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize sensitive data from logs.
        
        Args:
            data: Data to sanitize
            
        Returns:
            Sanitized data with sensitive fields masked
        """
        SENSITIVE_FIELDS = {
            "api_key", "token", "secret", "password", "authorization",
            "access_token", "refresh_token"
        }
        
        def _sanitize_dict(d: Dict[str, Any]) -> Dict[str, Any]:
            sanitized = {}
            for k, v in d.items():
                if any(field in k.lower() for field in SENSITIVE_FIELDS):
                    sanitized[k] = "***REDACTED***"
                elif isinstance(v, dict):
                    sanitized[k] = _sanitize_dict(v)
                else:
                    sanitized[k] = v
            return sanitized
        
        return _sanitize_dict(data)
    
    def log_request(
        self,
        provider: str,
        endpoint: str,
        method: str,
        request_id: str,
        payload: Optional[Dict[str, Any]] = None,
        **extra: Any
    ) -> None:
        """Log API request.
        
        Args:
            provider: Provider name
            endpoint: API endpoint
            method: HTTP method
            request_id: Unique request ID
            payload: Request payload
            **extra: Additional fields to log
        """
        log_data = {
            "event_type": "api_request",
            "provider": provider,
            "endpoint": endpoint,
            "method": method,
            "request_id": request_id,
            "timestamp": datetime.utcnow().isoformat(),
            **extra
        }
        
        if payload:
            log_data["payload"] = self.sanitize_data(payload)
        
        self.logger.info(
            f"API Request: {method} {endpoint}",
            extra=log_data
        )
    
    def log_response(
        self,
        provider: str,
        endpoint: str,
        method: str,
        request_id: str,
        status_code: int,
        response_time: float,
        response_data: Optional[Dict[str, Any]] = None,
        error: Optional[str] = None,
        **extra: Any
    ) -> None:
        """Log API response.
        
        Args:
            provider: Provider name
            endpoint: API endpoint
            method: HTTP method
            request_id: Unique request ID
            status_code: HTTP status code
            response_time: Response time in seconds
            response_data: Response data
            error: Error message if any
            **extra: Additional fields to log
        """
        log_data = {
            "event_type": "api_response",
            "provider": provider,
            "endpoint": endpoint,
            "method": method,
            "request_id": request_id,
            "status_code": status_code,
            "response_time": response_time,
            "timestamp": datetime.utcnow().isoformat(),
            **extra
        }
        
        if error:
            log_data["error"] = error
        
        if response_data:
            log_data["response"] = self.sanitize_data(response_data)
        
        if 200 <= status_code < 300:
            self.logger.info(
                f"API Response: {status_code} {method} {endpoint}",
                extra=log_data
            )
        else:
            self.logger.error(
                f"API Error: {status_code} {method} {endpoint}",
                extra=log_data
            )

# Create global API logger instance
api_logger = APILogger() 