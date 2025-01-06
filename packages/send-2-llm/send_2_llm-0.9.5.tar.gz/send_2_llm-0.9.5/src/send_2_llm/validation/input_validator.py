"""Input validation for send_2_llm.

This module handles validation and sanitization of prompts and parameters.
"""

import logging
from typing import Optional, Dict, Any
from ..types import ProviderType

logger = logging.getLogger(__name__)

class InputValidator:
    """Validates and sanitizes input data."""
    
    def __init__(self):
        """Initialize input validator."""
        self._max_prompt_length = 32768  # Default max prompt length
        
    def validate_prompt(self, prompt: str) -> bool:
        """Validate prompt text.
        
        Args:
            prompt: The prompt text to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not prompt or not isinstance(prompt, str):
            logger.warning("Prompt must be a non-empty string")
            return False
            
        if len(prompt) > self._max_prompt_length:
            logger.warning(f"Prompt exceeds maximum length of {self._max_prompt_length}")
            return False
            
        return True
        
    def sanitize_prompt(self, prompt: str) -> str:
        """Sanitize prompt text.
        
        Args:
            prompt: The prompt text to sanitize
            
        Returns:
            str: Sanitized prompt text
        """
        # Remove null bytes and replace with space
        prompt = prompt.replace('\x00', ' ')
        
        # Normalize whitespace
        prompt = ' '.join(prompt.split())
        
        return prompt
        
    def validate_parameters(
        self,
        provider: ProviderType,
        model: str,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ) -> bool:
        """Validate generation parameters.
        
        Args:
            provider: The provider to validate parameters for
            model: The model name
            temperature: Temperature parameter (0-2)
            top_p: Top-p parameter (0-1)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional provider-specific parameters
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not model:
            logger.warning("Model name must be specified")
            return False
            
        if temperature is not None and not 0 <= temperature <= 2:
            logger.warning("Temperature must be between 0 and 2")
            return False
            
        if top_p is not None and not 0 <= top_p <= 1:
            logger.warning("Top-p must be between 0 and 1")
            return False
            
        if max_tokens is not None and max_tokens <= 0:
            logger.warning("Max tokens must be positive")
            return False
            
        return True 