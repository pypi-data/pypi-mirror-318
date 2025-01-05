"""Interactive command for CLI."""

from typing import Optional
from rich.prompt import Prompt, Confirm

from .base import Command
from ..utils.validation import get_provider_config
from ..utils.formatting import format_response, format_error
from ..utils.logging import log_request
from ... import send_2_llm


class InteractiveCommand(Command):
    """Command for interactive mode."""
    
    async def _execute(self, **kwargs) -> None:
        """Execute interactive mode.
        
        Args:
            debug: Whether to show debug info
        """
        debug = kwargs.get('debug', False)
        
        self.console.print("[bold blue]Send2LLM Interactive Mode[/bold blue]")
        self.console.print("Type 'exit' to quit\n")
        
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
            provider = None
            while True:
                provider_input = Prompt.ask(
                    "[bold green]Provider[/bold green] (press Enter for default)",
                    default=''
                )
                
                if not provider_input:
                    provider, model = get_provider_config()
                    if provider:
                        break
                    self.console.print("[red]No default provider configured[/red]")
                    continue
                
                provider, model = get_provider_config(provider_input)
                if provider:
                    break
                self.console.print("[red]Please specify a valid provider[/red]")
            
            # Get model
            model_input = Prompt.ask(
                "[bold green]Model[/bold green] (press Enter for default)",
                default=''
            )
            if model_input:
                model = model_input
            
            # Run query
            try:
                if debug:
                    self.console.print("\n[yellow]Sending request...[/yellow]")
                
                # Log request
                log_request(provider, model, text, format_choice, json_output)
                
                response = await send_2_llm(
                    text,
                    output_format=self._validate_format(format_choice),
                    return_json=json_output,
                    provider_type=provider,
                    model=model
                )
                
                format_response(response, debug=debug)
                
            except Exception as e:
                format_error(e, debug=debug)
            
            self.console.print()
