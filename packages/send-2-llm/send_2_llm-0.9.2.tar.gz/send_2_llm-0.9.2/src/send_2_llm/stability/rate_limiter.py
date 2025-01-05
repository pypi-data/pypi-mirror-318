"""Rate limiter for send_2_llm.

This module handles request rate limiting using token bucket algorithm.
"""

import time
import logging
import asyncio
from typing import Dict, Optional
from dataclasses import dataclass
from ..types import ProviderType

logger = logging.getLogger(__name__)

@dataclass
class TokenBucket:
    """Token bucket for rate limiting."""
    capacity: float  # Maximum number of tokens
    rate: float     # Tokens per second
    tokens: float   # Current number of tokens
    last_update: float  # Last update timestamp

class RateLimiter:
    """Rate limiter using token bucket algorithm."""
    
    def __init__(self, default_rate: float = 10.0, default_capacity: float = 10.0):
        """Initialize rate limiter.
        
        Args:
            default_rate: Default tokens per second
            default_capacity: Default bucket capacity
        """
        self._default_rate = default_rate
        self._default_capacity = default_capacity
        self._buckets: Dict[ProviderType, TokenBucket] = {}
        
    def _get_bucket(self, provider: ProviderType) -> TokenBucket:
        """Get or create token bucket for provider.
        
        Args:
            provider: Provider to get bucket for
            
        Returns:
            TokenBucket: Token bucket for provider
        """
        if provider not in self._buckets:
            self._buckets[provider] = TokenBucket(
                capacity=self._default_capacity,
                rate=self._default_rate,
                tokens=self._default_capacity,
                last_update=time.time()
            )
        return self._buckets[provider]
        
    def _update_tokens(self, bucket: TokenBucket) -> None:
        """Update tokens in bucket based on elapsed time.
        
        Args:
            bucket: Bucket to update
        """
        now = time.time()
        elapsed = now - bucket.last_update
        new_tokens = elapsed * bucket.rate
        
        bucket.tokens = min(bucket.capacity, bucket.tokens + new_tokens)
        bucket.last_update = now
        
    async def acquire(
        self,
        provider: ProviderType,
        tokens: float = 1.0,
        timeout: Optional[float] = None
    ) -> bool:
        """Acquire tokens for provider.
        
        Args:
            provider: Provider to acquire tokens for
            tokens: Number of tokens to acquire
            timeout: Maximum time to wait in seconds
            
        Returns:
            bool: True if tokens acquired, False if timeout
        """
        start_time = time.time()
        bucket = self._get_bucket(provider)
        
        while True:
            self._update_tokens(bucket)
            
            if bucket.tokens >= tokens:
                bucket.tokens -= tokens
                return True
                
            if timeout is not None:
                if time.time() - start_time >= timeout:
                    logger.warning(
                        f"Rate limit timeout for {provider.value} "
                        f"requesting {tokens} tokens"
                    )
                    return False
                    
            # Calculate wait time and check if it exceeds timeout
            wait_time = (tokens - bucket.tokens) / bucket.rate
            if timeout is not None and wait_time > timeout - (time.time() - start_time):
                logger.warning(
                    f"Rate limit timeout for {provider.value} - "
                    f"would need to wait {wait_time:.2f}s"
                )
                return False
                
            # Wait for tokens to replenish
            await asyncio.sleep(min(wait_time, 1.0))  # Cap wait at 1 second
            
    def set_rate(self, provider: ProviderType, rate: float, capacity: Optional[float] = None) -> None:
        """Set rate for provider.
        
        Args:
            provider: Provider to set rate for
            rate: Tokens per second
            capacity: Optional new capacity
        """
        bucket = self._get_bucket(provider)
        bucket.rate = rate
        if capacity is not None:
            bucket.capacity = capacity
            bucket.tokens = min(bucket.tokens, capacity)
            
    def get_rate(self, provider: ProviderType) -> float:
        """Get current rate for provider.
        
        Args:
            provider: Provider to get rate for
            
        Returns:
            float: Current tokens per second rate
        """
        return self._get_bucket(provider).rate 