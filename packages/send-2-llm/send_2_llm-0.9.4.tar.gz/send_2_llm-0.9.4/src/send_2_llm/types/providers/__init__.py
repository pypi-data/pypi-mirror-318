"""Provider-specific types for the LLM system."""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

from ..base import ProviderType, StrategyType, TokenUsage, LLMResponse


class Citation(BaseModel):
    """Citation information from Perplexity API."""
    
    url: str = Field(..., description="Source URL")
    text: str = Field(..., description="Cited text")
    title: Optional[str] = Field(None, description="Source title")
    published_date: Optional[datetime] = Field(None, description="Publication date")


class PerplexityMetadata(BaseModel):
    """Metadata from Perplexity API response."""
    
    provider: ProviderType = ProviderType.PERPLEXITY
    strategy: StrategyType = StrategyType.SINGLE
    model: str
    created: int
    usage: TokenUsage
    citations: List[Citation] = []
    raw_response: Dict[str, Any]
    finish_reason: Optional[str] = None
    latency: float = 0.0
    related_questions: List[str] = []
    images: List[str] = []


class PerplexityResponse(LLMResponse):
    """Extended response for Perplexity provider."""
    
    metadata: PerplexityMetadata = Field(..., description="Perplexity-specific metadata") 