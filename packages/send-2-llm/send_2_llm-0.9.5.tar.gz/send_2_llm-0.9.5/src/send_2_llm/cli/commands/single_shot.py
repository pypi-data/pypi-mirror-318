"""Single shot command for CLI."""

import asyncio
from typing import Optional

from .base import Command
from ..utils.validation import get_provider_config, validate_required_text
from ..utils.formatting import format_response, format_error
from ..utils.logging import log_request
from ... import send_2_llm


class SingleShotCommand(Command):
    """Command for single shot LLM requests."""
    
    async def _execute(self, **kwargs) -> None:
        """Execute single shot request.
        
        Args:
            text: Input text
            format: Output format
            json: Whether to return JSON
            provider: Provider to use
            model: Model to use
            debug: Whether to show debug info
        """
        text = kwargs.get('text')
        format = kwargs.get('format')
        json = kwargs.get('json', False)
        provider = kwargs.get('provider')
        model = kwargs.get('model')
        debug = kwargs.get('debug', False)
        
        # Validate input
        if not validate_required_text(text, interactive=False):
            return
            
        # Get provider config
        if not provider:
            provider, default_model = get_provider_config()
            if not provider:
                self.console.print("[red]Error: No valid provider available. Please specify a provider or set DEFAULT_PROVIDER in .env[/red]")
                return
            if not model:
                model = default_model
        
        # Validate format
        output_format = self._validate_format(format)
        
        if debug:
            self.console.print("[yellow]Debug mode enabled[/yellow]")
            self.console.print(f"Text: {text}")
            self.console.print(f"Format: {format}")
            self.console.print(f"JSON: {json}")
            self.console.print(f"Provider: {provider}")
            self.console.print(f"Model: {model}")
        
        try:
            if debug:
                self.console.print("[yellow]Sending request...[/yellow]")
            
            # Log request
            log_request(provider, model, text, format, json)
            
            response = await send_2_llm(
                text,
                output_format=output_format,
                return_json=json,
                provider_type=provider,
                model=model
            )
            
            format_response(response, debug=debug)
            
        except Exception as e:
            format_error(e, debug=debug)
