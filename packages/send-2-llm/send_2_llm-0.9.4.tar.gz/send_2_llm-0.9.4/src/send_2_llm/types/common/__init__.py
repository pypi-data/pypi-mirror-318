"""Common types shared across the system."""

from enum import Enum
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class ProviderType(str, Enum):
    """Types of LLM providers."""
    
    OPENAI = "openai"  # !!! STABLE - DO NOT MODIFY !!!
    TOGETHER = "together"
    ANTHROPIC = "anthropic"
    PERPLEXITY = "perplexity"
    DEEPSEEK = "deepseek"
    GEMINI = "gemini"


class StrategyType(str, Enum):
    """Types of LLM strategies."""
    
    SINGLE = "single"  # Single provider
    FALLBACK = "fallback"  # Try providers in sequence
    PARALLEL = "parallel"  # Run multiple providers in parallel
    COST_OPTIMIZED = "cost_optimized"  # Choose based on cost
    PERFORMANCE = "performance"  # Choose based on performance
    SMART = "smart"  # Smart provider selection


class OutputFormat(str, Enum):
    """Output format types for LLM responses."""
    
    RAW = "raw"  # Raw provider output without modifications
    TEXT = "text"  # Clean text with normalized whitespace (default)
    json = "json"  # Structured JSON response
    TELEGRAM_MARKDOWN = "telegram_markdown"  # Telegram-specific markdown


class TokenUsage(BaseModel):
    """Information about token usage."""
    
    prompt_tokens: int = Field(default=0, description="Number of tokens in prompt")
    completion_tokens: int = Field(default=0, description="Number of tokens in completion")
    total_tokens: int = Field(default=0, description="Total number of tokens")
    cost: float = Field(default=0.0, description="Request cost in USD")


class ErrorDetails(BaseModel):
    """Error details."""
    error_type: str = Field(..., description="Type of error")
    message: str = Field(..., description="Error message")
    retryable: bool = Field(default=False, description="Whether error is retryable")
    retry_after: Optional[float] = Field(None, description="Suggested retry delay in seconds") 