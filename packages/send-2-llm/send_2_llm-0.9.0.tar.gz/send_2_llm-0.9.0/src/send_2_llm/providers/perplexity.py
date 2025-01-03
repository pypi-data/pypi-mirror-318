"""
Perplexity API provider implementation.
Supports online models, chat models and web search integration.

Features:
- Online models integration
- Chat models integration
- Web search integration
- RAG support
- Citations support
- Related questions support
"""

import os
import json
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime
import aiohttp

from ..types import (
    ProviderType,
    LLMRequest,
    PerplexityResponse,
    PerplexityMetadata,
    Citation,
    TokenUsage,
    ProviderAPIError,
    StrategyType
)
from .base import BaseLLMProvider

# Настройка логирования
logger = logging.getLogger(__name__)
if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

class PerplexityProvider(BaseLLMProvider):
    """Perplexity API provider implementation."""
    
    def __init__(self):
        """Initialize Perplexity provider."""
        super().__init__()
        self.provider_type = ProviderType.PERPLEXITY
        self.default_model = os.getenv("PERPLEXITY_MODEL", "llama-3.1-sonar-huge-128k-online")
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        self.api_base = "https://api.perplexity.ai/chat/completions"
        
        if not self.api_key:
            raise ProviderAPIError("PERPLEXITY_API_KEY environment variable not set")
            
    def _get_provider_type(self) -> ProviderType:
        """Get provider type."""
        return ProviderType.PERPLEXITY
        
    async def _generate(self, request: LLMRequest) -> PerplexityResponse:
        """Generate text using Perplexity API."""
        try:
            start_time = datetime.now()
            
            # Get extra parameters
            extra_params = request.extra_params or {}
            system_prompt = extra_params.pop("system_prompt", None)
            web_search = extra_params.pop("web_search", False)
            return_citations = extra_params.pop("return_citations", False)
            return_related_questions = extra_params.pop("return_related_questions", False)
            search_domain_filter = extra_params.pop("search_domain_filter", None)
            
            # Prepare messages
            messages = []
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            messages.append({
                "role": "user",
                "content": request.prompt
            })
            
            # Prepare request payload
            payload = {
                "model": request.model or self.default_model,
                "messages": messages,
                "max_tokens": request.max_tokens,
                "temperature": request.temperature,
                "top_p": request.top_p,
                "web_search": web_search,
                "return_citations": return_citations,
                "return_related_questions": return_related_questions
            }
            
            if search_domain_filter:
                payload["search_domain_filter"] = search_domain_filter
            
            # Add remaining extra parameters
            payload.update(extra_params)
            
            # Make API call
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.api_base,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json=payload
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise ProviderAPIError(f"Perplexity API error: {error_text}")
                    
                    result = await response.json()
            
            end_time = datetime.now()
            latency = (end_time - start_time).total_seconds()
            
            # Extract response text
            text = result["choices"][0]["message"]["content"]
            
            # Extract citations if available
            citations = self._extract_citations(result) if return_citations else []
            
            # Extract related questions if available
            related_questions = self._extract_related_questions(result) if return_related_questions else []
            
            # Create token usage info
            token_usage = TokenUsage(
                prompt_tokens=result["usage"]["prompt_tokens"],
                completion_tokens=result["usage"]["completion_tokens"],
                total_tokens=result["usage"]["total_tokens"]
            )
            
            # Create metadata
            metadata = PerplexityMetadata(
                provider=ProviderType.PERPLEXITY,
                strategy=StrategyType.SINGLE,
                model=result["model"],
                created=result["created"],
                usage=token_usage,
                citations=citations,
                raw_response=result,
                finish_reason=result["choices"][0].get("finish_reason"),
                latency=latency,
                related_questions=related_questions,
                images=[]
            )
            
            return PerplexityResponse(
                text=text,
                metadata=metadata
            )
            
        except Exception as e:
            raise ProviderAPIError(f"Perplexity API error: {str(e)}")
            
    def validate_request(self, request: LLMRequest) -> None:
        """Validate request parameters."""
        if not request.prompt:
            raise ValueError("Prompt is required")
            
    def _extract_citations(self, result: Dict[str, Any]) -> List[Citation]:
        """Extract citations from API response."""
        citations = []
        if "citations" in result:
            for citation in result["citations"]:
                citations.append(Citation(
                    title=citation.get("title", ""),
                    url=citation.get("url", ""),
                    text=citation.get("text", "")
                ))
        return citations
        
    def _extract_related_questions(self, result: Dict[str, Any]) -> List[str]:
        """Extract related questions from API response."""
        if "related_questions" in result:
            return result["related_questions"]
        return [] 