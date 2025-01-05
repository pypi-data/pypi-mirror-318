"""Log analysis utilities."""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

from .logging import LOG_DIR


def parse_log_line(line: str) -> Optional[Dict]:
    """Parse log line into structured data.
    
    Args:
        line: Log line to parse
        
    Returns:
        Dictionary with parsed data or None if line cannot be parsed
    """
    # Parse timestamp and level
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (\w+) - (\w+) - (.+)', line)
    if not match:
        return None
        
    timestamp, logger, level, message = match.groups()
    
    # Parse JSON data if present
    try:
        data = json.loads(message)
        return {
            'timestamp': timestamp,
            'logger': logger,
            'level': level,
            'data': data
        }
    except json.JSONDecodeError:
        return {
            'timestamp': timestamp,
            'logger': logger,
            'level': level,
            'message': message
        }


def analyze_requests(days: int = 7) -> Dict:
    """Analyze request logs.
    
    Args:
        days: Number of days to analyze
        
    Returns:
        Dictionary with request statistics
    """
    stats = {
        'total_requests': 0,
        'providers': defaultdict(int),
        'models': defaultdict(int),
        'formats': defaultdict(int),
        'hourly_distribution': defaultdict(int),
        'daily_distribution': defaultdict(int),
        'avg_text_length': 0,
        'total_text_length': 0
    }
    
    cutoff = datetime.now() - timedelta(days=days)
    log_files = [REQUEST_LOG] + list(LOG_DIR.glob('requests.*.log*'))
    
    for log_file in log_files:
        if not log_file.exists():
            continue
            
        with log_file.open() as f:
            for line in f:
                parsed = parse_log_line(line)
                if not parsed:
                    continue
                
                timestamp = datetime.strptime(parsed['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
                if timestamp < cutoff:
                    continue
                
                if 'data' in parsed:
                    data = parsed['data']
                    stats['total_requests'] += 1
                    stats['providers'][data.get('provider', 'unknown')] += 1
                    stats['models'][data.get('model', 'unknown')] += 1
                    stats['formats'][data.get('format', 'raw')] += 1
                    stats['hourly_distribution'][timestamp.hour] += 1
                    stats['daily_distribution'][timestamp.strftime('%Y-%m-%d')] += 1
                    
                    text_length = len(data.get('text', ''))
                    stats['total_text_length'] += text_length
    
    if stats['total_requests'] > 0:
        stats['avg_text_length'] = stats['total_text_length'] / stats['total_requests']
    
    return dict(stats)


def analyze_errors(days: int = 7) -> Dict:
    """Analyze error logs.
    
    Args:
        days: Number of days to analyze
        
    Returns:
        Dictionary with error statistics
    """
    stats = {
        'total_errors': 0,
        'error_types': defaultdict(int),
        'error_contexts': defaultdict(list),
        'hourly_distribution': defaultdict(int),
        'daily_distribution': defaultdict(int)
    }
    
    cutoff = datetime.now() - timedelta(days=days)
    log_files = [ERROR_LOG] + list(LOG_DIR.glob('errors.*.log*'))
    
    for log_file in log_files:
        if not log_file.exists():
            continue
            
        with log_file.open() as f:
            for line in f:
                parsed = parse_log_line(line)
                if not parsed:
                    continue
                
                timestamp = datetime.strptime(parsed['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
                if timestamp < cutoff:
                    continue
                
                if 'data' in parsed and 'error_type' in parsed['data']:
                    data = parsed['data']
                    error_type = data['error_type']
                    context = json.loads(data.get('context', '{}'))
                    
                    stats['total_errors'] += 1
                    stats['error_types'][error_type] += 1
                    stats['error_contexts'][error_type].append(context)
                    stats['hourly_distribution'][timestamp.hour] += 1
                    stats['daily_distribution'][timestamp.strftime('%Y-%m-%d')] += 1
    
    return dict(stats)


def get_recent_activity(hours: int = 24) -> List[Dict]:
    """Get recent CLI activity.
    
    Args:
        hours: Number of hours to look back
        
    Returns:
        List of recent activity entries
    """
    activity = []
    cutoff = datetime.now() - timedelta(hours=hours)
    
    log_files = [CLI_LOG] + list(LOG_DIR.glob('cli.*.log*'))
    
    for log_file in log_files:
        if not log_file.exists():
            continue
            
        with log_file.open() as f:
            for line in f:
                parsed = parse_log_line(line)
                if not parsed:
                    continue
                
                timestamp = datetime.strptime(parsed['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
                if timestamp < cutoff:
                    continue
                
                activity.append({
                    'timestamp': parsed['timestamp'],
                    'level': parsed['level'],
                    'message': parsed.get('message', ''),
                    'data': parsed.get('data', {})
                })
    
    return sorted(activity, key=lambda x: x['timestamp'], reverse=True) 