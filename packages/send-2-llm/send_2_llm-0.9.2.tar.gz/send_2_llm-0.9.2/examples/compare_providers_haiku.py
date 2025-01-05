"""Compare haiku generation across different providers."""

import os
import asyncio
import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from rich.style import Style
import json
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, Any, List

from send_2_llm import (
    LLMRequest,
    ProviderType,
    StrategyType,
    LLMManager,
    ProviderInfo,
    LLMResponse
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "function": "%(funcName)s", "line": %(lineno)d, "message": "%(message)s"}'
)

logger = logging.getLogger(__name__)
console = Console()

# Store results for dashboard
results: Dict[str, Dict[str, Any]] = {}

def datetime_handler(obj):
    """Handle datetime serialization to JSON."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def display_dashboard():
    """Display summary dashboard of all provider results."""
    console.print("\n[bold cyan]== Provider Performance Dashboard ==[/bold cyan]\n")
    
    # Create results table
    table = Table(
        title="Provider Results Summary",
        show_header=True,
        header_style="bold magenta"
    )
    
    # Add columns
    table.add_column("Provider", style="cyan")
    table.add_column("Status", style="bold")
    table.add_column("Model Used")
    table.add_column("Tokens", justify="right")
    table.add_column("Cost ($)", justify="right")
    table.add_column("Latency (s)", justify="right")
    table.add_column("Error")
    
    # Add rows
    for provider, data in results.items():
        status = data.get("status", "UNKNOWN")
        status_style = {
            "SUCCESS": Style(color="green"),
            "ERROR": Style(color="red"),
            "SKIPPED": Style(color="yellow"),
            "TIMEOUT": Style(color="red"),
        }.get(status, Style(color="white"))
        
        table.add_row(
            provider,
            status,
            data.get("model", "N/A"),
            str(data.get("total_tokens", "N/A")),
            f"{data.get('cost', 0.0):.6f}",
            f"{data.get('latency', 0.0):.3f}",
            data.get("error", ""),
            style=status_style
        )
    
    console.print(table)
    
    # Print statistics
    success_count = sum(1 for d in results.values() if d.get("status") == "SUCCESS")
    error_count = sum(1 for d in results.values() if d.get("status") == "ERROR")
    skipped_count = sum(1 for d in results.values() if d.get("status") == "SKIPPED")
    timeout_count = sum(1 for d in results.values() if d.get("status") == "TIMEOUT")
    
    total_tokens = sum(d.get("total_tokens", 0) for d in results.values())
    total_cost = sum(d.get("cost", 0.0) for d in results.values())
    avg_latency = sum(d.get("latency", 0.0) for d in results.values() if d.get("latency")) / success_count if success_count else 0
    
    stats = Table.grid(padding=1)
    stats.add_column(style="bold")
    stats.add_column()
    
    stats.add_row("Total Providers:", str(len(results)))
    stats.add_row("Successful:", f"[green]{success_count}[/green]")
    stats.add_row("Failed:", f"[red]{error_count}[/red]")
    stats.add_row("Skipped:", f"[yellow]{skipped_count}[/yellow]")
    stats.add_row("Timeouts:", f"[red]{timeout_count}[/red]")
    stats.add_row("Total Tokens:", str(total_tokens))
    stats.add_row("Total Cost ($):", f"{total_cost:.6f}")
    stats.add_row("Avg Latency (s):", f"{avg_latency:.3f}")
    
    console.print("\n[bold cyan]Statistics[/bold cyan]")
    console.print(stats)

async def generate_haiku(llm: LLMManager, provider: ProviderInfo) -> None:
    """Generate haiku using specified provider."""
    start_time = datetime.now()
    provider_name = provider.type.value
    
    try:
        # Check if provider's API key is set
        env_var = f"{provider_name.upper()}_API_KEY"
        if not os.getenv(env_var):
            console.print(f"[yellow]Skipping {provider_name} - {env_var} not set[/yellow]")
            results[provider_name] = {
                "status": "SKIPPED",
                "error": f"{env_var} not set"
            }
            return

        # Create request
        request = LLMRequest(
            prompt="Generate a haiku about cherry blossoms",
            provider_type=provider.type,
            strategy=StrategyType.SINGLE,
            temperature=0.4,
            system_prompt_type="haiku"
        )
        
        # Display provider info
        console.print(f"\n[cyan]Trying {provider_name}...[/cyan]")
        
        # Generate haiku with timeout
        try:
            async with asyncio.timeout(30):  # 30 second timeout
                logger.debug(f"Starting request to {provider_name}")
                response = await llm.generate(request)
                logger.debug(f"Got response from {provider_name}")
                
                # Store results
                end_time = datetime.now()
                latency = (end_time - start_time).total_seconds()
                
                results[provider_name] = {
                    "status": "SUCCESS",
                    "model": response.metadata.model,
                    "total_tokens": response.metadata.usage.total_tokens,
                    "cost": response.metadata.usage.cost or 0.0,
                    "latency": latency
                }
                
                # Display result
                console.print(Panel(response.text, title=f"Haiku from {provider_name}"))
                
                # Display metadata
                metadata_json = json.dumps(response.metadata.model_dump(), indent=2, default=datetime_handler)
                console.print(Syntax(metadata_json, "json", theme="monokai", line_numbers=True))
                
        except asyncio.TimeoutError:
            results[provider_name] = {
                "status": "TIMEOUT",
                "error": "Request timed out after 30s"
            }
            console.print(f"[red]Timeout error with {provider_name}[/red]")
            
    except Exception as e:
        logger.exception(f"Error with {provider_name}")
        results[provider_name] = {
            "status": "ERROR",
            "error": str(e)
        }
        console.print(f"[red]Error with {provider_name}: {str(e)}[/red]")

async def main():
    """Run the example."""
    try:
        # Initialize LLM manager
        logger.info("Initializing LLM manager")
        llm = LLMManager()
        
        # Get available providers
        logger.info("Getting available providers")
        providers = llm.get_available_providers()
        logger.info(f"Found {len(providers)} providers")
        
        # Display available providers
        table = Table(title="Available Providers")
        table.add_column("Provider")
        table.add_column("Priority")
        table.add_column("Fallback")
        table.add_column("Description")
        
        for provider in providers:
            logger.debug(f"Adding provider to table: {provider.type.value}")
            table.add_row(
                provider.type.value,
                str(provider.priority),
                "✓" if provider.fallback else "✗",
                provider.description
            )
        
        console.print(table)
        console.print()
        
        # Generate haiku with each provider
        for provider in providers:
            logger.info(f"Processing provider: {provider.type.value}")
            await generate_haiku(llm, provider)
            
        # Display final dashboard
        display_dashboard()
            
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
    except Exception as e:
        logger.exception("Unexpected error")
        console.print(f"[red]Unexpected error: {str(e)}[/red]")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]Program terminated by user[/yellow]")
        # Still show dashboard with partial results
        display_dashboard()
    except Exception as e:
        logger.exception("Fatal error")
        console.print(f"[red]Fatal error: {str(e)}[/red]") 