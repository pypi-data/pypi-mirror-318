"""
!!! WARNING - STABLE TYPES !!!
This file contains critical type definitions for OpenAI integration.
DO NOT MODIFY OpenAI-related types without explicit permission.
Commit: b25d24a
Tag: stable_openai_v1

Protected types:
- ProviderType (OpenAI enum)
- LLMRequest (used by OpenAI provider)
- LLMResponse (used by OpenAI provider)
- TokenUsage (OpenAI token tracking)
- LLMMetadata (OpenAI response metadata)
- ProviderAPIError (OpenAI error handling)

Required dependencies:
- pydantic>=2.0.0
!!! WARNING !!!
"""

from enum import Enum
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
import json


# !!! STABLE TYPE - DO NOT MODIFY !!!
class ProviderType(str, Enum):
    """Types of LLM providers."""
    
    OPENAI = "openai"  # !!! STABLE - DO NOT MODIFY !!!
    TOGETHER = "together"
    ANTHROPIC = "anthropic"
    PERPLEXITY = "perplexity"
    DEEPSEEK = "deepseek"
    GEMINI = "gemini"


class StrategyType(str, Enum):
    """Types of LLM strategies."""
    
    SINGLE = "single"  # Single provider
    FALLBACK = "fallback"  # Try providers in sequence
    PARALLEL = "parallel"  # Run multiple providers in parallel
    COST_OPTIMIZED = "cost_optimized"  # Choose based on cost
    PERFORMANCE = "performance"  # Choose based on performance
    SMART = "smart"  # Smart provider selection


class OutputFormat(str, Enum):
    """Output format types for LLM responses.
    
    Available formats:
    - RAW: Unmodified provider output without any formatting
    - TEXT: Clean plain text (default) with normalized whitespace
    - JSON: Structured JSON response with consistent schema
    - TELEGRAM_MARKDOWN: Telegram-specific markdown formatting
    """
    
    RAW = "raw"  # Raw provider output without modifications
    TEXT = "text"  # Clean text with normalized whitespace (default)
    json = "json"  # Structured JSON response
    TELEGRAM_MARKDOWN = "telegram_markdown"  # Telegram-specific markdown


# !!! STABLE TYPE - DO NOT MODIFY !!!
class TokenUsage(BaseModel):
    """Information about token usage."""
    
    prompt_tokens: int = Field(default=0, description="Number of tokens in prompt")
    completion_tokens: int = Field(default=0, description="Number of tokens in completion")
    total_tokens: int = Field(default=0, description="Total number of tokens")
    cost: float = Field(default=0.0, description="Request cost in USD")


# !!! STABLE TYPE - DO NOT MODIFY !!!
class LLMMetadata(BaseModel):
    """LLM response metadata."""
    
    provider: ProviderType = Field(..., description="LLM provider used")
    model: str = Field(..., description="Model name used")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    usage: TokenUsage = Field(default_factory=TokenUsage, description="Token usage info")
    raw_response: Optional[Dict[str, Any]] = Field(None, description="Raw provider response")
    strategy: Optional[StrategyType] = Field(None, description="Strategy used if any")
    latency: Optional[float] = Field(None, description="Request latency in seconds")


# !!! STABLE TYPE - DO NOT MODIFY !!!
class LLMRequest(BaseModel):
    """Request to LLM provider."""
    
    prompt: str = Field(..., description="Input prompt")
    provider_type: Optional[ProviderType] = Field(None, description="Specific provider to use")
    model: Optional[str] = Field(None, description="Specific model to use")
    strategy: Optional[StrategyType] = Field(None, description="Strategy to use")
    max_tokens: Optional[int] = Field(None, description="Maximum tokens in response")
    temperature: float = Field(default=0.7, description="Sampling temperature")
    top_p: float = Field(default=1.0, description="Nucleus sampling parameter")
    stop: Optional[List[str]] = Field(None, description="Stop sequences")
    output_format: Optional[OutputFormat] = Field(default=OutputFormat.RAW, description="Output format type")
    return_json: bool = Field(default=False, description="Whether to return response in JSON format")
    extra_params: Optional[Dict[str, Any]] = Field(None, description="Extra provider-specific parameters")


# !!! STABLE TYPE - DO NOT MODIFY !!!
class LLMResponse(BaseModel):
    """Structured response from LLM."""
    
    text: str = Field(..., description="Response text")
    metadata: LLMMetadata = Field(..., description="Response metadata")
    cached: bool = Field(default=False, description="Whether response was cached")


# !!! STABLE TYPE - DO NOT MODIFY !!!
class LLMError(Exception):
    """Base class for LLM errors."""
    
    def __init__(self, message: str, provider: Optional[ProviderType] = None):
        self.provider = provider
        super().__init__(message)


