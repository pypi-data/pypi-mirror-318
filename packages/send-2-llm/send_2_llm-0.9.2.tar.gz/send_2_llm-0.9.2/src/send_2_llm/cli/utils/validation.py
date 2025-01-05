"""Validation utilities for CLI."""

import os
from typing import Optional, Tuple
from rich.console import Console

from ...types import ProviderType


def get_provider_config(provider: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
    """Get provider configuration from environment.
    
    Args:
        provider: Provider name to check
        
    Returns:
        Tuple of (provider_name, model_name) or (None, None) if invalid
    """
    console = Console()
    
    # Get provider
    if not provider:
        provider = os.getenv('DEFAULT_PROVIDER')
        if not provider:
            return None, None
    
    # Validate provider
    try:
        ProviderType(provider)
    except ValueError:
        console.print(f"[yellow]Warning: Provider {provider} not supported[/yellow]")
        return None, None
    
    # Check API key
    api_key = os.getenv(f"{provider.upper()}_API_KEY")
    if not api_key:
        console.print(f"[yellow]Warning: No API key found for {provider}[/yellow]")
        return None, None
    
    # Get model
    model = os.getenv(f"{provider.upper()}_MODEL")
    if not model:
        console.print(f"[yellow]Warning: No model configured for {provider}[/yellow]")
    
    return provider, model


def validate_required_text(text: Optional[str], interactive: bool = False) -> bool:
    """Validate that text is provided when not in interactive mode.
    
    Args:
        text: Text to validate
        interactive: Whether in interactive mode
        
    Returns:
        True if valid, False otherwise
    """
    if not text and not interactive:
        Console().print("[red]Error: Please provide text or use --interactive mode[/red]")
        return False
    return True
