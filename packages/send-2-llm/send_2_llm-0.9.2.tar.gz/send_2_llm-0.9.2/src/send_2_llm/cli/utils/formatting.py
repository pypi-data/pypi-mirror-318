"""Formatting utilities for CLI output."""

from typing import Any, Dict, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from ...types import LLMResponse


def format_response(response: LLMResponse, debug: bool = False) -> None:
    """Format and print LLM response.
    
    Args:
        response: Response to format
        debug: Whether to show debug info
    """
    console = Console()
    
    # Print response text
    console.print(Panel(
        response.text,
        title=f"Response from {response.metadata.provider}",
        border_style="blue"
    ))
    
    if debug:
        # Print metadata
        table = Table(title="Response Metadata")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Provider", str(response.metadata.provider))
        table.add_row("Model", response.metadata.model)
        table.add_row("Created At", str(response.metadata.created_at))
        table.add_row("Total Tokens", str(response.metadata.usage.total_tokens))
        table.add_row("Cost", f"${response.metadata.usage.cost:.4f}")
        if response.metadata.latency:
            table.add_row("Latency", f"{response.metadata.latency:.2f}s")
        
        console.print(table)


def format_error(error: Exception, debug: bool = False) -> None:
    """Format and print error message.
    
    Args:
        error: Exception to format
        debug: Whether to show debug info
    """
    console = Console()
    console.print(f"[red]Error: {str(error)}[/red]")
    
    if debug:
        import traceback
        console.print("[yellow]Traceback:[/yellow]")
        console.print(traceback.format_exc())
