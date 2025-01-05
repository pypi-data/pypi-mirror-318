"""LLM Manager for handling providers and requests."""

import logging
from typing import List, Optional
from dataclasses import dataclass

from ..types import (
    LLMRequest,
    LLMResponse,
    ProviderType,
    ProviderNotAvailableError
)
from .factory import ProviderFactory

logger = logging.getLogger(__name__)

@dataclass
class ProviderInfo:
    """Provider information."""
    type: ProviderType
    priority: int
    fallback: bool
    description: str

class LLMManager:
    """Manager for LLM providers."""
    
    def __init__(self):
        """Initialize LLM manager."""
        logger.info("Initializing LLM manager")
        self.factory = ProviderFactory()
    
    def get_available_providers(self) -> List[ProviderInfo]:
        """Get list of available providers with their info."""
        logger.info("Getting available providers")
        providers = []
        for provider_type, info in self.factory.list_providers():
            logger.debug(f"Found provider: {provider_type.value} (priority={info.priority})")
            providers.append(ProviderInfo(
                type=provider_type,
                priority=info.priority,
                fallback=info.is_fallback,
                description=info.description
            ))
        providers = sorted(providers, key=lambda x: x.priority, reverse=True)
        logger.info(f"Found {len(providers)} available providers")
        return providers
    
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using specified provider and strategy."""
        try:
            logger.info(f"Creating provider instance for {request.provider_type.value}")
            provider = self.factory.create_provider(
                request.provider_type,
                model=request.model
            )
            logger.info(f"Generating response with {request.provider_type.value}")
            return await provider.generate(request)
        except Exception as e:
            logger.error(f"Provider {request.provider_type.value} failed: {str(e)}")
            raise ProviderNotAvailableError(
                f"Provider {request.provider_type.value} not available: {str(e)}",
                provider=request.provider_type
            ) 