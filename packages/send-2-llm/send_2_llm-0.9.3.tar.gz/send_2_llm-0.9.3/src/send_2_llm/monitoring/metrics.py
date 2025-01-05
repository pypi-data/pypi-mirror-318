"""Metrics collection for send_2_llm.

This module handles performance metrics and provider availability monitoring.
"""

import time
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import deque
from ..types import ProviderType

logger = logging.getLogger(__name__)

@dataclass
class RequestMetrics:
    """Metrics for a single request."""
    timestamp: float
    latency: float  # Request latency in seconds
    success: bool   # Whether request succeeded
    tokens: int     # Number of tokens used
    cost: float     # Cost of request

@dataclass
class ProviderMetrics:
    """Metrics for a provider."""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_tokens: int = 0
    total_cost: float = 0.0
    total_latency: float = 0.0
    last_success: Optional[float] = None
    last_failure: Optional[float] = None
    recent_requests: deque = field(default_factory=lambda: deque(maxlen=100))

class MetricsCollector:
    """Collects and aggregates metrics."""
    
    def __init__(self, history_minutes: int = 60):
        """Initialize metrics collector.
        
        Args:
            history_minutes: How many minutes of detailed history to keep
        """
        self._history_minutes = history_minutes
        self._provider_metrics: Dict[ProviderType, ProviderMetrics] = {}
        
    def _get_metrics(self, provider: ProviderType) -> ProviderMetrics:
        """Get or create metrics for provider.
        
        Args:
            provider: Provider to get metrics for
            
        Returns:
            ProviderMetrics: Metrics for provider
        """
        if provider not in self._provider_metrics:
            self._provider_metrics[provider] = ProviderMetrics()
        return self._provider_metrics[provider]
        
    def record_request(
        self,
        provider: ProviderType,
        latency: float,
        success: bool,
        tokens: int,
        cost: float
    ) -> None:
        """Record metrics for a request.
        
        Args:
            provider: Provider that handled request
            latency: Request latency in seconds
            success: Whether request succeeded
            tokens: Number of tokens used
            cost: Cost of request
        """
        metrics = self._get_metrics(provider)
        
        # Update aggregate metrics
        metrics.total_requests += 1
        metrics.total_tokens += tokens
        metrics.total_cost += cost
        metrics.total_latency += latency
        
        if success:
            metrics.successful_requests += 1
            metrics.last_success = time.time()
        else:
            metrics.failed_requests += 1
            metrics.last_failure = time.time()
            
        # Record detailed metrics
        request_metrics = RequestMetrics(
            timestamp=time.time(),
            latency=latency,
            success=success,
            tokens=tokens,
            cost=cost
        )
        metrics.recent_requests.append(request_metrics)
        
    def get_success_rate(self, provider: ProviderType) -> float:
        """Get success rate for provider.
        
        Args:
            provider: Provider to get rate for
            
        Returns:
            float: Success rate (0-1)
        """
        metrics = self._get_metrics(provider)
        if metrics.total_requests == 0:
            return 1.0
        return metrics.successful_requests / metrics.total_requests
        
    def get_average_latency(self, provider: ProviderType) -> float:
        """Get average latency for provider.
        
        Args:
            provider: Provider to get latency for
            
        Returns:
            float: Average latency in seconds
        """
        metrics = self._get_metrics(provider)
        if metrics.total_requests == 0:
            return 0.0
        return metrics.total_latency / metrics.total_requests
        
    def get_recent_metrics(
        self,
        provider: ProviderType,
        minutes: Optional[int] = None
    ) -> List[RequestMetrics]:
        """Get recent request metrics.
        
        Args:
            provider: Provider to get metrics for
            minutes: Optional time window in minutes
            
        Returns:
            List[RequestMetrics]: Recent request metrics
        """
        metrics = self._get_metrics(provider)
        if not minutes:
            return list(metrics.recent_requests)
            
        cutoff = time.time() - (minutes * 60)
        return [m for m in metrics.recent_requests if m.timestamp >= cutoff]
        
    def is_healthy(
        self,
        provider: ProviderType,
        success_threshold: float = 0.9,
        window_minutes: int = 5
    ) -> bool:
        """Check if provider is healthy.
        
        Args:
            provider: Provider to check
            success_threshold: Minimum success rate
            window_minutes: Time window to check
            
        Returns:
            bool: True if provider is healthy
        """
        metrics = self._get_metrics(provider)
        
        # Check if any recent requests
        recent = self.get_recent_metrics(provider, window_minutes)
        if not recent:
            # No recent requests, check if ever succeeded
            return metrics.last_success is not None
            
        # Calculate success rate in window
        successes = sum(1 for m in recent if m.success)
        rate = successes / len(recent)
        return rate >= success_threshold 

class Monitoring:
    """Monitoring interface for tracking provider health and performance."""
    
    def __init__(self):
        """Initialize monitoring."""
        self._collector = MetricsCollector()
        
    def track_request(self, provider: ProviderType, model: str):
        """Context manager for tracking request metrics.
        
        Args:
            provider: Provider being used
            model: Model being used
            
        Returns:
            Context manager that tracks request metrics
        """
        start_time = time.time()
        success = True
        tokens = 0
        cost = 0.0
        
        class RequestTracker:
            def __init__(self, monitoring, provider, start_time):
                self.monitoring = monitoring
                self.provider = provider
                self.start_time = start_time
                self.success = True
                self.tokens = 0
                self.cost = 0.0
                
            def __enter__(self):
                return self
                
            def __exit__(self, exc_type, exc_val, exc_tb):
                end_time = time.time()
                latency = end_time - self.start_time
                
                if exc_type is not None:
                    self.success = False
                    
                self.monitoring._collector.record_request(
                    provider=self.provider,
                    latency=latency,
                    success=self.success,
                    tokens=self.tokens,
                    cost=self.cost
                )
                
        return RequestTracker(self, provider, start_time)
        
    def is_healthy(self, provider: ProviderType) -> bool:
        """Check if provider is healthy.
        
        Args:
            provider: Provider to check
            
        Returns:
            bool: True if provider is healthy
        """
        return self._collector.is_healthy(provider)
        
    def get_success_rate(self, provider: ProviderType) -> float:
        """Get success rate for provider.
        
        Args:
            provider: Provider to get rate for
            
        Returns:
            float: Success rate (0-1)
        """
        return self._collector.get_success_rate(provider)
        
    def get_average_latency(self, provider: ProviderType) -> float:
        """Get average latency for provider.
        
        Args:
            provider: Provider to get latency for
            
        Returns:
            float: Average latency in seconds
        """
        return self._collector.get_average_latency(provider) 