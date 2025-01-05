"""
Constants for model pricing and token limits.
Contains pricing information per million tokens and model limits.
"""

from typing import Dict, Any

# Prices per MILLION tokens (not per 1000 as before)
PERPLEXITY_MODEL_PRICES: Dict[str, Dict[str, float]] = {
    # Sonar models
    "llama-3.1-sonar-huge-128k-online": {
        "prompt": 1.5,  # $1.50 per million tokens
        "completion": 2.0  # $2.00 per million tokens
    },
    "llama-3.1-sonar-huge-online": {
        "prompt": 1.2,
        "completion": 1.6
    },
    "llama-3.1-sonar-medium-online": {
        "prompt": 0.8,
        "completion": 1.2
    },
    "llama-3.1-sonar-small-online": {
        "prompt": 0.6,
        "completion": 0.8
    },
    # Mixtral & Mistral models
    "mixtral-8x7b-instruct": {
        "prompt": 0.4,
        "completion": 0.8
    },
    "mistral-7b-instruct": {
        "prompt": 0.2,
        "completion": 0.4
    },
    # CodeLlama models
    "codellama-34b-instruct": {
        "prompt": 0.3,
        "completion": 0.6
    }
}

# Token limits for each model
PERPLEXITY_MODEL_LIMITS: Dict[str, Dict[str, int]] = {
    # Sonar models
    "llama-3.1-sonar-huge-128k-online": {
        "max_total_tokens": 128000,
        "max_prompt_tokens": 96000,
        "max_completion_tokens": 32000
    },
    "llama-3.1-sonar-huge-online": {
        "max_total_tokens": 32000,
        "max_prompt_tokens": 24000,
        "max_completion_tokens": 8000
    },
    "llama-3.1-sonar-medium-online": {
        "max_total_tokens": 16000,
        "max_prompt_tokens": 12000,
        "max_completion_tokens": 4000
    },
    "llama-3.1-sonar-small-online": {
        "max_total_tokens": 8000,
        "max_prompt_tokens": 6000,
        "max_completion_tokens": 2000
    },
    # Mixtral & Mistral models
    "mixtral-8x7b-instruct": {
        "max_total_tokens": 32000,
        "max_prompt_tokens": 24000,
        "max_completion_tokens": 8000
    },
    "mistral-7b-instruct": {
        "max_total_tokens": 16000,
        "max_prompt_tokens": 12000,
        "max_completion_tokens": 4000
    },
    # CodeLlama models
    "codellama-34b-instruct": {
        "max_total_tokens": 16000,
        "max_prompt_tokens": 12000,
        "max_completion_tokens": 4000
    }
}

# Default system prompts for different tasks
DEFAULT_SYSTEM_PROMPTS: Dict[str, str] = {
    "general": "You are a helpful AI assistant. Provide accurate and relevant information.",
    "code": "You are a code assistant. Provide clear, efficient, and well-documented code solutions.",
    "math": "You are a math assistant. Show detailed steps and explanations for mathematical problems.",
    "writing": "You are a writing assistant. Help improve text while maintaining the original meaning and style.",
    "research": "You are a research assistant. Provide well-sourced information and cite references when available."
} 