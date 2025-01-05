"""
Response formatting layer for LLM responses.
Handles output format conversion without modifying core provider functionality.
"""

from typing import Optional

from .types import LLMResponse, OutputFormat
from .formatters import convert_to_format


class ResponseFormatter:
    """Format LLM responses according to requested output format."""
    
    @staticmethod
    def format_response(response: LLMResponse, output_format: Optional[OutputFormat] = None) -> LLMResponse:
        """Format response text according to requested format.
        
        Args:
            response: Original LLM response
            output_format: Requested output format (uses request format if None)
            
        Returns:
            Formatted LLM response
        """
        # If no format specified or RAW format, return as is
        if not output_format or output_format == OutputFormat.RAW:
            return response
            
        # Format the text while preserving metadata
        formatted_text = convert_to_format(
            response.text,
            output_format,
            metadata=response.metadata.dict() if output_format == OutputFormat.json else None
        )
        
        # Create new response with formatted text
        return LLMResponse(
            text=formatted_text,
            metadata=response.metadata,
            cached=response.cached
        ) 