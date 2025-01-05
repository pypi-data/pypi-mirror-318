"""Configuration utilities for CLI."""

import os
from typing import Dict, Optional
from rich.console import Console
from rich.table import Table

from ...types import ProviderType


def load_env_config() -> Dict[str, Dict[str, str]]:
    """Load configuration from environment variables.
    
    Returns:
        Dictionary of provider configurations
    """
    config = {}
    
    for provider in ProviderType:
        provider_name = provider.value
        provider_config = {
            'api_key': os.getenv(f"{provider_name.upper()}_API_KEY"),
            'model': os.getenv(f"{provider_name.upper()}_MODEL"),
            'is_default': os.getenv('DEFAULT_PROVIDER') == provider_name
        }
        config[provider_name] = provider_config
    
    return config


def print_config(debug: bool = False) -> None:
    """Print current configuration.
    
    Args:
        debug: Whether to show sensitive info
    """
    console = Console()
    config = load_env_config()
    
    table = Table(title="Provider Configuration")
    table.add_column("Provider", style="cyan")
    table.add_column("Model", style="green")
    table.add_column("API Key", style="yellow")
    table.add_column("Default", style="blue")
    
    for provider, cfg in config.items():
        api_key = cfg['api_key']
        if api_key and not debug:
            api_key = f"{api_key[:4]}...{api_key[-4:]}"
        
        table.add_row(
            provider,
            cfg['model'] or "[red]Not Set[/red]",
            api_key or "[red]Not Set[/red]",
            "✓" if cfg['is_default'] else ""
        )
    
    console.print(table)
