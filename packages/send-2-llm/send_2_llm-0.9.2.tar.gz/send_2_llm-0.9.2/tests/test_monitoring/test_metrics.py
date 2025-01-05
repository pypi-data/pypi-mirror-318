"""Tests for MetricsCollector."""

import time
import pytest
from send_2_llm.monitoring.metrics import MetricsCollector
from send_2_llm.types import ProviderType

def test_record_request():
    """Test recording request metrics."""
    collector = MetricsCollector()
    
    # Record successful request
    collector.record_request(
        provider=ProviderType.OPENAI,
        latency=0.5,
        success=True,
        tokens=100,
        cost=0.002
    )
    
    metrics = collector._get_metrics(ProviderType.OPENAI)
    assert metrics.total_requests == 1
    assert metrics.successful_requests == 1
    assert metrics.failed_requests == 0
    assert metrics.total_tokens == 100
    assert metrics.total_cost == 0.002
    assert metrics.total_latency == 0.5
    assert metrics.last_success is not None
    assert metrics.last_failure is None

def test_success_rate():
    """Test success rate calculation."""
    collector = MetricsCollector()
    
    # No requests yet
    assert collector.get_success_rate(ProviderType.OPENAI) == 1.0
    
    # Record mix of successes and failures
    collector.record_request(ProviderType.OPENAI, 0.5, True, 100, 0.002)
    collector.record_request(ProviderType.OPENAI, 0.5, False, 100, 0.002)
    collector.record_request(ProviderType.OPENAI, 0.5, True, 100, 0.002)
    
    assert collector.get_success_rate(ProviderType.OPENAI) == 2/3

def test_average_latency():
    """Test average latency calculation."""
    collector = MetricsCollector()
    
    # No requests yet
    assert collector.get_average_latency(ProviderType.OPENAI) == 0.0
    
    # Record requests with different latencies
    collector.record_request(ProviderType.OPENAI, 0.5, True, 100, 0.002)
    collector.record_request(ProviderType.OPENAI, 1.5, True, 100, 0.002)
    
    assert collector.get_average_latency(ProviderType.OPENAI) == 1.0

def test_recent_metrics():
    """Test getting recent metrics."""
    collector = MetricsCollector()
    
    # Record some requests
    collector.record_request(ProviderType.OPENAI, 0.5, True, 100, 0.002)
    time.sleep(0.1)  # Ensure different timestamps
    collector.record_request(ProviderType.OPENAI, 1.5, False, 100, 0.002)
    
    recent = collector.get_recent_metrics(ProviderType.OPENAI)
    assert len(recent) == 2
    assert recent[0].success
    assert not recent[1].success

def test_health_check():
    """Test provider health check."""
    collector = MetricsCollector()
    
    # No requests yet, but never failed
    assert not collector.is_healthy(ProviderType.OPENAI)
    
    # Record some successes
    for _ in range(9):
        collector.record_request(ProviderType.OPENAI, 0.5, True, 100, 0.002)
        
    # Should be healthy with 90% success rate
    assert collector.is_healthy(ProviderType.OPENAI)
    
    # Add a failure
    collector.record_request(ProviderType.OPENAI, 0.5, False, 100, 0.002)
    
    # Should still be healthy with 90% success rate
    assert collector.is_healthy(ProviderType.OPENAI)
    
    # Add another failure
    collector.record_request(ProviderType.OPENAI, 0.5, False, 100, 0.002)
    
    # Should be unhealthy with < 90% success rate
    assert not collector.is_healthy(ProviderType.OPENAI) 