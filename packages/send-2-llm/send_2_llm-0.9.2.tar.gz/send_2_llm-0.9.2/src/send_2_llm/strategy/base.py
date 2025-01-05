"""Base strategy interface for provider selection and error handling."""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

from ..types import (
    ProviderType,
    LLMRequest,
    LLMResponse,
    ProviderAPIError,
    ErrorDetails,
    StrategyType
)
from ..providers.factory import ProviderFactory, ProviderInfo

@dataclass
class StrategyContext:
    """Context information for strategy execution."""
    request: LLMRequest
    factory: ProviderFactory
    error_history: Dict[ProviderType, List[ProviderAPIError]] = None
    attempt_count: int = 0
    max_attempts: int = 3
    
    def __post_init__(self):
        """Initialize error history if not provided."""
        if self.error_history is None:
            self.error_history = {}

class BaseStrategy(ABC):
    """Base class for provider selection strategies."""
    
    def __init__(self, strategy_type: StrategyType):
        """Initialize strategy.
        
        Args:
            strategy_type: Type of strategy
        """
        self.strategy_type = strategy_type
    
    @abstractmethod
    async def select_provider(self, context: StrategyContext) -> tuple[ProviderType, Optional[str]]:
        """Select provider and model for the request.
        
        Args:
            context: Strategy execution context
            
        Returns:
            Tuple of (provider_type, model_name)
            
        Raises:
            ProviderAPIError: If no suitable provider found
        """
        pass
    
    @abstractmethod
    async def handle_error(
        self,
        error: ProviderAPIError,
        context: StrategyContext
    ) -> tuple[ProviderType, Optional[str]]:
        """Handle provider error and select alternative if available.
        
        Args:
            error: Error that occurred
            context: Strategy execution context
            
        Returns:
            Tuple of (new_provider_type, new_model_name)
            
        Raises:
            ProviderAPIError: If no alternative provider available
        """
        pass
    
    def _get_provider_score(self, provider_info: ProviderInfo, context: StrategyContext) -> float:
        """Calculate provider score based on priority and error history.
        
        Args:
            provider_info: Provider information
            context: Strategy execution context
            
        Returns:
            Provider score (higher is better)
        """
        # Start with base priority
        score = float(provider_info.priority)
        
        # Reduce score based on recent errors
        provider_errors = context.error_history.get(provider_info.provider_type, [])
        error_penalty = len(provider_errors) * 10.0
        
        return max(0.0, score - error_penalty)
    
    def _get_sorted_providers(
        self,
        context: StrategyContext,
        fallback_only: bool = False
    ) -> List[tuple[ProviderType, ProviderInfo]]:
        """Get list of providers sorted by score.
        
        Args:
            context: Strategy execution context
            fallback_only: Whether to return only fallback providers
            
        Returns:
            List of (provider_type, provider_info) tuples sorted by score
        """
        # Get providers
        providers = (
            context.factory.get_fallback_providers()
            if fallback_only
            else context.factory.list_providers()
        )
        
        # Sort by score
        return sorted(
            providers,
            key=lambda x: self._get_provider_score(x[1], context),
            reverse=True
        )
    
    def _should_retry(self, error: ProviderAPIError, context: StrategyContext) -> bool:
        """Check if request should be retried with different provider.
        
        Args:
            error: Error that occurred
            context: Strategy execution context
            
        Returns:
            True if should retry, False otherwise
        """
        # Don't retry if max attempts reached
        if context.attempt_count >= context.max_attempts:
            return False
            
        # Don't retry if error is not retryable
        if error.error_details and not error.error_details.retryable:
            return False
            
        return True 