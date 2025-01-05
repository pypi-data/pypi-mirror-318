"""Provider factory for creating LLM provider instances."""

import logging
import importlib
import pkgutil
from typing import Dict, Type, Optional, List, Any
from dataclasses import dataclass
import os
from pathlib import Path

from ..types import ProviderType, ProviderAPIError
from .base import BaseLLMProvider
from ..constants.config_loader import list_providers, list_models

logger = logging.getLogger(__name__)

@dataclass
class ProviderInfo:
    """Information about a registered provider."""
    provider_class: Type[BaseLLMProvider]
    priority: int = 0
    is_fallback: bool = False
    description: str = ""
    features: Dict[str, Any] = None
    models: List[str] = None

class ProviderFactory:
    """Factory for creating provider instances with enhanced registration and fallback support."""
    
    def __init__(self):
        """Initialize provider factory with dynamic provider discovery."""
        logger.info("Initializing provider factory")
        self._providers: Dict[ProviderType, ProviderInfo] = {}
        self._discover_providers()
        logger.info(f"Registered {len(self._providers)} providers")

    def _discover_providers(self) -> None:
        """Discover and register available providers."""
        try:
            # Get current directory
            current_dir = Path(__file__).parent
            
            # Scan for provider modules
            for module_info in pkgutil.iter_modules([str(current_dir)]):
                if module_info.name.endswith('_provider'):
                    try:
                        # Import module
                        module = importlib.import_module(f".{module_info.name}", package="send_2_llm.providers")
                        
                        # Look for provider class
                        for attr_name in dir(module):
                            attr = getattr(module, attr_name)
                            if (isinstance(attr, type) and 
                                issubclass(attr, BaseLLMProvider) and 
                                attr != BaseLLMProvider):
                                
                                # Get provider type
                                try:
                                    provider_instance = attr()
                                    provider_type = provider_instance.provider_type
                                    
                                    # Get provider info from config
                                    provider_name = provider_type.value.lower()
                                    models = list_models(provider_name)
                                    
                                    # Register provider
                                    self.register_provider(
                                        provider_type=provider_type,
                                        provider_class=attr,
                                        priority=getattr(attr, 'PRIORITY', 0),
                                        is_fallback=getattr(attr, 'IS_FALLBACK', False),
                                        description=attr.__doc__ or "",
                                        models=models
                                    )
                                    
                                except Exception as e:
                                    logger.warning(
                                        f"Failed to register provider from {attr_name}: {str(e)}"
                                    )
                                    
                    except Exception as e:
                        logger.warning(
                            f"Failed to import provider module {module_info.name}: {str(e)}"
                        )
                        
        except Exception as e:
            logger.error(f"Provider discovery failed: {str(e)}")
            raise ProviderAPIError(
                f"Provider discovery failed: {str(e)}",
                error_details={
                    "error_type": "ProviderDiscoveryError",
                    "message": str(e),
                    "retryable": False,
                    "recommendations": [
                        "Check provider module structure",
                        "Verify provider class implementations",
                        "Check file permissions"
                    ]
                }
            )

    def register_provider(
        self, 
        provider_type: ProviderType, 
        provider_class: Type[BaseLLMProvider],
        priority: int = 0,
        is_fallback: bool = False,
        description: str = "",
        models: List[str] = None,
        features: Dict[str, Any] = None,
        override: bool = False
    ) -> None:
        """Register a new provider or update existing one."""
        try:
            if provider_type in self._providers and not override:
                msg = f"Provider {provider_type.value} already registered"
                logger.error(msg)
                raise ValueError(f"{msg}. Set override=True to replace it.")
                
            # Validate provider class
            if not issubclass(provider_class, BaseLLMProvider):
                msg = f"Provider class must inherit from BaseLLMProvider. Got {provider_class.__name__}"
                logger.error(msg)
                raise ValueError(msg)
                
            # Register provider
            self._providers[provider_type] = ProviderInfo(
                provider_class=provider_class,
                priority=priority,
                is_fallback=is_fallback,
                description=description,
                models=models or [],
                features=features or {}
            )
            
            logger.info(
                f"Successfully registered provider {provider_type.value} "
                f"(priority={priority}, fallback={is_fallback}, models={len(models or [])})"
            )
        except Exception as e:
            logger.error(f"Failed to register provider {provider_type.value}: {str(e)}")
            raise

    def get_provider_info(self, provider_type: ProviderType) -> Optional[ProviderInfo]:
        """Get information about a registered provider."""
        info = self._providers.get(provider_type)
        if info:
            logger.debug(f"Found provider info for {provider_type.value}")
        else:
            logger.debug(f"No provider info found for {provider_type.value}")
        return info
        
    def list_providers(self) -> List[tuple[ProviderType, ProviderInfo]]:
        """Get list of all registered providers sorted by priority."""
        providers = sorted(
            self._providers.items(),
            key=lambda x: x[1].priority,
            reverse=True
        )
        logger.debug(f"Listed {len(providers)} providers")
        return providers
        
    def get_fallback_providers(self) -> List[tuple[ProviderType, ProviderInfo]]:
        """Get list of fallback providers sorted by priority."""
        fallbacks = [
            (pt, pi) for pt, pi in self.list_providers()
            if pi.is_fallback
        ]
        logger.debug(f"Found {len(fallbacks)} fallback providers")
        return fallbacks

    def create_provider(self, provider_type: ProviderType, **kwargs) -> BaseLLMProvider:
        """Create provider instance with enhanced error handling."""
        try:
            if provider_type not in self._providers:
                available = ", ".join(p.value for p in self._providers.keys())
                msg = f"Provider {provider_type.value} not registered. Available: {available}"
                logger.error(msg)
                raise ValueError(msg)
                
            provider_info = self._providers[provider_type]
            provider_class = provider_info.provider_class
            
            logger.info(f"Creating instance of {provider_class.__name__}")
            provider = provider_class(**kwargs)
            
            # Validate provider type matches
            if provider.provider_type != provider_type:
                msg = (f"Provider type mismatch. Expected {provider_type.value}, "
                      f"got {provider.provider_type.value}")
                logger.error(msg)
                raise ValueError(msg)
                
            logger.info(f"Successfully created provider instance for {provider_type.value}")
            return provider
            
        except Exception as e:
            logger.error(f"Failed to create provider {provider_type.value}: {str(e)}")
            raise ProviderAPIError(
                f"Failed to create provider {provider_type.value}: {str(e)}",
                provider=provider_type,
                error_details={
                    "error_type": "ProviderCreationError",
                    "message": str(e),
                    "retryable": True,
                    "recommendations": [
                        "Check provider configuration",
                        "Verify API keys are set",
                        "Check network connectivity"
                    ]
                }
            ) 