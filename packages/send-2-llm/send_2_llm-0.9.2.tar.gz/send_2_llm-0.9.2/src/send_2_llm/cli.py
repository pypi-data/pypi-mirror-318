#!/usr/bin/env python3
"""CLI interface for send_2_llm."""

import asyncio
import click
import os
from typing import Optional
from rich.console import Console
from rich.prompt import Prompt, Confirm
from dotenv import load_dotenv

from . import send_2_llm
from .types import OutputFormat, ProviderType

# Load environment variables
load_dotenv()

console = Console()

def get_default_provider() -> Optional[str]:
    """Get default provider from .env with validation."""
    provider = os.getenv('DEFAULT_PROVIDER')
    if not provider:
        return None
        
    # Validate provider is supported
    try:
        ProviderType(provider)
        return provider
    except ValueError:
        console.print(f"[yellow]Warning: Provider {provider} not supported[/yellow]")
        return None

def get_default_model(provider: str) -> Optional[str]:
    """Get default model for provider from .env."""
    if not provider:
        return None
        
    model_env = f"{provider.upper()}_MODEL"
    model = os.getenv(model_env)
    
    if not model:
        console.print(f"[yellow]Warning: No model configured for {provider}[/yellow]")
    
    return model

def validate_provider(provider: Optional[str]) -> Optional[str]:
    """Validate provider and its configuration."""
    if not provider:
        return None
        
    # Check if provider has API key
    api_key = os.getenv(f"{provider.upper()}_API_KEY")
    if not api_key:
        console.print(f"[yellow]Warning: No API key found for {provider}[/yellow]")
        return None
    
    # Validate provider is supported
    try:
        ProviderType(provider)
        return provider
    except ValueError:
        console.print(f"[yellow]Warning: Provider {provider} not supported[/yellow]")
        return None

def interactive_mode():
    """Run interactive mode."""
    console.print("[bold blue]Send2LLM Interactive Mode[/bold blue]")
    console.print("Type 'exit' to quit\n")
    
    while True:
        # Get input
        text = Prompt.ask("[bold green]Prompt[/bold green]")
        if text.lower() == 'exit':
            break
            
        # Get format
        format_choice = Prompt.ask(
            "[bold green]Format[/bold green]",
            choices=['raw', 'text', 'markdown', 'telegram_markdown', 'html'],
            default='raw'
        )
        
        # Get JSON option
        json_output = Confirm.ask("[bold green]Return as JSON?[/bold green]", default=False)
        
        # Get provider
        default_provider = get_default_provider()
        while True:
            provider = Prompt.ask(
                f"[bold green]Provider[/bold green] (default: {default_provider or 'none'})",
                default=default_provider or ''
            )
            if not provider and not default_provider:
                console.print("[red]Error: Provider is required[/red]")
                continue
                
            provider = validate_provider(provider or default_provider)
            if provider:
                break
            console.print("[red]Please specify a valid provider[/red]")
        
        # Get model
        default_model = get_default_model(provider)
        model = Prompt.ask(
            f"[bold green]Model[/bold green] (default: {default_model or 'none'})",
            default=default_model or ''
        )
        
        # Run query
        try:
            async def _run():
                console.print("\n[yellow]Sending request...[/yellow]")
                response = await send_2_llm(
                    text,
                    output_format=format_choice if format_choice != 'raw' else None,
                    return_json=json_output,
                    provider_type=provider,
                    model=model if model else None
                )
                console.print("\n[bold yellow]Response:[/bold yellow]")
                console.print(response.text)
                console.print()
            
            asyncio.run(_run())
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
            console.print()


@click.command()
@click.argument('text', required=False)
@click.option('--interactive', '-i', is_flag=True, help='Run in interactive mode')
@click.option('--format', '-f', 
    type=click.Choice(['raw', 'text', 'markdown', 'telegram_markdown', 'html']), 
    default='raw',
    help='Output format')
@click.option('--json', '-j', is_flag=True, help='Return response in JSON format')
@click.option('--provider', '-p', help='Provider to use (default from .env)')
@click.option('--model', '-m', help='Model to use (default from .env)')
@click.option('--debug', '-d', is_flag=True, help='Show debug output')
def cli(text: Optional[str] = None,
        interactive: bool = False,
        format: Optional[str] = None, 
        json: bool = False,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        debug: bool = False):
    """Send text to LLM and get response."""
    # Get and validate provider
    if provider:
        # User specified provider takes precedence
        provider = validate_provider(provider)
    if not provider:
        # Try default provider from .env
        provider = validate_provider(get_default_provider())
        
    if not provider:
        console.print("[red]Error: No valid provider available. Please specify a provider or set DEFAULT_PROVIDER in .env[/red]")
        return
        
    # Get model
    if not model:
        model = get_default_model(provider)
        
    if debug:
        console.print("[yellow]Debug mode enabled[/yellow]")
        console.print(f"Text: {text}")
        console.print(f"Format: {format}")
        console.print(f"JSON: {json}")
        console.print(f"Provider: {provider} (from {'CLI' if provider else '.env'})")
        console.print(f"Model: {model} (from {'CLI' if model else '.env'})")
    
    if interactive:
        interactive_mode()
        return
        
    if not text:
        console.print("[red]Error: Please provide text or use --interactive mode[/red]")
        return
        
    try:
        async def _run():
            if debug:
                console.print("[yellow]Sending request...[/yellow]")
            response = await send_2_llm(
                text,
                output_format=format if format != 'raw' else None,
                return_json=json,
                provider_type=provider,
                model=model
            )
            if debug:
                console.print("[yellow]Got response:[/yellow]")
            console.print(response.text)
        
        asyncio.run(_run())
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        if debug:
            import traceback
            console.print("[yellow]Traceback:[/yellow]")
            console.print(traceback.format_exc())


def main():
    """Entry point for CLI."""
    cli()


if __name__ == '__main__':
    main() 