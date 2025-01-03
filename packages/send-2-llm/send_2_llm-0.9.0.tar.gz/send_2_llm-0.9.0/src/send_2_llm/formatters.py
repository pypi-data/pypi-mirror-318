"""
Output formatting utilities for LLM responses.
"""

import json
import re
from typing import Any, Dict, Optional
from datetime import datetime

from .types import OutputFormat


def normalize_whitespace(text: str) -> str:
    """Normalize whitespace in text.
    
    - Replace multiple spaces with single space
    - Normalize line endings
    - Remove leading/trailing whitespace
    - Preserve paragraph breaks
    """
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Split into paragraphs
    paragraphs = []
    current_paragraph = []
    
    for line in text.split('\n'):
        if line.strip():
            # Add words from non-empty line to current paragraph
            current_paragraph.extend(word for word in line.split() if word)
        elif current_paragraph:
            # Empty line - end current paragraph
            paragraphs.append(' '.join(current_paragraph))
            current_paragraph = []
            
    # Add last paragraph if any
    if current_paragraph:
        paragraphs.append(' '.join(current_paragraph))
            
    # Join paragraphs with double newlines
    return '\n\n'.join(paragraphs)


def escape_telegram_markdown(text: str) -> str:
    """Escape special characters for Telegram markdown.
    
    Escapes: _ * [ ] ( ) ~ > # + - = | { } . !
    Note: ` is not escaped as it's used for inline code
    """
    escape_chars = '_*[]()~`>#+-=|{}.!'
    result = []
    
    for char in text:
        if char in escape_chars and (not result or result[-1] != '\\'):
            result.append('\\' + char)
        else:
            result.append(char)
            
    return ''.join(result)


def format_telegram_markdown(text: str) -> str:
    """Format text as Telegram markdown.
    
    - Escape special characters
    - Format code blocks
    - Format inline code
    - Format links
    """
    # First normalize whitespace
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Process code blocks first
    result = []
    parts = text.split('```')
    
    for i, part in enumerate(parts):
        if i % 2 == 0:
            # Outside code block - escape markdown
            result.append(escape_telegram_markdown(part))
        else:
            # Inside code block
            lines = part.strip().split('\n', 1)
            if len(lines) > 1:
                # If there's a language specified
                lang, code = lines
                result.append(f'```{lang.strip()}\n{code.strip()}\n```')
            else:
                # No language specified
                result.append(f'```\n{part.strip()}\n```')
            
    return ''.join(result)


def format_as_json(text: str, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Format response as JSON.
    
    Args:
        text: The response text
        metadata: Optional metadata to include
    
    Returns:
        JSON formatted string with response and metadata
    """
    response = {
        "text": normalize_whitespace(text)
    }
    
    if metadata:
        # Convert datetime objects to ISO format
        processed_metadata = {}
        for key, value in metadata.items():
            if isinstance(value, datetime):
                processed_metadata[key] = value.isoformat()
            elif isinstance(value, dict):
                # Recursively process nested dictionaries
                processed_metadata[key] = {
                    k: v.isoformat() if isinstance(v, datetime) else v
                    for k, v in value.items()
                }
            else:
                processed_metadata[key] = value
        response["metadata"] = processed_metadata
        
    return json.dumps(response, indent=2, ensure_ascii=False)


def convert_to_format(text: str, output_format: OutputFormat, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Convert text to specified output format.
    
    Args:
        text: Input text to format
        output_format: Target output format
        metadata: Optional metadata (for JSON format)
    
    Returns:
        Formatted text in requested format
    """
    if output_format == OutputFormat.RAW:
        return text
        
    if output_format == OutputFormat.TEXT:
        return normalize_whitespace(text)
        
    if output_format == OutputFormat.json:  # Note lowercase 'json'
        return format_as_json(text, metadata)
        
    if output_format == OutputFormat.TELEGRAM_MARKDOWN:
        return format_telegram_markdown(text)
        
    raise ValueError(f"Unsupported output format: {output_format}")


def validate_format(text: str, output_format: OutputFormat) -> bool:
    """Validate if text matches expected format.
    
    Args:
        text: Text to validate
        output_format: Expected format
    
    Returns:
        True if text matches format, False otherwise
    """
    if output_format == OutputFormat.RAW:
        return True  # RAW accepts any format
        
    if output_format == OutputFormat.TEXT:
        # Check if text has consistent whitespace
        return text == normalize_whitespace(text)
        
    if output_format == OutputFormat.json:  # Note lowercase 'json'
        try:
            # Try to parse as JSON
            json.loads(text)
            return True
        except json.JSONDecodeError:
            return False
            
    if output_format == OutputFormat.TELEGRAM_MARKDOWN:
        # Check for unescaped special characters outside code blocks
        lines = text.split('\n')
        is_code = False
        for line in lines:
            if line.startswith('```'):
                is_code = not is_code
                continue
            if not is_code:
                if re.search(r'(?<!\\)[_*\[\]()~`>#+=|{}.!-]', line):
                    return False
        return True
        
    return False 