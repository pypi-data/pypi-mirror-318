"""Single provider strategy implementation."""

from typing import Optional, List, Dict, Any

from ..types import (
    ProviderType,
    ProviderAPIError,
    ErrorDetails,
    StrategyType
)
from .base import BaseStrategy, StrategyContext

class SingleProviderStrategy(BaseStrategy):
    """Strategy that uses a single provider with no fallback."""
    
    def __init__(self):
        """Initialize single provider strategy."""
        super().__init__(strategy_type=StrategyType.SINGLE)
    
    async def select_provider(self, context: StrategyContext) -> tuple[ProviderType, Optional[str]]:
        """Select provider based on request parameters.
        
        Args:
            context: Strategy execution context
            
        Returns:
            Tuple of (provider_type, model_name)
            
        Raises:
            ProviderAPIError: If provider not found or invalid
        """
        request = context.request
        
        # Use provider from request if specified
        if request.provider:
            provider_type = request.provider
            model = request.model
            
            # Validate provider exists
            provider_info = context.factory.get_provider_info(provider_type)
            if not provider_info:
                available = ", ".join(p.value for p in context.factory._providers.keys())
                raise ProviderAPIError(
                    f"Provider {provider_type.value} not found. "
                    f"Available providers: {available}",
                    error_details=ErrorDetails(
                        error_type="ProviderNotFound",
                        message=f"Provider {provider_type.value} not found",
                        retryable=False,
                        recommendations=[
                            f"Use one of the available providers: {available}",
                            "Check provider name spelling",
                            "Ensure provider is properly registered"
                        ]
                    )
                )
            
            return provider_type, model
            
        # Get highest priority provider if none specified
        providers = self._get_sorted_providers(context)
        if not providers:
            raise ProviderAPIError(
                "No providers available",
                error_details=ErrorDetails(
                    error_type="NoProvidersAvailable",
                    message="No providers registered in factory",
                    retryable=False,
                    recommendations=[
                        "Register at least one provider",
                        "Check provider registration"
                    ]
                )
            )
            
        provider_type, _ = providers[0]
        return provider_type, None
    
    async def handle_error(
        self,
        error: ProviderAPIError,
        context: StrategyContext
    ) -> tuple[ProviderType, Optional[str]]:
        """Handle provider error.
        
        Args:
            error: Error that occurred
            context: Strategy execution context
            
        Returns:
            Tuple of (provider_type, model_name)
            
        Raises:
            ProviderAPIError: Always raises original error since no fallback
        """
        # Add error to history
        provider_type = context.request.provider
        if provider_type:
            if provider_type not in context.error_history:
                context.error_history[provider_type] = []
            context.error_history[provider_type].append(error)
        
        # Single provider strategy doesn't handle errors
        raise error 