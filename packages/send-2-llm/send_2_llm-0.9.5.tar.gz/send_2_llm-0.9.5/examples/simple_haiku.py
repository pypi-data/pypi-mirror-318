"""Simple haiku generation example."""

import os
import asyncio
import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
import json
from datetime import datetime
from dotenv import load_dotenv

from send_2_llm import (
    LLMRequest,
    ProviderType,
    StrategyType,
    LLMManager,
    ProviderInfo
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "function": "%(funcName)s", "line": %(lineno)d, "message": "%(message)s"}'
)

console = Console()

def datetime_handler(obj):
    """Handle datetime serialization to JSON."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

async def main():
    """Run the example."""
    # Initialize LLM manager
    llm = LLMManager()
    
    # Get available providers
    providers = llm.get_available_providers()
    
    # Display available providers
    table = Table(title="Available Providers")
    table.add_column("Provider")
    table.add_column("Priority")
    table.add_column("Fallback")
    table.add_column("Description")
    
    for provider in providers:
        table.add_row(
            provider.type.value,
            str(provider.priority),
            "✓" if provider.fallback else "✗",
            provider.description
        )
    
    console.print(table)
    console.print()
    
    # Get provider from environment or use default
    provider = os.getenv("DEFAULT_PROVIDER", "perplexity")
    strategy = os.getenv("STRATEGY", "single")
    
    console.print(f"DEFAULT_PROVIDER from .env: {provider}")
    console.print(f"STRATEGY from .env: {strategy}")
    
    # Create request
    request = LLMRequest(
        prompt="Generate a haiku about cherry blossoms",
        provider_type=ProviderType(provider),
        strategy=StrategyType(strategy),
        temperature=0.4,
        system_prompt_type="haiku"
    )
    
    # Display configuration
    config_panel = Panel(
        f"Provider: {request.provider_type.value}\n"
        f"Model: {os.getenv(f'{provider.upper()}_MODEL', 'default')}\n"
        f"Temperature: {request.temperature}\n"
        f"Strategy: {request.strategy.value.title()} Provider Strategy",
        title="Configuration"
    )
    console.print(config_panel)
    console.print()
    
    console.print("Generating haiku...")
    console.print()
    
    try:
        # Generate haiku
        response = await llm.generate(request)
        
        # Display result
        console.print(Panel(response.text, title="Generated Haiku"))
        console.print()
        
        # Display metadata as formatted JSON
        metadata_json = json.dumps(response.metadata.model_dump(), indent=2, default=datetime_handler)
        console.print(Syntax(metadata_json, "json", theme="monokai", line_numbers=True))
        
    except Exception as e:
        console.print(f"Error: {str(e)}")
        
        # Get provider info
        provider_info = next(
            (p for p in providers if p.type == request.provider_type),
            None
        )
        
        if provider_info:
            console.print("\nProvider Information:")
            console.print(f"Priority: {provider_info.priority}")
            console.print(f"Fallback: {'Yes' if provider_info.fallback else 'No'}")
            console.print(f"Description: {provider_info.description}")

if __name__ == "__main__":
    asyncio.run(main()) 