"""Main package interface."""

from typing import List, Optional, Union
import asyncio

from .client import LLMClient
from .types import ProviderType, LLMResponse, LLMRequest, StrategyType, OutputFormat

__version__ = "0.1.0"

async def send_2_llm(
    text: str,
    strategy_type: Optional[StrategyType] = None,
    provider_type: Optional[ProviderType] = None,
    providers: Optional[List[ProviderType]] = None,
    model: Optional[str] = None,
    models: Optional[List[str]] = None,
    output_format: Optional[OutputFormat] = None,
    **kwargs
) -> LLMResponse:
    """Основной метод для отправки текста в LLM.
    
    Args:
        text: Текст для отправки в LLM
        strategy_type: Тип стратегии (если нужно переопределить)
        provider_type: Провайдер для single strategy
        providers: Список провайдеров для других стратегий
        model: Модель для single strategy
        models: Список моделей для других стратегий
        output_format: Формат вывода (text, markdown, html, json)
        **kwargs: Дополнительные параметры для провайдера
        
    Returns:
        LLMResponse с ответом от модели
        
    Examples:
        >>> response = await send_2_llm("Привет, как дела?")
        >>> print(response.text)
        
        >>> # С переопределением стратегии
        >>> response = await send_2_llm(
        ...     "Сложный вопрос",
        ...     strategy_type=StrategyType.FALLBACK,
        ...     providers=[ProviderType.TOGETHER, ProviderType.OPENAI]
        ... )
        
        >>> # С форматированием в markdown
        >>> response = await send_2_llm(
        ...     "Создай список преимуществ Python",
        ...     output_format=OutputFormat.MARKDOWN
        ... )
    """
    async with LLMClient(
        strategy_type=strategy_type,
        provider_type=provider_type,
        providers=providers,
        model=model,
        models=models,
        **kwargs
    ) as client:
        if output_format and output_format != OutputFormat.RAW:
            if output_format == OutputFormat.MARKDOWN:
                text = f"{text}\n\nОтвет должен быть отформатирован в стандартном markdown."
            elif output_format == OutputFormat.TELEGRAM_MARKDOWN:
                text = f"{text}\n\nОтвет должен быть отформатирован в markdown для Telegram (поддерживаются *bold*, _italic_, `code`, ```pre```, [text](URL))."
            elif output_format == OutputFormat.HTML:
                text = f"{text}\n\nОтвет должен быть отформатирован в HTML."
            elif output_format == OutputFormat.JSON:
                text = f"{text}\n\nОтвет должен быть в формате JSON."
        
        return await client.generate(text)

def send_2_llm_sync(
    text: str,
    strategy_type: Optional[StrategyType] = None,
    provider_type: Optional[ProviderType] = None,
    providers: Optional[List[ProviderType]] = None,
    model: Optional[str] = None,
    models: Optional[List[str]] = None,
    output_format: Optional[OutputFormat] = None,
    **kwargs
) -> LLMResponse:
    """
    Синхронная версия send_2_llm.
    Позволяет использовать библиотеку без async/await.
    
    Пример:
        from send_2_llm import send_2_llm_sync
        
        response = send_2_llm_sync("Привет!")
        print(response.text)
    """
    return asyncio.run(send_2_llm(
        text,
        strategy_type=strategy_type,
        provider_type=provider_type,
        providers=providers,
        model=model,
        models=models,
        output_format=output_format,
        **kwargs
    ))

__all__ = [
    "send_2_llm",
    "send_2_llm_sync",
    "LLMClient",
    "ProviderType",
    "StrategyType",
    "OutputFormat",
    "LLMResponse",
    "LLMRequest"
] 