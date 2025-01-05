"""Tests for RateLimiter."""

import time
import pytest
from send_2_llm.stability.rate_limiter import RateLimiter
from send_2_llm.types import ProviderType

@pytest.mark.asyncio
async def test_acquire_tokens():
    """Test acquiring tokens."""
    limiter = RateLimiter(default_rate=10.0, default_capacity=10.0)
    assert await limiter.acquire(ProviderType.OPENAI, tokens=1.0)

@pytest.mark.asyncio
async def test_rate_limiting():
    """Test rate limiting when tokens exhausted."""
    limiter = RateLimiter(default_rate=1.0, default_capacity=1.0)
    
    # First request should succeed
    assert await limiter.acquire(ProviderType.OPENAI, tokens=1.0)
    
    # Second request should timeout
    assert not await limiter.acquire(
        ProviderType.OPENAI,
        tokens=1.0,
        timeout=0.1
    )

@pytest.mark.asyncio
async def test_token_replenishment():
    """Test tokens replenish over time."""
    limiter = RateLimiter(default_rate=10.0, default_capacity=1.0)
    
    # Use all tokens
    assert await limiter.acquire(ProviderType.OPENAI, tokens=1.0)
    
    # Wait for tokens to replenish
    await limiter.acquire(ProviderType.OPENAI, tokens=1.0)
    
    # Should have tokens again
    assert await limiter.acquire(ProviderType.OPENAI, tokens=0.5)

@pytest.mark.asyncio
async def test_multiple_providers():
    """Test rate limiting works independently for providers."""
    limiter = RateLimiter(default_rate=1.0, default_capacity=1.0)
    
    # Use OpenAI tokens
    assert await limiter.acquire(ProviderType.OPENAI, tokens=1.0)
    assert not await limiter.acquire(
        ProviderType.OPENAI,
        tokens=1.0,
        timeout=0.1
    )
    
    # Anthropic should still have tokens
    assert await limiter.acquire(ProviderType.ANTHROPIC, tokens=1.0)

def test_set_rate():
    """Test setting custom rates."""
    limiter = RateLimiter()
    
    # Set custom rate
    limiter.set_rate(ProviderType.OPENAI, rate=20.0, capacity=20.0)
    assert limiter.get_rate(ProviderType.OPENAI) == 20.0
    
    # Other providers should keep default rate
    assert limiter.get_rate(ProviderType.ANTHROPIC) == 10.0 