"""Circuit breaker for send_2_llm.

This module handles error tracking and temporary provider disabling.
"""

import time
import logging
from enum import Enum
from typing import Dict, Optional, List
from dataclasses import dataclass
from ..types import ProviderType

logger = logging.getLogger(__name__)

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"         # Provider disabled
    HALF_OPEN = "half_open"  # Testing if provider recovered

@dataclass
class ErrorStats:
    """Error statistics for a provider."""
    error_count: int = 0
    last_error_time: Optional[float] = None
    consecutive_failures: int = 0
    last_success_time: Optional[float] = None

class CircuitBreaker:
    """Circuit breaker for managing provider availability."""
    
    def __init__(
        self,
        error_threshold: int = 5,
        recovery_timeout: float = 300.0,  # 5 minutes
        half_open_timeout: float = 60.0,  # 1 minute
    ):
        """Initialize circuit breaker.
        
        Args:
            error_threshold: Number of errors before opening circuit
            recovery_timeout: Time in seconds before attempting recovery
            half_open_timeout: Time in seconds to test recovery
        """
        self._error_threshold = error_threshold
        self._recovery_timeout = recovery_timeout
        self._half_open_timeout = half_open_timeout
        
        self._states: Dict[ProviderType, CircuitState] = {}
        self._stats: Dict[ProviderType, ErrorStats] = {}
        
    def record_success(self, provider: ProviderType) -> None:
        """Record successful operation for provider.
        
        Args:
            provider: Provider that succeeded
        """
        if provider not in self._stats:
            self._stats[provider] = ErrorStats()
            
        stats = self._stats[provider]
        stats.consecutive_failures = 0
        stats.last_success_time = time.time()
        
        # If in half-open state and success, close circuit
        if self.get_state(provider) == CircuitState.HALF_OPEN:
            self._states[provider] = CircuitState.CLOSED
            logger.info(f"Circuit closed for {provider.value} after successful recovery")
            
    def record_error(self, provider: ProviderType) -> None:
        """Record error for provider.
        
        Args:
            provider: Provider that failed
        """
        if provider not in self._stats:
            self._stats[provider] = ErrorStats()
            
        stats = self._stats[provider]
        stats.error_count += 1
        stats.consecutive_failures += 1
        stats.last_error_time = time.time()
        
        # Check if should open circuit
        if (stats.consecutive_failures >= self._error_threshold and 
            self.get_state(provider) == CircuitState.CLOSED):
            self._states[provider] = CircuitState.OPEN
            logger.warning(
                f"Circuit opened for {provider.value} after "
                f"{stats.consecutive_failures} consecutive failures"
            )
            
    def get_state(self, provider: ProviderType) -> CircuitState:
        """Get current state for provider.
        
        Args:
            provider: Provider to check state for
            
        Returns:
            CircuitState: Current circuit state
        """
        if provider not in self._states:
            self._states[provider] = CircuitState.CLOSED
            return CircuitState.CLOSED
            
        current_state = self._states[provider]
        
        # Check if should transition from OPEN to HALF_OPEN
        if current_state == CircuitState.OPEN:
            stats = self._stats.get(provider)
            if stats and stats.last_error_time:
                time_since_error = time.time() - stats.last_error_time
                if time_since_error >= self._recovery_timeout:
                    self._states[provider] = CircuitState.HALF_OPEN
                    logger.info(f"Circuit half-opened for {provider.value} to test recovery")
                    return CircuitState.HALF_OPEN
                    
        return current_state
        
    def is_available(self, provider: ProviderType) -> bool:
        """Check if provider is available.
        
        Args:
            provider: Provider to check availability for
            
        Returns:
            bool: True if provider is available
        """
        state = self.get_state(provider)
        return state in (CircuitState.CLOSED, CircuitState.HALF_OPEN)
        
    def get_available_providers(self, providers: List[ProviderType]) -> List[ProviderType]:
        """Get list of available providers from provided list.
        
        Args:
            providers: List of providers to check
            
        Returns:
            List[ProviderType]: List of available providers
        """
        return [p for p in providers if self.is_available(p)] 