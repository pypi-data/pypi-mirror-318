"""Gemini provider implementation."""

import os
import logging
from typing import Optional, Dict, Any
from datetime import datetime
import google.generativeai as genai
from google.generativeai.types import BlockedPromptException

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

logger = logging.getLogger(__name__)

class GeminiProvider(BaseLLMProvider):
    """Provider for Google's Gemini models."""
    
    DEFAULT_MODEL = "gemini-pro"
    PRIORITY = 50  # Lower priority
    IS_FALLBACK = True  # Can be used as fallback
    
    def __init__(self, model: Optional[str] = None, **kwargs: Any):
        """Initialize Gemini provider.
        
        Args:
            model: Model name to use (defaults to GEMINI_MODEL env var or DEFAULT_MODEL)
            **kwargs: Additional provider parameters
        """
        super().__init__(provider_type=ProviderType.GEMINI)
        
        # Get API key
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ProviderAPIError("GEMINI_API_KEY not found in environment variables")
            
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Set model with priority:
        # 1. model parameter from constructor
        # 2. GEMINI_MODEL environment variable
        # 3. DEFAULT_MODEL constant
        env_model = os.getenv("GEMINI_MODEL")
        if env_model:
            logger.info(f"Using model from GEMINI_MODEL: {env_model}")
        self.model = model or env_model or self.DEFAULT_MODEL
        
        if self.model == self.DEFAULT_MODEL:
            logger.warning(
                f"Using default model {self.DEFAULT_MODEL}. "
                "Consider setting GEMINI_MODEL environment variable."
            )
        
    def _get_generation_config(self, request: LLMRequest) -> Dict[str, Any]:
        """Get generation configuration from request."""
        config = {
            "temperature": request.temperature if request.temperature is not None else 1.0,
            "top_p": request.top_p if request.top_p is not None else 0.95,
            "top_k": request.top_k if request.top_k is not None else 40,
            "max_output_tokens": request.max_tokens if request.max_tokens is not None else 8192,
            "response_mime_type": request.response_format if request.response_format else "text/plain"
        }
        return config
        
    async def _generate(self, request: LLMRequest) -> LLMResponse:
        """Generate response using Gemini model."""
        try:
            # Use model from request, instance, or default
            model_name = request.model or self.model
            generation_config = self._get_generation_config(request)
            
            # Create model instance
            model = genai.GenerativeModel(
                model_name=model_name,
                generation_config=generation_config
            )
            
            # Generate response
            response = await model.generate_content_async(request.prompt)
            
            # Check if response was blocked
            if response.prompt_feedback.block_reason:
                error_details = ErrorDetails(
                    error_type="BlockedPromptError",
                    message=f"Content blocked: {response.prompt_feedback.block_reason}",
                    retryable=False
                )
                raise ProviderAPIError("Content blocked by safety filters", error_details=error_details)
            
            # Create metadata
            metadata = LLMMetadata(
                provider=ProviderType.GEMINI,
                model=model_name,
                usage=TokenUsage(
                    prompt_tokens=0,  # TODO: Implement token counting
                    completion_tokens=0,
                    total_tokens=0
                ),
                raw_response={
                    "generation_config": generation_config,
                    "response_type": response.prompt_feedback.block_reason if hasattr(response, 'prompt_feedback') else None
                }
            )
            
            return LLMResponse(
                text=response.text,
                metadata=metadata
            )
            
        except BlockedPromptException as e:
            error_details = ErrorDetails(
                error_type="BlockedPromptError",
                message=str(e),
                retryable=False
            )
            raise ProviderAPIError(f"Content blocked by safety filters: {e}", error_details=error_details)
            
        except Exception as e:
            error_details = ErrorDetails(
                error_type="ProviderError",
                message=str(e),
                retryable=True
            )
            raise ProviderAPIError(f"Gemini API error: {e}", error_details=error_details) 