class TokenLimitError(LLMError):
    """Token limit exceeded error."""
    pass


# !!! STABLE TYPE - DO NOT MODIFY !!!
class ProviderAPIError(LLMError):
    """Provider API error."""
    pass


class ProviderNotAvailableError(LLMError):
    """Provider not available error."""
    pass


class StrategyError(LLMError):
    """Strategy error."""
    pass 


class Citation(BaseModel):
    """Citation information from Perplexity API."""
    
    url: str = Field(..., description="Source URL")
    text: str = Field(..., description="Cited text")
    title: Optional[str] = Field(None, description="Source title")
    published_date: Optional[datetime] = Field(None, description="Publication date")


class PerplexityMetadata(BaseModel):
    """Metadata from Perplexity API response."""
    
    provider: ProviderType = ProviderType.PERPLEXITY
    strategy: StrategyType = StrategyType.SINGLE
    model: str
    created: int
    usage: TokenUsage
    citations: List[Citation] = []
    raw_response: Dict[str, Any]
    finish_reason: Optional[str] = None
    latency: float = 0.0
    related_questions: List[str] = []
    images: List[str] = []


class PerplexityResponse(LLMResponse):
    """Extended response for Perplexity provider."""
    
    metadata: PerplexityMetadata = Field(..., description="Perplexity-specific metadata") 


class RelatedQuestionsGenerator(BaseModel):
    """Generator for structured follow-up questions"""
    
    system_prompt: str = Field(
        default="""You are a follow-up question generator that helps users explore topics deeper.

RULES:
1. Generate exactly 3 follow-up questions
2. Questions must be non-trivial and help continue the conversation
3. Return questions in clean JSON format:
{
  "follow_up_questions": [
    {
      "question": "text of the question?",
      "intent": "brief explanation of why this question is helpful",
      "exploration_path": "what topic branch this opens"
    }
  ]
}

QUESTION STRUCTURE:
1. First question: Dive deeper into the main topic
2. Second question: Explore related aspects or context
3. Third question: Connect to broader implications or practical applications

GUIDELINES:
- Questions should be open-ended
- Each question should open a new conversation branch
- Use the same language as the original question
- No formatting, just clean text with ? at the end
- Questions should feel natural in conversation""",
        description="System prompt for generating follow-up questions"
    )
    max_questions: int = Field(
        default=3,
        description="Maximum number of questions"
    )
    temperature: float = Field(
        default=0.7,
        description="Generation temperature"
    )
        
    def format_prompt(self, question: str) -> str:
        """Format prompt for the model."""
        return f"Original question: {question}\nGenerate 3 follow-up questions in JSON format:"
        
    def parse_response(self, text: str) -> List[str]:
        """Parse model response into list of questions."""
        try:
            # Try to parse JSON response
            data = json.loads(text)
            questions = []
            
            if "follow_up_questions" in data:
                for q in data["follow_up_questions"]:
                    if isinstance(q, dict) and "question" in q:
                        questions.append(q["question"])
            
            # If we got valid questions, return them
            if len(questions) > 0:
                return questions[:3]
                
        except json.JSONDecodeError:
            pass
            
        # Fallback: try to extract questions from text
        questions = [
            q.strip() for q in text.split('\n') 
            if q.strip() and '?' in q and not q.startswith('-') and not q.startswith('*')
        ]
        return questions[:3]


class RelatedQuestionsConfig(BaseModel):
    """Конфигурация для генерации связанных вопросов"""
    
    enabled: bool = Field(
        default=True,
        description="Включена ли генерация вопросов"
    )
    generator: RelatedQuestionsGenerator = Field(
        default_factory=RelatedQuestionsGenerator,
        description="Генератор вопросов"
    )


class RelatedQuestion(BaseModel):
    """Модель для связанного вопроса"""
    
    text: str = Field(..., description="Текст вопроса")
    confidence: float = Field(default=1.0, description="Уверенность в релевантности вопроса (0-1)")
    source: str = Field(default="generated", description="Источник вопроса (api/generated)")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Дополнительные метаданные")


class RelatedQuestionsResponse(BaseModel):
    """Ответ API для связанных вопросов"""
    
    questions: List[RelatedQuestion] = Field(default_factory=list, description="Список связанных вопросов")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Метаданные ответа")


class RelatedQuestionsRequest(BaseModel):
    """Запрос для получения связанных вопросов"""
    
    original_question: str = Field(..., description="Исходный вопрос")
    config: Optional[RelatedQuestionsConfig] = Field(
        default=None,
        description="Конфигурация генерации вопросов"
    )
    max_questions: int = Field(default=5, description="Максимальное количество вопросов")
    min_confidence: float = Field(
        default=0.5,
        description="Минимальная уверенность для включения вопроса"
    ) 