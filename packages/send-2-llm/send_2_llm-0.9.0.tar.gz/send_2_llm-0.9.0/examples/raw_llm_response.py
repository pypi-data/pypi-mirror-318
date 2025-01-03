#!/usr/bin/env python3
"""
CLI tool to send requests to LLM providers and get raw unformatted responses.
Shows complete provider response including metadata, token usage, and timing information.

Usage:
    python raw_llm_response.py
"""

import asyncio
import json
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from send_2_llm import send_2_llm
from send_2_llm.types import OutputFormat, ProviderType

console = Console()

async def get_raw_response() -> None:
    """Get raw response from LLM provider"""
    try:
        prompt = "Напиши стихотворение из 3 слов с эмодзи"
        
        console.print("[cyan]Отправляем запрос к LLM...[/cyan]")
        
        console.print(f"[yellow]DEBUG: Sending request with prompt: {prompt}[/yellow]")
            
        response = await send_2_llm(
            prompt,
            provider=ProviderType.GEMINI,
            output_format=OutputFormat.RAW
        )
        
        console.print(f"[yellow]DEBUG: Got response: {response}[/yellow]")
        
        # Display complete raw response from API
        console.print("\n[bold green]=== COMPLETE RAW API RESPONSE ===[/bold green]")
        
        # Print raw response object attributes
        console.print("\n[yellow]Response Text:[/yellow]")
        console.print(response.text)
        
        console.print("\n[yellow]Raw Response Metadata:[/yellow]")
        console.print(f"Provider: {response.metadata.provider}")
        console.print(f"Model: {response.metadata.model}")
        console.print(f"Created At: {response.metadata.created_at}")
        console.print(f"Strategy: {response.metadata.strategy}")
        console.print(f"Latency: {response.metadata.latency:.2f} seconds")
        
        console.print("\n[yellow]Token Usage:[/yellow]")
        console.print(f"Prompt Tokens: {response.metadata.usage.prompt_tokens}")
        console.print(f"Completion Tokens: {response.metadata.usage.completion_tokens}")
        console.print(f"Total Tokens: {response.metadata.usage.total_tokens}")
        console.print(f"Cost: ${response.metadata.usage.cost:.6f}")
        
        if response.metadata.raw_response:
            console.print("\n[yellow]Complete Provider JSON Response:[/yellow]")
            syntax = Syntax(
                json.dumps(response.metadata.raw_response, indent=2, ensure_ascii=False),
                "json",
                theme="monokai"
            )
            console.print(syntax)
        
    except Exception as e:
        error_panel = Panel(
            f"[red]{str(e)}[/red]",
            title="[bold red]Error[/bold red]",
            border_style="red"
        )
        console.print(error_panel)

async def main():
    """Main CLI interface"""
    console.print(Panel(
        "[bold blue]Raw LLM Response Viewer[/bold blue]\n"
        "Shows complete unformatted provider response with all metadata",
        border_style="blue"
    ))
    
    await get_raw_response()

if __name__ == "__main__":
    asyncio.run(main())