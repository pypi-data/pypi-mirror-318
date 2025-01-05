"""
Perplexity API provider implementation.
Supports online models, chat models and web search integration.
Now uses OpenAI SDK format for API calls.

Features:
- Online models integration via OpenAI SDK format
- Chat models integration
- Web search integration
- RAG support
- Citations support
- Related questions support
"""

import os
import logging
from typing import Optional, Dict, Any, AsyncGenerator
import aiohttp
from datetime import datetime
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from ..types import (
    LLMRequest,
    LLMResponse,
    LLMMetadata,
    TokenUsage,
    ProviderType,
    ProviderAPIError,
    ErrorDetails
)
from .base import BaseLLMProvider
from ..constants.config_loader import (
    get_provider_config,
    get_model_config,
    get_model_price,
    get_model_limits,
    get_model_features,
    list_models
)

logger = logging.getLogger(__name__)

class PerplexityProvider(BaseLLMProvider):
    """Perplexity API provider implementation using OpenAI SDK format."""
    
    # Default model will be used only if PERPLEXITY_MODEL is not set
    DEFAULT_MODEL = "llama-3.1-sonar-huge-128k-online"
    PRIORITY = 70  # Medium priority
    IS_FALLBACK = False  # Not recommended as fallback due to cost
    
    def __init__(self, model: Optional[str] = None, **kwargs: Any):
        """Initialize Perplexity provider.
        
        Args:
            model: Model name to use (defaults to PERPLEXITY_MODEL env var or DEFAULT_MODEL)
            **kwargs: Additional provider parameters
        """
        super().__init__(provider_type=ProviderType.PERPLEXITY)
        
        # Get API key
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            raise ProviderAPIError(
                "PERPLEXITY_API_KEY environment variable not set",
                provider=self.provider_type,
                error_details=ErrorDetails(
                    error_type="ConfigurationError",
                    message="API key not found",
                    retryable=False
                )
            )
            
        # Initialize OpenAI client with Perplexity base URL
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://api.perplexity.ai"
        )
        
        # Set model with priority:
        # 1. model parameter from constructor
        # 2. PERPLEXITY_MODEL environment variable
        # 3. DEFAULT_MODEL constant
        env_model = os.getenv("PERPLEXITY_MODEL")
        if env_model:
            logger.info(f"Using model from PERPLEXITY_MODEL: {env_model}")
        self.model = model or env_model or self.DEFAULT_MODEL
        
        # Validate model against configuration
        try:
            # Get model configuration to validate
            model_config = get_model_config("perplexity", self.model)
            model_features = get_model_features("perplexity", self.model)
            model_limits = get_model_limits("perplexity", self.model)
            
            # Store model configuration
            self.model_config = model_config
            self.model_features = model_features
            self.model_limits = model_limits
            
            logger.info(f"Loaded configuration for model {self.model}")
            logger.debug(f"Model features: {model_features}")
            logger.debug(f"Model limits: {model_limits}")
            
        except ValueError as e:
            available_models = list_models("perplexity")
            logger.warning(
                f"Model {self.model} not found in configuration. "
                f"Available models: {', '.join(available_models)}"
            )
            raise ProviderAPIError(
                f"Invalid model configuration: {str(e)}",
                provider=self.provider_type,
                error_details=ErrorDetails(
                    error_type="ConfigurationError",
                    message=f"Model {self.model} not found in configuration",
                    retryable=False,
                    recommendations=[
                        f"Use one of the available models: {', '.join(available_models)}",
                        "Check model name for typos",
                        "Update configuration if using a new model"
                    ]
                )
            )
            
    def _calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate cost based on token usage."""
        try:
            # Get price configuration
            prices = get_model_price("perplexity", self.model)
            
            # Calculate costs (prices are per million tokens)
            prompt_cost = (prompt_tokens / 1_000_000) * prices["prompt"]
            completion_cost = (completion_tokens / 1_000_000) * prices["completion"]
            
            return prompt_cost + completion_cost
            
        except Exception as e:
            logger.warning(f"Failed to calculate cost: {str(e)}")
            return 0.0
            
    def _get_generation_config(self, request: LLMRequest) -> Dict[str, Any]:
        """Get generation configuration from request."""
        # Get model limits
        max_tokens = self.model_limits.get("max_total_tokens", 4096)
        max_completion_tokens = self.model_limits.get("max_completion_tokens", 1024)
        
        # Use request values or defaults
        config = {
            "temperature": request.temperature if request.temperature is not None else 0.2,
            "top_p": request.top_p if request.top_p is not None else 0.9,
            "max_tokens": min(
                request.max_tokens if request.max_tokens is not None else max_completion_tokens,
                max_completion_tokens
            ),
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 1
        }
        
        # Add optional search parameters if provided and supported
        if request.extra_params and self.model_features.get("web_search", False):
            for param in ["search_domain_filter", "return_images", 
                         "return_related_questions", "search_recency_filter"]:
                if param in request.extra_params:
                    config[param] = request.extra_params[param]
        
        return config
        
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using Perplexity API via OpenAI SDK format."""
        try:
            # Get system prompt if specified
            system_prompt = None
            if request.system_prompt_type:
                try:
                    system_prompt = self.get_system_prompt(request.system_prompt_type)
                except ValueError as e:
                    logger.warning(f"Could not get system prompt: {e}")
            
            # Prepare messages
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": request.prompt})
            
            # Prepare request data
            config = self._get_generation_config(request)
            
            logger.info(f"Sending request to Perplexity API:")
            logger.info(f"  Model: {self.model}")
            logger.info(f"  Messages: {messages}")
            logger.info(f"  Config: {config}")
            
            start_time = datetime.now()
            
            try:
                # Make API request using OpenAI SDK
                response: ChatCompletion = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    **config
                )
                
                end_time = datetime.now()
                latency = (end_time - start_time).total_seconds()
                
                logger.info(f"Got response from Perplexity API: {response}")
                
                # Extract response
                completion = response.choices[0].message.content
                
                # Extract usage
                usage = response.usage
                prompt_tokens = usage.prompt_tokens
                completion_tokens = usage.completion_tokens
                total_tokens = usage.total_tokens
                
                # Calculate cost
                cost = self._calculate_cost(prompt_tokens, completion_tokens)
                
                # Prepare metadata
                metadata = LLMMetadata(
                    provider=self.provider_type,
                    model=self.model,
                    usage=TokenUsage(
                        prompt_tokens=prompt_tokens,
                        completion_tokens=completion_tokens,
                        total_tokens=total_tokens,
                        cost=cost
                    ),
                    raw_response=response.model_dump(),
                    created_at=end_time,
                    latency=latency
                )
                
                return LLMResponse(
                    text=completion,
                    metadata=metadata
                )
                
            except Exception as e:
                logger.error(f"Error during API request: {str(e)}", exc_info=True)
                raise ProviderAPIError(
                    f"API request failed: {str(e)}",
                    provider=self.provider_type,
                    error_details=ErrorDetails(
                        error_type="APIError",
                        message=str(e),
                        retryable=True
                    )
                )
                
        except Exception as e:
            logger.exception("Error in Perplexity provider")
            raise ProviderAPIError(
                f"Perplexity provider error: {str(e)}",
                provider=self.provider_type,
                error_details=ErrorDetails(
                    error_type="ProviderError",
                    message=str(e),
                    retryable=True
                )
            ) 