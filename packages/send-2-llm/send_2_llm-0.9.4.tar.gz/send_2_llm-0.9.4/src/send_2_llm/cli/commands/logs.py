"""Log management command."""

from typing import Optional
from rich.table import Table

from .base import Command
from ..utils.log_rotation import rotate_logs, cleanup_old_logs, get_log_stats
from ..utils.log_analysis import analyze_requests, analyze_errors, get_recent_activity


class LogsCommand(Command):
    """Command for log management."""
    
    async def _execute(self, **kwargs) -> None:
        """Execute logs command.
        
        Args:
            action: Action to perform (status/rotate/cleanup/analyze)
            days: Number of days for analysis/cleanup
            max_size: Maximum log file size in MB
            max_backups: Maximum number of backup files
        """
        action = kwargs.get('action', 'status')
        days = kwargs.get('days', 7)
        max_size = kwargs.get('max_size', 10)
        max_backups = kwargs.get('max_backups', 5)
        
        if action == 'status':
            self._show_status()
        elif action == 'rotate':
            self._rotate_logs(max_size, max_backups)
        elif action == 'cleanup':
            self._cleanup_logs(days)
        elif action == 'analyze':
            self._analyze_logs(days)
    
    def _show_status(self) -> None:
        """Show log files status."""
        stats = get_log_stats()
        
        self.console.print("[bold blue]Log Files Status[/bold blue]")
        
        # Summary table
        summary = Table(title="Summary")
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="green")
        
        summary.add_row("Total Size", f"{stats['total_size_mb']:.2f} MB")
        summary.add_row("File Count", str(stats['file_count']))
        if stats['oldest_file']:
            summary.add_row("Oldest File", f"{stats['oldest_file']['file']} ({stats['oldest_file']['date']})")
        if stats['newest_file']:
            summary.add_row("Newest File", f"{stats['newest_file']['file']} ({stats['newest_file']['date']})")
        
        self.console.print(summary)
        
        # Files table
        files = Table(title="Log Files")
        files.add_column("File", style="cyan")
        files.add_column("Size (MB)", style="green")
        files.add_column("Modified", style="yellow")
        
        for name, info in stats['files'].items():
            files.add_row(
                name,
                f"{info['size_mb']:.2f}",
                info['modified']
            )
        
        self.console.print(files)
    
    def _rotate_logs(self, max_size: int, max_backups: int) -> None:
        """Rotate log files."""
        self.console.print("[bold blue]Rotating Log Files[/bold blue]")
        rotate_logs(max_size_mb=max_size, max_backups=max_backups)
        self.console.print("[green]Log rotation completed[/green]")
    
    def _cleanup_logs(self, days: int) -> None:
        """Clean up old log files."""
        self.console.print(f"[bold blue]Cleaning Up Logs Older Than {days} Days[/bold blue]")
        cleanup_old_logs(days=days)
        self.console.print("[green]Cleanup completed[/green]")
    
    def _analyze_logs(self, days: int) -> None:
        """Analyze logs."""
        self.console.print(f"[bold blue]Log Analysis ({days} days)[/bold blue]")
        
        # Analyze requests
        request_stats = analyze_requests(days=days)
        
        requests = Table(title="Request Statistics")
        requests.add_column("Metric", style="cyan")
        requests.add_column("Value", style="green")
        
        requests.add_row("Total Requests", str(request_stats['total_requests']))
        requests.add_row("Average Text Length", f"{request_stats['avg_text_length']:.0f} chars")
        
        self.console.print(requests)
        
        # Provider distribution
        if request_stats['providers']:
            providers = Table(title="Provider Distribution")
            providers.add_column("Provider", style="cyan")
            providers.add_column("Count", style="green")
            
            for provider, count in request_stats['providers'].items():
                providers.add_row(provider, str(count))
            
            self.console.print(providers)
        
        # Error analysis
        error_stats = analyze_errors(days=days)
        
        errors = Table(title="Error Statistics")
        errors.add_column("Metric", style="cyan")
        errors.add_column("Value", style="green")
        
        errors.add_row("Total Errors", str(error_stats['total_errors']))
        
        self.console.print(errors)
        
        if error_stats['error_types']:
            error_types = Table(title="Error Types")
            error_types.add_column("Type", style="cyan")
            error_types.add_column("Count", style="green")
            
            for error_type, count in error_stats['error_types'].items():
                error_types.add_row(error_type, str(count))
            
            self.console.print(error_types)
        
        # Recent activity
        activity = get_recent_activity(hours=24)
        
        if activity:
            recent = Table(title="Recent Activity (24h)")
            recent.add_column("Time", style="cyan")
            recent.add_column("Level", style="green")
            recent.add_column("Message", style="yellow")
            
            for entry in activity[:10]:  # Show last 10 entries
                recent.add_row(
                    entry['timestamp'],
                    entry['level'],
                    entry['message']
                )
            
            self.console.print(recent) 