"""Base classes for CLI commands."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from rich.console import Console

from ...types import ProviderType, OutputFormat
from ..utils.logging import log_command, log_error


class Command(ABC):
    """Base class for CLI commands."""
    
    def __init__(self, console: Optional[Console] = None):
        """Initialize command.
        
        Args:
            console: Rich console instance for output
        """
        self.console = console or Console()
    
    @abstractmethod
    async def execute(self, **kwargs: Any) -> None:
        """Execute the command.
        
        Args:
            **kwargs: Command arguments
        """
        command_name = self.__class__.__name__.replace('Command', '').lower()
        log_command(command_name, kwargs)
        
        try:
            await self._execute(**kwargs)
        except Exception as e:
            log_error(e, {'command': command_name, 'args': kwargs})
            raise
    
    @abstractmethod
    async def _execute(self, **kwargs: Any) -> None:
        """Internal execute method to be implemented by subclasses.
        
        Args:
            **kwargs: Command arguments
        """
        pass
    
    def _validate_provider(self, provider: Optional[str]) -> Optional[str]:
        """Validate provider name.
        
        Args:
            provider: Provider name to validate
            
        Returns:
            Validated provider name or None if invalid
        """
        if not provider:
            return None
            
        try:
            ProviderType(provider)
            return provider
        except ValueError:
            self.console.print(f"[yellow]Warning: Provider {provider} not supported[/yellow]")
            return None
    
    def _validate_format(self, format: Optional[str]) -> Optional[OutputFormat]:
        """Validate output format.
        
        Args:
            format: Format name to validate
            
        Returns:
            Validated OutputFormat or None if invalid
        """
        if not format or format == 'raw':
            return None
            
        try:
            return OutputFormat(format)
        except ValueError:
            self.console.print(f"[yellow]Warning: Format {format} not supported[/yellow]")
            return None
    
    def _format_error(self, error: Exception) -> str:
        """Format error message.
        
        Args:
            error: Exception to format
            
        Returns:
            Formatted error message
        """
        return f"[red]Error: {str(error)}[/red]"
