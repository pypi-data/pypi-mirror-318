"""Chat example using random provider selection for each message."""

import asyncio
import random
from typing import Optional
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich import box

from dotenv import load_dotenv
from send_2_llm import LLMClient
from send_2_llm.config import reload_config
from send_2_llm.types import ProviderType, LLMResponse

# Initialize rich console
console = Console()

class ChatUI:
    """Chat UI handler using rich."""
    
    def __init__(self):
        """Initialize chat UI."""
        self.total_cost = 0.0
        self.total_tokens = 0
        self.start_time = datetime.now()
        self.messages = []
        
    def create_header(self) -> Panel:
        """Create header panel."""
        providers = [p for p in ProviderType if p.value not in ('unknown', 'invalid', '')]
        provider_list = ", ".join(p.value for p in providers)
        
        header = Text()
        header.append("Чат с разными LLM провайдерами\n", style="bold cyan")
        header.append("Каждое сообщение будет отправлено случайному провайдеру\n", style="cyan")
        header.append(f"Доступные провайдеры: {provider_list}\n", style="blue")
        header.append("Введите ваш текст (или 'exit' для выхода)", style="yellow")
        
        return Panel(header, box=box.ROUNDED)
        
    def create_stats(self) -> Panel:
        """Create statistics panel."""
        duration = (datetime.now() - self.start_time).total_seconds()
        
        stats = Table.grid(padding=1)
        stats.add_column(style="cyan")
        stats.add_column(style="yellow")
        stats.add_row("Время сессии:", f"{duration:.1f} сек")
        stats.add_row("Всего токенов:", str(self.total_tokens))
        stats.add_row("Общая стоимость:", f"${self.total_cost:.6f}")
        
        return Panel(stats, title="[bold cyan]Статистика", border_style="cyan", box=box.ROUNDED)
        
    def create_message_panel(self, text: str, is_user: bool = False, metadata: Optional[dict] = None) -> Panel:
        """Create message panel."""
        style = "yellow" if is_user else "green"
        sender = "Вы" if is_user else "LLM"
        
        content = Text(text, style=style)
        
        if metadata:
            content.append(f"\n\n[blue]Провайдер:[/blue] {metadata['provider']}")
            content.append(f"\n[blue]Модель:[/blue] {metadata['model']}")
            content.append(f"\n[blue]Токены:[/blue] {metadata['tokens']}")
            content.append(f"\n[blue]Стоимость:[/blue] ${metadata['cost']:.6f}")
        
        return Panel(
            content,
            title=f"[bold {style}]{sender}",
            border_style=style,
            box=box.ROUNDED
        )

async def chat():
    """Chat with LLM using random provider for each message."""
    load_dotenv()  # Load environment variables from .env
    reload_config()  # Clear config cache
    
    # Initialize UI
    ui = ChatUI()
    console.clear()
    
    # Available providers
    providers = [p for p in ProviderType if p.value not in ('unknown', 'invalid', '')]
    
    # Show header
    console.print(ui.create_header())
    console.print(ui.create_stats())
    
    while True:
        try:
            # Get user input
            user_input = console.input("\n[yellow]Вы:[/yellow] ").strip()
            if user_input.lower() == 'exit':
                break
            
            if not user_input:
                continue
            
            # Show user message
            console.print(ui.create_message_panel(user_input, is_user=True))
            
            # Select random provider
            provider = random.choice(providers)
            console.print(f"\n[cyan]Выбран провайдер:[/cyan] {provider.value}")
            
            # Create client with selected provider
            async with LLMClient(provider_type=provider) as client:
                with console.status("[cyan]LLM генерирует ответ...", spinner="dots"):
                    response = await client.generate(user_input)
                
                # Update statistics
                ui.total_cost += response.metadata.usage.cost
                ui.total_tokens += response.metadata.usage.total_tokens
                
                # Show response with metadata
                metadata = {
                    "provider": response.metadata.provider,
                    "model": response.metadata.model,
                    "tokens": response.metadata.usage.total_tokens,
                    "cost": response.metadata.usage.cost
                }
                console.print(ui.create_message_panel(response.text, metadata=metadata))
                
                # Show updated stats
                console.print(ui.create_stats())
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"\n[red]Ошибка:[/red] {str(e)}")
            continue
    
    # Show final stats
    console.print("\n[bold cyan]Итоги сессии:[/bold cyan]")
    console.print(ui.create_stats())
    console.print("\n[yellow]До свидания![/yellow]")


if __name__ == "__main__":
    asyncio.run(chat()) 