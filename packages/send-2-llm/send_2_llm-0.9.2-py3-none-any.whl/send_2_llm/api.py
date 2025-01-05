"""Public API for send_2_llm module."""

from typing import Optional, Any, Dict, List
from .client import LLMClient
from .types import (
    LLMRequest,
    LLMResponse,
    ProviderType,
    StrategyType
)


async def generate(
    request: LLMRequest,
    strategy_type: Optional[StrategyType] = None,
    **kwargs: Any
) -> LLMResponse:
    """Generate response using specified provider and strategy.
    
    Args:
        request: The request containing prompt and parameters
        strategy_type: Optional strategy type to use
        **kwargs: Additional arguments passed to LLMClient
        
    Returns:
        LLMResponse containing generated text and metadata
    """
    client = LLMClient(
        strategy_type=strategy_type,
        provider_type=request.provider_type,
        **kwargs
    )
    return await client.generate(
        prompt=request.prompt,
        provider_type=request.provider_type,
        model=request.model,
        **{k: v for k, v in request.dict().items() if k not in ['prompt', 'provider_type', 'model']}
    ) 