"""Configuration management module."""

import os
from typing import Optional, Dict, Any, List
from functools import lru_cache
from dotenv import load_dotenv
import logging

from .types import ProviderType, StrategyType

logger = logging.getLogger(__name__)

class ConfigurationError(Exception):
    """Configuration related errors."""
    pass

def is_development() -> bool:
    """Check if running in development mode."""
    return os.getenv("ENV", "development").lower() == "development"

def _get_env_hash() -> str:
    """Get hash of relevant environment variables for cache key."""
    env_vars = [
        "DEFAULT_PROVIDER",
        "LLM_PROVIDERS",
        "LLM_STRATEGY",
        "MAX_INPUT_TOKENS",
        "MAX_OUTPUT_TOKENS",
        "CONTEXT_WINDOW",
        "TEMPERATURE",
        "TOP_P",
        "OPENAI_MODEL",
        "TOGETHER_MODEL",
        "ANTHROPIC_MODEL",
        "GEMINI_MODEL",
        "DEEPSEEK_MODEL"
    ]
    
    # Создаем копию текущих значений окружения
    env_values = {}
    for var in env_vars:
        if var in os.environ:
            env_values[var] = os.environ[var]
    
    return "|".join(f"{var}={env_values.get(var, '')}" for var in sorted(env_vars))

@lru_cache(maxsize=1)
def load_config_with_cache(env_hash: str, load_env: bool = True) -> Dict[str, Any]:
    """Cached version of config loading for production."""
    # Load .env file if requested
    if load_env:
        load_dotenv()
    
    # Create a copy of the config and environment
    config = dict(_load_config_internal())
    
    # Store a copy of current environment variables
    env_copy = {}
    for var in [
        "DEFAULT_PROVIDER",
        "LLM_PROVIDERS",
        "LLM_STRATEGY",
        "MAX_INPUT_TOKENS",
        "MAX_OUTPUT_TOKENS",
        "CONTEXT_WINDOW",
        "TEMPERATURE",
        "TOP_P",
        "OPENAI_MODEL",
        "TOGETHER_MODEL",
        "ANTHROPIC_MODEL",
        "GEMINI_MODEL",
        "DEEPSEEK_MODEL"
    ]:
        if var in os.environ:
            env_copy[var] = os.environ[var]
    
    # Return config with environment snapshot
    return {"config": config, "env": env_copy}

def load_config_no_cache(load_env: bool = True) -> Dict[str, Any]:
    """Load configuration without caching for development."""
    if load_env:
        load_dotenv()
    return _load_config_internal()

def load_config(load_env: bool = True) -> Dict[str, Any]:
    """Load configuration from environment variables with caching in production."""
    if is_development():
        return load_config_no_cache(load_env)
    
    # Load .env file if requested
    if load_env:
        load_dotenv()
    
    # Get current environment hash
    env_hash = _get_env_hash()
    
    # Get cached config with environment snapshot
    cached = load_config_with_cache(env_hash, load_env=False)
    
    # If environment has changed, reload config
    if any(os.environ.get(var) != cached["env"].get(var) for var in cached["env"]):
        reload_config()
        cached = load_config_with_cache(env_hash, load_env=False)
    
    return cached["config"]

def _load_config_internal() -> Dict[str, Any]:
    """Internal function to load configuration."""
    config = {
        # Provider settings
        "default_provider": _get_provider_from_env(),
        "provider_list": _get_providers_list_from_env(),
        
        # Strategy settings
        "strategy": _get_strategy_from_env(),
        
        # Model settings
        "max_input_tokens": int(os.getenv("MAX_INPUT_TOKENS", "3072")),
        "max_output_tokens": int(os.getenv("MAX_OUTPUT_TOKENS", "1024")),
        "context_window": int(os.getenv("CONTEXT_WINDOW", "4096")),
        
        # Generation settings
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
        "top_p": float(os.getenv("TOP_P", "0.95")),
        
        # Provider-specific settings
        "openai_model": os.getenv("OPENAI_MODEL", "gpt-4o-mini-2024-07-18"),
        "together_model": os.getenv("TOGETHER_MODEL", "meta-llama/Llama-Vision-Free"),
        "anthropic_model": os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307"),
    }
    
    logger.debug(f"Loaded config: {config}")
    return config

def _get_provider_from_env() -> Optional[ProviderType]:
    """Get provider type from environment."""
    provider_name = os.getenv("DEFAULT_PROVIDER", "").lower()
    logger.debug(f"Raw provider name from env: '{provider_name}'")
    
    if not provider_name:
        return None
        
    try:
        return ProviderType(provider_name)
    except ValueError as e:
        raise ConfigurationError(f"Invalid provider type in DEFAULT_PROVIDER: {provider_name}") from e

def _get_providers_list_from_env() -> List[ProviderType]:
    """Get list of providers from environment."""
    providers_str = os.getenv("LLM_PROVIDERS", "").lower()
    if not providers_str:
        return []
        
    providers = []
    for name in providers_str.split(","):
        name = name.strip()
        try:
            providers.append(ProviderType(name))
        except ValueError as e:
            raise ConfigurationError(f"Invalid provider type in LLM_PROVIDERS: {name}") from e
            
    return providers

def _get_strategy_from_env() -> StrategyType:
    """Get strategy type from environment."""
    strategy_name = os.getenv("LLM_STRATEGY", "single").lower()
    try:
        return StrategyType(strategy_name)
    except ValueError as e:
        raise ConfigurationError(f"Invalid strategy type: {strategy_name}") from e

def reload_config() -> None:
    """Clear config cache and force reload."""
    # Clear LRU cache
    load_config_with_cache.cache_clear()
    
    # Force reload .env file
    load_dotenv(override=True)
    
    # Get current environment hash
    env_hash = _get_env_hash()
    
    # Load fresh config
    return load_config_with_cache(env_hash, load_env=False) 