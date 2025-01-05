"""Security manager for send_2_llm.

This module handles API key validation, access control, and credential storage.
"""

import os
import logging
from typing import Optional, Dict
from pathlib import Path
from ..types import ProviderType

logger = logging.getLogger(__name__)

class SecurityManager:
    """Manages security aspects of send_2_llm."""
    
    def __init__(self):
        """Initialize security manager."""
        self._provider_keys: Dict[ProviderType, str] = {}
        self._load_api_keys()
    
    def _load_api_keys(self) -> None:
        """Load API keys from environment variables."""
        for provider in ProviderType:
            key_name = f"{provider.value.upper()}_API_KEY"
            if key := os.getenv(key_name):
                self._provider_keys[provider] = key
                logger.debug(f"Loaded API key for {provider.value}")
    
    def validate_api_key(self, provider: ProviderType) -> bool:
        """Validate that API key exists for provider.
        
        Args:
            provider: Provider type to validate key for
            
        Returns:
            bool: True if valid key exists, False otherwise
        """
        key_exists = provider in self._provider_keys
        if not key_exists:
            logger.warning(f"No API key found for provider {provider.value}")
        return key_exists
    
    def get_api_key(self, provider: ProviderType) -> Optional[str]:
        """Get API key for provider if it exists.
        
        Args:
            provider: Provider to get key for
            
        Returns:
            Optional[str]: API key if exists, None otherwise
        """
        return self._provider_keys.get(provider)
    
    def validate_access(self, provider: ProviderType, model: str) -> bool:
        """Validate access to provider and model combination.
        
        Args:
            provider: Provider to validate
            model: Model to validate
            
        Returns:
            bool: True if access is allowed, False otherwise
        """
        # Basic validation - just check API key exists
        # TODO: Add more sophisticated access control
        return self.validate_api_key(provider) 