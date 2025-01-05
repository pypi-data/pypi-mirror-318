"""
Configuration management system for send_2_llm.
Handles loading, validation, and runtime updates of configurations.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from pydantic import BaseModel, Field

class PriceConfig(BaseModel):
    """Price configuration for a model"""
    prompt: float = Field(..., description="Price per million input tokens")
    completion: float = Field(..., description="Price per million output tokens")
    prompt_cache_hit: Optional[float] = Field(None, description="Price per million cached input tokens")
    prompt_cache_write: Optional[float] = Field(None, description="Price per million tokens for cache writing")
    prompt_cache_read: Optional[float] = Field(None, description="Price per million tokens for cache reading")

class ModelConfig(BaseModel):
    """Configuration for a specific model"""
    prices: PriceConfig
    limits: Dict[str, int]
    features: Dict[str, bool]

class ProviderConfig(BaseModel):
    """Configuration for a provider"""
    models: Dict[str, ModelConfig]

class ConfigManager:
    """Manages configuration loading and access"""
    
    def __init__(self, config_dir: Optional[str] = None):
        """Initialize the configuration manager"""
        if config_dir is None:
            config_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_dir = Path(config_dir)
        self.configs: Dict[str, Any] = {}
        self._load_configs()

    def _load_configs(self) -> None:
        """Load all configuration files"""
        config_files = {
            'pricing': 'model_pricing.yaml',
            'features': 'provider_features.yaml',
            'prompts': 'system_prompts.yaml',
            'defaults': 'defaults.yaml'
        }
        
        for key, filename in config_files.items():
            path = self.config_dir / filename
            if path.exists():
                with open(path, 'r') as f:
                    self.configs[key] = yaml.safe_load(f)

    def get_model_price(self, provider: str, source: str, model: str) -> PriceConfig:
        """Get pricing for a specific model from a specific provider and source"""
        try:
            config = self.configs['pricing']['providers'][source][provider]['models'][model]
            return PriceConfig(**config['prices'])
        except KeyError:
            raise ValueError(f"No pricing found for {provider}/{model} via {source}")

    def get_model_features(self, provider: str, model: str) -> Dict[str, bool]:
        """Get features for a specific model"""
        try:
            return self.configs['features']['providers'][provider]['models'][model]['features']
        except KeyError:
            raise ValueError(f"No features found for {provider}/{model}")

    def get_system_prompt(self, prompt_type: str) -> str:
        """Get a system prompt by type"""
        try:
            return self.configs['prompts']['system_prompts'][prompt_type]
        except KeyError:
            raise ValueError(f"No system prompt found for type: {prompt_type}")

    def get_default_config(self, config_path: str) -> Any:
        """Get a default configuration value by path (e.g., 'rate_limits.rpm')"""
        try:
            value = self.configs['defaults']
            for key in config_path.split('.'):
                value = value[key]
            return value
        except KeyError:
            raise ValueError(f"No default config found for path: {config_path}")

    def reload_configs(self) -> None:
        """Reload all configuration files"""
        self._load_configs()

# Create a global instance
config_manager = ConfigManager() 