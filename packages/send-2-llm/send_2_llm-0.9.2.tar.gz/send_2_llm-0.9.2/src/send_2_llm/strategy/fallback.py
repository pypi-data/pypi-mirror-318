"""Fallback strategy implementation."""

from typing import Optional, List, Dict, Any

from ..types import (
    ProviderType,
    ProviderAPIError,
    ErrorDetails,
    StrategyType
)
from .base import BaseStrategy, StrategyContext

class FallbackStrategy(BaseStrategy):
    """Strategy that automatically switches to fallback providers on errors."""
    
    def __init__(self):
        """Initialize fallback strategy."""
        super().__init__(strategy_type=StrategyType.FALLBACK)
    
    async def select_provider(self, context: StrategyContext) -> tuple[ProviderType, Optional[str]]:
        """Select provider with fallback support.
        
        Args:
            context: Strategy execution context
            
        Returns:
            Tuple of (provider_type, model_name)
            
        Raises:
            ProviderAPIError: If no suitable provider found
        """
        request = context.request
        
        # Use provider from request if specified and no errors
        if request.provider and request.provider not in context.error_history:
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
            
        # Get available providers sorted by score
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
            
        # Try each provider in order until one works
        for provider_type, _ in providers:
            # Skip providers with errors
            if provider_type in context.error_history:
                continue
                
            return provider_type, None
            
        # No providers available without errors
        raise ProviderAPIError(
            "All providers have errors",
            error_details=ErrorDetails(
                error_type="AllProvidersError",
                message="All available providers have recent errors",
                retryable=False,
                recommendations=[
                    "Check provider status",
                    "Verify API keys and configuration",
                    "Wait and retry later"
                ]
            )
        )
    
    async def handle_error(
        self,
        error: ProviderAPIError,
        context: StrategyContext
    ) -> tuple[ProviderType, Optional[str]]:
        """Handle provider error by switching to fallback.
        
        Args:
            error: Error that occurred
            context: Strategy execution context
            
        Returns:
            Tuple of (new_provider_type, new_model_name)
            
        Raises:
            ProviderAPIError: If no fallback providers available
        """
        # Add error to history
        provider_type = context.request.provider
        if provider_type:
            if provider_type not in context.error_history:
                context.error_history[provider_type] = []
            context.error_history[provider_type].append(error)
        
        # Check if should retry
        if not self._should_retry(error, context):
            raise error
            
        # Try to find fallback provider
        context.attempt_count += 1
        return await self.select_provider(context) 