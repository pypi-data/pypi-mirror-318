"""
Raw API CLI example.
Shows direct provider usage without LLMClient.
Displays raw API response without any processing.
"""

import os
import json
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.json import JSON
from rich.syntax import Syntax
from rich.table import Table
from rich.box import ROUNDED

from send_2_llm.config import reload_config
from send_2_llm.types import ProviderType, LLMRequest
from send_2_llm.providers.factory import create_provider

# Initialize rich console
console = Console()

async def chat():
    """Chat directly with provider API."""
    load_dotenv()  # Load environment variables from .env
    reload_config()  # Clear config cache
    
    # Get provider from environment or use default
    provider_type = os.getenv("DEFAULT_PROVIDER", "openai")
    try:
        provider = create_provider(ProviderType(provider_type.lower()))
    except ValueError:
        console.print(f"[red]Invalid provider: {provider_type}[/red]")
        console.print("[yellow]Using OpenAI as fallback[/yellow]")
        provider = create_provider(ProviderType.OPENAI)
    
    # Print header
    console.print(Panel(
        "[bold blue]=== Прямой доступ к API провайдера ===[/bold blue]\n" +
        f"[green]Провайдер:[/green] {provider.provider_type.value}\n" +
        f"[green]Модель по умолчанию:[/green] {provider.default_model}\n" +
        "[yellow]Введите ваш текст (или 'exit' для выхода)[/yellow]",
        box=ROUNDED
    ))
    
    # Initialize session stats
    session_start = datetime.now()
    total_messages = 0
    total_tokens = 0
    total_cost = 0.0
    
    while True:
        try:
            # Get user input
            user_input = console.input("\n[bold cyan]Вы:[/bold cyan] ").strip()
            if user_input.lower() == 'exit':
                break
            
            if not user_input:
                continue
            
            # Create request
            request = LLMRequest(
                prompt=user_input,
                max_tokens=1000,  # Adjust as needed
                temperature=0.7  # Adjust for creativity
            )
            
            # Generate response
            response = await provider.generate(request)
            total_messages += 1
            
            # Print raw response
            console.print("\n[bold green]RAW API RESPONSE:[/bold green]")
            # Convert raw response to pretty JSON
            json_str = json.dumps(response.metadata.raw_response, indent=2, ensure_ascii=False)
            console.print(Panel(
                JSON(json_str),
                title="Raw Response",
                border_style="green",
                box=ROUNDED
            ))
            
            # Print processed response
            console.print(Panel(
                response.text,
                title="[bold]Processed Response[/bold]",
                border_style="blue",
                box=ROUNDED
            ))
            
            # Print metadata in a table
            table = Table(title="Метаданные", box=ROUNDED, show_header=True, header_style="bold magenta")
            table.add_column("Параметр", style="cyan")
            table.add_column("Значение", style="green")
            
            table.add_row("Провайдер", str(response.metadata.provider))
            table.add_row("Модель", response.metadata.model)
            table.add_row("Токены", str(response.metadata.usage.total_tokens))
            table.add_row("Стоимость", f"${response.metadata.usage.cost:.6f}")
            
            console.print(table)
            
            # Update totals
            total_tokens += response.metadata.usage.total_tokens
            total_cost += response.metadata.usage.cost
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"\n[red]Ошибка:[/red] {str(e)}")
            continue
    
    # Print session summary in a table
    summary_table = Table(title="Итоги сессии", box=ROUNDED, show_header=True, header_style="bold magenta")
    summary_table.add_column("Параметр", style="cyan")
    summary_table.add_column("Значение", style="green")
    
    session_duration = (datetime.now() - session_start).total_seconds()
    summary_table.add_row("Длительность", f"{session_duration:.1f} сек")
    summary_table.add_row("Сообщений", str(total_messages))
    summary_table.add_row("Всего токенов", str(total_tokens))
    summary_table.add_row("Общая стоимость", f"${total_cost:.6f}")
    
    if total_messages > 0:
        summary_table.add_row("Среднее токенов/сообщение", f"{total_tokens/total_messages:.1f}")
        summary_table.add_row("Средняя стоимость/сообщение", f"${total_cost/total_messages:.6f}")
    
    console.print("\n", summary_table)
    console.print("\n[bold green]До свидания![/bold green]")


if __name__ == "__main__":
    asyncio.run(chat()) 