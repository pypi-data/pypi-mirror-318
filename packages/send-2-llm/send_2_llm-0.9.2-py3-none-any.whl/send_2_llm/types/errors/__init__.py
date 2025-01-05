"""Error types for the LLM system."""

from typing import Optional
from pydantic import BaseModel, Field

from ..common import ProviderType, ErrorDetails


class LLMError(Exception):
    """Base class for LLM errors."""
    
    def __init__(self, message: str, provider: Optional[ProviderType] = None, error_details: Optional[ErrorDetails] = None):
        self.provider = provider
        self.error_details = error_details
        super().__init__(message)


class TokenLimitError(LLMError):
    """Token limit exceeded error."""
    pass


class ProviderAPIError(LLMError):
    """Provider API error."""
    
    def __init__(self, message: str, provider: Optional[ProviderType] = None, error_details: Optional[ErrorDetails] = None):
        super().__init__(message, provider=provider, error_details=error_details)


class ProviderNotAvailableError(LLMError):
    """Provider not available error."""
    pass


class StrategyError(LLMError):
    """Strategy error."""
    pass


class SecurityError(Exception):
    """Security related errors."""
    pass


class ValidationError(Exception):
    """Validation errors."""
    pass


class ProviderError(Exception):
    """Provider specific errors."""
    pass


class RateLimitError(Exception):
    """Rate limit exceeded errors."""
    pass 