"""
Configuration loader for model pricing and limits.
"""

import os
from typing import Dict, Any
import yaml
from pathlib import Path

def load_yaml_config(filename: str) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    config_path = Path(__file__).parent / filename
    
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing configuration file: {e}")

def load_model_configs() -> Dict[str, Any]:
    """Load model configurations from YAML files."""
    # Load both configs
    model_config = load_yaml_config("model_configs.yaml")
    provider_config = load_yaml_config("provider_features.yaml")
    
    # Merge configurations
    merged = {}
    
    # Add providers from both configs
    for provider in set(list(model_config.keys()) + list(provider_config.get("providers", {}).keys())):
        if provider == "system_prompts":
            merged[provider] = model_config.get(provider, {})
            continue
            
        merged[provider] = {
            "models": {},
            "features": provider_config.get("providers", {}).get(provider, {}).get("features", {}),
            "limits": model_config.get(provider, {}).get("limits", {}),
            "prices": model_config.get(provider, {}).get("prices", {})
        }
        
        # Merge models
        provider_models = provider_config.get("providers", {}).get(provider, {}).get("models", {})
        model_config_models = model_config.get(provider, {}).get("models", {})
        
        for model in set(list(provider_models.keys()) + list(model_config_models.keys())):
            merged[provider]["models"][model] = {
                "features": provider_models.get(model, {}).get("features", {}),
                "limits": model_config_models.get(model, {}).get("limits", {}),
                "prices": model_config_models.get(model, {}).get("prices", {})
            }
    
    return merged

def get_provider_config(provider: str) -> Dict[str, Any]:
    """Get configuration for specific provider."""
    configs = load_model_configs()
    if provider not in configs:
        raise ValueError(f"Provider not found in configuration: {provider}")
    return configs[provider]

def get_model_config(provider: str, model: str) -> Dict[str, Any]:
    """Get configuration for specific model."""
    provider_config = get_provider_config(provider)
    if "models" not in provider_config or model not in provider_config["models"]:
        raise ValueError(f"Model {model} not found for provider {provider}")
    return provider_config["models"][model]

def get_model_price(provider: str, model: str) -> Dict[str, float]:
    """Get price information for specific model."""
    model_config = get_model_config(provider, model)
    if "prices" not in model_config:
        raise ValueError(f"Price information not found for model {model}")
    return model_config["prices"]

def get_model_limits(provider: str, model: str) -> Dict[str, int]:
    """Get token limits for specific model."""
    model_config = get_model_config(provider, model)
    if "limits" not in model_config:
        raise ValueError(f"Limit information not found for model {model}")
    return model_config["limits"]

def get_model_features(provider: str, model: str) -> Dict[str, bool]:
    """Get feature support information for specific model."""
    model_config = get_model_config(provider, model)
    if "features" not in model_config:
        raise ValueError(f"Feature information not found for model {model}")
    return model_config["features"]

def get_system_prompts() -> Dict[str, str]:
    """Get default system prompts for different tasks."""
    configs = load_model_configs()
    if "system_prompts" not in configs:
        raise ValueError("System prompts not found in configuration")
    return configs["system_prompts"]

def list_providers() -> list[str]:
    """Get list of all configured providers."""
    configs = load_model_configs()
    return [provider for provider in configs.keys() if provider != "system_prompts"]

def list_models(provider: str) -> list[str]:
    """Get list of all models for specific provider."""
    provider_config = get_provider_config(provider)
    if "models" not in provider_config:
        return []
    return list(provider_config["models"].keys()) 