"""Base types for the LLM system."""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

from ..common import (
    ProviderType,
    StrategyType,
    OutputFormat,
    TokenUsage,
    ErrorDetails,
)


class LLMMetadata(BaseModel):
    """LLM response metadata."""
    
    provider: ProviderType = Field(..., description="LLM provider used")
    model: str = Field(..., description="Model name used")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    usage: TokenUsage = Field(default_factory=TokenUsage, description="Token usage info")
    raw_response: Optional[Dict[str, Any]] = Field(None, description="Raw provider response")
    strategy: Optional[StrategyType] = Field(None, description="Strategy used if any")
    latency: Optional[float] = Field(None, description="Request latency in seconds")


class RetryConfig(BaseModel):
    """Retry configuration."""
    max_retries: int = Field(3, description="Maximum number of retries")
    initial_delay: float = Field(1.0, description="Initial delay between retries in seconds")
    exponential_base: float = Field(2.0, description="Base for exponential backoff")
    max_delay: float = Field(60.0, description="Maximum delay between retries in seconds")
    retry_on_errors: List[str] = Field(
        ["RateLimitError", "ServiceUnavailableError", "ConnectionError", "TimeoutError"],
        description="List of error types to retry on"
    )


class LLMRequest(BaseModel):
    """Request to LLM provider."""
    
    prompt: str = Field(..., description="Input prompt")
    provider_type: Optional[ProviderType] = Field(None, description="Specific provider to use")
    model: Optional[str] = Field(None, description="Specific model to use")
    strategy: Optional[StrategyType] = Field(None, description="Strategy to use")
    max_tokens: Optional[int] = Field(None, description="Maximum tokens in response")
    system_prompt_type: Optional[str] = Field(None, description="Type of system prompt to use")
    
    temperature: Optional[float] = Field(None, description="Sampling temperature")
    top_p: Optional[float] = Field(None, description="Nucleus sampling parameter")
    top_k: Optional[int] = Field(None, description="Top-k sampling parameter")
    
    stop: Optional[List[str]] = Field(None, description="Stop sequences")
    response_format: Optional[str] = Field(None, description="Response MIME type")
    token_estimation_ratio: Optional[float] = Field(None, description="Token estimation ratio")
    output_format: Optional[OutputFormat] = Field(default=OutputFormat.RAW, description="Output format type")
    return_json: bool = Field(default=False, description="Whether to return response in JSON format")
    
    retry_config: Optional[RetryConfig] = Field(None, description="Retry configuration")
    extra_params: Optional[Dict[str, Any]] = Field(None, description="Extra provider-specific parameters")


class LLMResponse(BaseModel):
    """Structured response from LLM."""
    
    text: str = Field(..., description="Response text")
    metadata: LLMMetadata = Field(..., description="Response metadata")
    cached: bool = Field(default=False, description="Whether response was cached")
    error_details: Optional[ErrorDetails] = Field(None, description="Error details if any")
    retry_count: Optional[int] = Field(None, description="Number of retries if any") 