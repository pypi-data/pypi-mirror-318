"""Main CLI interface."""

import asyncio
import click
from rich.console import Console

from .commands.single_shot import SingleShotCommand
from .commands.interactive import InteractiveCommand
from .commands.config import ConfigCommand
from .commands.logs import LogsCommand
from .utils.logging import setup_logging


@click.group()
@click.option('--debug', '-d', is_flag=True, help='Show debug output')
@click.pass_context
def cli(ctx: click.Context, debug: bool = False) -> None:
    """Send2LLM CLI tool."""
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug
    ctx.obj['console'] = Console()
    
    # Setup logging
    setup_logging(debug=debug)


@cli.command()
@click.argument('text', required=True)
@click.option('--format', '-f',
    type=click.Choice(['raw', 'text', 'markdown', 'telegram_markdown', 'html']),
    default='raw',
    help='Output format')
@click.option('--json', '-j', is_flag=True, help='Return response in JSON format')
@click.option('--provider', '-p', help='Provider to use (default from .env)')
@click.option('--model', '-m', help='Model to use (default from .env)')
@click.pass_context
def send(ctx: click.Context,
         text: str,
         format: str = 'raw',
         json: bool = False,
         provider: str = None,
         model: str = None) -> None:
    """Send text to LLM and get response."""
    command = SingleShotCommand(console=ctx.obj['console'])
    asyncio.run(command.execute(
        text=text,
        format=format,
        json=json,
        provider=provider,
        model=model,
        debug=ctx.obj['debug']
    ))


@cli.command()
@click.pass_context
def interactive(ctx: click.Context) -> None:
    """Run in interactive mode."""
    command = InteractiveCommand(console=ctx.obj['console'])
    asyncio.run(command.execute(debug=ctx.obj['debug']))


@cli.command()
@click.pass_context
def config(ctx: click.Context) -> None:
    """Show current configuration."""
    command = ConfigCommand(console=ctx.obj['console'])
    asyncio.run(command.execute(debug=ctx.obj['debug']))


@cli.command()
@click.option('--action', '-a',
    type=click.Choice(['status', 'rotate', 'cleanup', 'analyze']),
    default='status',
    help='Action to perform')
@click.option('--days', '-d',
    type=int,
    default=7,
    help='Number of days for analysis/cleanup')
@click.option('--max-size', '-s',
    type=int,
    default=10,
    help='Maximum log file size in MB')
@click.option('--max-backups', '-b',
    type=int,
    default=5,
    help='Maximum number of backup files')
@click.pass_context
def logs(ctx: click.Context,
         action: str = 'status',
         days: int = 7,
         max_size: int = 10,
         max_backups: int = 5) -> None:
    """Manage log files."""
    command = LogsCommand(console=ctx.obj['console'])
    asyncio.run(command.execute(
        action=action,
        days=days,
        max_size=max_size,
        max_backups=max_backups
    ))


def main() -> None:
    """Entry point for CLI."""
    cli(obj={})
