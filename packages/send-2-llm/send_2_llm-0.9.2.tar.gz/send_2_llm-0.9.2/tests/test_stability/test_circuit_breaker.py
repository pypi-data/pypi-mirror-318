"""Tests for CircuitBreaker."""

import time
import pytest
from send_2_llm.stability.circuit_breaker import CircuitBreaker, CircuitState
from send_2_llm.types import ProviderType

def test_initial_state():
    """Test initial circuit breaker state."""
    breaker = CircuitBreaker()
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.CLOSED
    assert breaker.is_available(ProviderType.OPENAI)

def test_error_threshold():
    """Test circuit opens after error threshold."""
    breaker = CircuitBreaker(error_threshold=3)
    
    # Record errors up to threshold
    for _ in range(3):
        breaker.record_error(ProviderType.OPENAI)
        
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.OPEN
    assert not breaker.is_available(ProviderType.OPENAI)

def test_recovery_timeout():
    """Test circuit transitions to half-open after timeout."""
    breaker = CircuitBreaker(
        error_threshold=1,
        recovery_timeout=0.1  # 100ms for testing
    )
    
    # Open circuit
    breaker.record_error(ProviderType.OPENAI)
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.OPEN
    
    # Wait for recovery timeout
    time.sleep(0.2)
    
    # Should transition to half-open
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.HALF_OPEN
    assert breaker.is_available(ProviderType.OPENAI)

def test_success_closes_circuit():
    """Test successful operation closes circuit."""
    breaker = CircuitBreaker(
        error_threshold=1,
        recovery_timeout=0.1
    )
    
    # Open circuit
    breaker.record_error(ProviderType.OPENAI)
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.OPEN
    
    # Wait for recovery
    time.sleep(0.2)
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.HALF_OPEN
    
    # Record success
    breaker.record_success(ProviderType.OPENAI)
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.CLOSED

def test_multiple_providers():
    """Test circuit breaker handles multiple providers independently."""
    breaker = CircuitBreaker(error_threshold=1)
    
    # Open circuit for OpenAI
    breaker.record_error(ProviderType.OPENAI)
    assert breaker.get_state(ProviderType.OPENAI) == CircuitState.OPEN
    
    # Anthropic should still be closed
    assert breaker.get_state(ProviderType.ANTHROPIC) == CircuitState.CLOSED

def test_get_available_providers():
    """Test getting available providers."""
    breaker = CircuitBreaker(error_threshold=1)
    providers = [ProviderType.OPENAI, ProviderType.ANTHROPIC]
    
    # Initially all available
    assert breaker.get_available_providers(providers) == providers
    
    # Open circuit for OpenAI
    breaker.record_error(ProviderType.OPENAI)
    assert breaker.get_available_providers(providers) == [ProviderType.ANTHROPIC] 