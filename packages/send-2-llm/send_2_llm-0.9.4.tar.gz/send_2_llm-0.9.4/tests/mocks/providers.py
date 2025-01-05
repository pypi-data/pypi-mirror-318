"""Mock providers for testing."""

from typing import Optional, Any
from send_2_llm.types import (
    LLMResponse,
    LLMMetadata,
    ProviderType,
    LLMRequest,
    TokenUsage,
    StrategyType
)
from send_2_llm.providers.base import BaseLLMProvider

class MockTogetherProvider(BaseLLMProvider):
    """Mock Together AI provider for testing."""
    
    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ):
        """Initialize provider."""
        super().__init__()
        self.model = model or "mistralai/Mixtral-8x7B-Instruct-v0.1"
        self.temperature = temperature or 0.7
        self.top_p = top_p or 0.95
        self.max_tokens = max_tokens or 512
        self.kwargs = kwargs
    
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate mock response."""
        prompt_tokens = len(request.prompt.split())
        completion_tokens = 28
        
        metadata = LLMMetadata(
            provider=ProviderType.TOGETHER,
            model=self.model,
            task_type="generate",
            strategy=StrategyType.SINGLE,
            usage=TokenUsage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
                cost=0.0
            )
        )
        
        return LLMResponse(
            text="Мягкий котик на окошке\nГреет лапки на дорожке\nМурлыкает песню свою\nЯ его очень люблю",
            metadata=metadata
        )

class MockOpenAIProvider(BaseLLMProvider):
    """Mock OpenAI provider for testing."""
    
    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs: Any
    ):
        """Initialize provider."""
        super().__init__()
        self.model = model or "gpt-4o-mini-2024-07-18"
        self.temperature = temperature or 0.7
        self.top_p = top_p or 0.95
        self.max_tokens = max_tokens or 512
        self.kwargs = kwargs
    
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate mock response."""
        return LLMResponse(
            text="Пушистый кот мурлычет сладко,\nНа солнце греется украдкой.\nОн дремлет целый день подряд,\nИ жизни он безмерно рад.",
            metadata=LLMMetadata(
                provider=ProviderType.OPENAI,
                model=self.model,
                tokens_prompt=len(request.prompt.split()),
                tokens_completion=32,
                tokens_total=len(request.prompt.split()) + 32
            )
        ) 