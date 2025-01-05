"""
LLM Manager - main interface for send_2_llm library.
Provides centralized management of all components.
"""

import logging
from typing import Optional, Dict, Any

from .types import ProviderType, LLMRequest, LLMResponse
from .security.manager import SecurityManager
from .validation.input_validator import InputValidator
from .stability.circuit_breaker import CircuitBreaker
from .stability.rate_limiter import RateLimiter
from .monitoring.metrics import Monitoring
from .providers.factory import ProviderFactory

logger = logging.getLogger(__name__)

class LLMManager:
    """Main interface for managing LLM operations."""
    
    def __init__(self):
        """Initialize LLM Manager with all required components."""
        self.security = SecurityManager()
        self.validator = InputValidator()
        self.circuit_breaker = CircuitBreaker()
        self.rate_limiter = RateLimiter()
        self.monitoring = Monitoring()
        self.provider_factory = ProviderFactory()
        
    async def generate(
        self,
        prompt: str,
        provider: ProviderType,
        model: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
        extra_params: Optional[Dict[str, Any]] = None
    ) -> LLMResponse:
        """
        Generate response using specified provider with all safety checks.
        
        Args:
            prompt: Input prompt
            provider: Provider type
            model: Model name
            temperature: Generation temperature
            max_tokens: Maximum tokens to generate
            top_p: Top-p sampling parameter
            extra_params: Additional provider-specific parameters
            
        Returns:
            LLMResponse object containing generated text and metadata
            
        Raises:
            SecurityError: If access is denied
            ValidationError: If input validation fails
            ProviderError: If provider is unavailable
            RateLimitError: If rate limit is exceeded
        """
        # Validate security access
        if not self.security.validate_access(provider, model):
            raise SecurityError(f"Access denied for {provider.value} with model {model}")
            
        # Validate input parameters
        self.validator.validate_prompt(prompt)
        self.validator.validate_parameters(
            provider=provider,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )
        
        # Check circuit breaker
        if not self.circuit_breaker.is_available(provider):
            raise ProviderError(f"Provider {provider.value} is currently unavailable")
            
        # Check rate limit
        await self.rate_limiter.acquire(provider)
        
        try:
            # Get provider instance
            provider_instance = self.provider_factory.create_provider(
                provider,
                model=model
            )
            
            # Start monitoring
            with self.monitoring.track_request(provider, model):
                # Create request
                request = LLMRequest(
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p,
                    extra_params=extra_params
                )
                
                # Generate response
                response = await provider_instance._generate(request)
                
                # Record success
                self.circuit_breaker.record_success(provider)
                
                return response
                
        except Exception as e:
            # Record failure
            self.circuit_breaker.record_error(provider)
            # Re-raise with context
            raise ProviderError(f"Generation failed: {str(e)}")
            
    async def list_models(self, provider: ProviderType) -> list[str]:
        """List available models for specified provider."""
        if not self.security.validate_api_key(provider):
            raise SecurityError(f"No valid API key for {provider.value}")
            
        provider_instance = self.provider_factory.create_provider(provider)
        return await provider_instance.list_models() 