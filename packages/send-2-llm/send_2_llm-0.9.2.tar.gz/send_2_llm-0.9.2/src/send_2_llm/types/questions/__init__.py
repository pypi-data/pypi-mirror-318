"""Types for handling related questions functionality."""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field


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
        description="Temperature for question generation"
    )

    def format_prompt(self, question: str) -> str:
        """Format the prompt for question generation."""
        return f"Original question: {question}\n\nGenerate follow-up questions following the rules above."

    def parse_response(self, text: str) -> List[str]:
        """Parse the response into a list of questions."""
        try:
            import json
            data = json.loads(text)
            questions = []
            for q in data.get("follow_up_questions", []):
                if isinstance(q, dict) and "question" in q:
                    questions.append(q["question"])
                elif isinstance(q, str):
                    questions.append(q)
            return questions[:self.max_questions]
        except:
            return []


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