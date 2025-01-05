"""Log rotation utilities."""

import os
import gzip
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

from .logging import LOG_DIR, CLI_LOG, REQUEST_LOG, ERROR_LOG


def rotate_logs(max_size_mb: int = 10,
               max_backups: int = 5,
               compress: bool = True) -> None:
    """Rotate log files if they exceed max size.
    
    Args:
        max_size_mb: Maximum size of log file in MB
        max_backups: Maximum number of backup files to keep
        compress: Whether to compress rotated logs
    """
    for log_file in [CLI_LOG, REQUEST_LOG, ERROR_LOG]:
        if not log_file.exists():
            continue
            
        # Check file size
        size_mb = log_file.stat().st_size / (1024 * 1024)
        if size_mb < max_size_mb:
            continue
        
        # Rotate existing backups
        for i in range(max_backups - 1, 0, -1):
            backup = log_file.with_suffix(f'.{i}.log')
            if backup.exists():
                if i == max_backups - 1:
                    backup.unlink()
                else:
                    new_backup = log_file.with_suffix(f'.{i+1}.log')
                    backup.rename(new_backup)
                    if compress and i == 1:
                        compress_log(new_backup)
        
        # Backup current log
        backup = log_file.with_suffix('.1.log')
        shutil.copy2(log_file, backup)
        
        # Clear current log
        log_file.write_text('')


def compress_log(log_file: Path) -> None:
    """Compress log file using gzip.
    
    Args:
        log_file: Path to log file
    """
    if not log_file.exists():
        return
        
    gz_file = log_file.with_suffix('.log.gz')
    with log_file.open('rb') as f_in:
        with gzip.open(gz_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    log_file.unlink()


def cleanup_old_logs(days: int = 30) -> None:
    """Delete log files older than specified days.
    
    Args:
        days: Number of days to keep logs
    """
    cutoff = datetime.now() - timedelta(days=days)
    
    for log_file in LOG_DIR.glob('*.log*'):
        if log_file.stat().st_mtime < cutoff.timestamp():
            log_file.unlink()


def get_log_stats() -> dict:
    """Get statistics about log files.
    
    Returns:
        Dictionary with log statistics
    """
    stats = {
        'total_size_mb': 0,
        'file_count': 0,
        'oldest_file': None,
        'newest_file': None,
        'files': {}
    }
    
    for log_file in LOG_DIR.glob('*.log*'):
        file_stat = log_file.stat()
        file_info = {
            'size_mb': file_stat.st_size / (1024 * 1024),
            'modified': datetime.fromtimestamp(file_stat.st_mtime).isoformat()
        }
        
        stats['files'][log_file.name] = file_info
        stats['total_size_mb'] += file_info['size_mb']
        stats['file_count'] += 1
        
        mtime = datetime.fromtimestamp(file_stat.st_mtime)
        if not stats['oldest_file'] or mtime < datetime.fromisoformat(stats['oldest_file']['date']):
            stats['oldest_file'] = {'file': log_file.name, 'date': mtime.isoformat()}
        if not stats['newest_file'] or mtime > datetime.fromisoformat(stats['newest_file']['date']):
            stats['newest_file'] = {'file': log_file.name, 'date': mtime.isoformat()}
    
    return stats 