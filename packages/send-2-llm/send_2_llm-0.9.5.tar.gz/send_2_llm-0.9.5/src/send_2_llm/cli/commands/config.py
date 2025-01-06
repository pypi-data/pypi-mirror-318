"""Configuration command for CLI."""

from .base import Command
from ..utils.config import print_config


class ConfigCommand(Command):
    """Command for configuration management."""
    
    async def _execute(self, **kwargs) -> None:
        """Execute configuration command.
        
        Args:
            debug: Whether to show sensitive info
        """
        debug = kwargs.get('debug', False)
        
        self.console.print("[bold blue]Current Configuration[/bold blue]")
        print_config(debug=debug)
