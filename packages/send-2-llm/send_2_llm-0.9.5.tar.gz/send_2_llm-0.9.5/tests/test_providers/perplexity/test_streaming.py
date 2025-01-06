"""Tests for Perplexity streaming functionality."""

import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from send_2_llm.providers.perplexity import PerplexityProvider
from send_2_llm.types import LLMRequest, ProviderType


class MockStreamResponse:
    """Mock streaming response."""
    def __init__(self, chunks):
        self.chunks = chunks
        self.current = 0
        
    def __aiter__(self):
        return self
        
    async def __anext__(self):
        if self.current >= len(self.chunks):
            raise StopAsyncIteration
        chunk = self.chunks[self.current]
        self.current += 1
        return chunk


@pytest.mark.asyncio
async def test_basic_streaming():
    """Test basic streaming functionality."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="Generate a long response",
            extra_params={"stream": True}
        )
        
        # Create mock chunks
        chunks = [
            MagicMock(choices=[MagicMock(delta=MagicMock(content="Hello"))]),
            MagicMock(choices=[MagicMock(delta=MagicMock(content=" world"))]),
            MagicMock(choices=[MagicMock(delta=MagicMock(content="!"))]),
        ]
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.return_value = MockStreamResponse(chunks)
            
            response = await provider._generate(request)
            
            # Check streaming was requested
            call_args = mock_client.return_value.chat.completions.create.call_args[1]
            assert call_args["stream"] is True
            
            # Check final response
            assert response.text == "Hello world!"


@pytest.mark.asyncio
async def test_streaming_with_function_calls():
    """Test streaming with function calls."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="What's the weather?",
            extra_params={
                "stream": True,
                "tools": [{
                    "name": "get_weather",
                    "parameters": {"location": "string"}
                }]
            }
        )
        
        # Create mock chunks with function call
        chunks = [
            MagicMock(choices=[MagicMock(delta=MagicMock(
                content=None,
                function_call=MagicMock(name="get_weather", arguments='{"location": "London"}')
            ))]),
            MagicMock(choices=[MagicMock(delta=MagicMock(content="The weather in London is"))]),
            MagicMock(choices=[MagicMock(delta=MagicMock(content=" sunny!"))]),
        ]
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.return_value = MockStreamResponse(chunks)
            
            response = await provider._generate(request)
            
            # Check response
            assert "weather in London" in response.text
            assert response.metadata.function_calls
            assert response.metadata.function_calls[0].name == "get_weather"
            assert response.metadata.function_calls[0].arguments == '{"location": "London"}'


@pytest.mark.asyncio
async def test_streaming_error_handling():
    """Test streaming error handling."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="Test streaming errors",
            extra_params={"stream": True}
        )
        
        # Create mock chunks with error
        chunks = [
            MagicMock(choices=[MagicMock(delta=MagicMock(content="Starting..."))]),
            MagicMock(choices=[MagicMock(delta=MagicMock(content=" Processing..."))]),
        ]
        
        with patch('openai.AsyncOpenAI') as mock_client:
            # Mock stream that raises error mid-way
            async def mock_stream():
                stream = MockStreamResponse(chunks)
                async for chunk in stream:
                    if stream.current == 2:  # Raise error after second chunk
                        raise ConnectionError("Stream interrupted")
                    yield chunk
                    
            mock_client.return_value.chat.completions.create.return_value = mock_stream()
            
            with pytest.raises(Exception) as exc_info:
                await provider._generate(request)
            
            assert "Stream interrupted" in str(exc_info.value)


@pytest.mark.asyncio
async def test_streaming_with_citations():
    """Test streaming with citations."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="Tell me about Python with citations",
            extra_params={"stream": True}
        )
        
        # Create mock chunks with citations
        chunks = [
            MagicMock(
                choices=[MagicMock(delta=MagicMock(content="Python is"))],
                citations=[{"url": "https://python.org/about"}]
            ),
            MagicMock(
                choices=[MagicMock(delta=MagicMock(content=" a programming language"))],
                citations=[{"url": "https://docs.python.org"}]
            ),
        ]
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.return_value = MockStreamResponse(chunks)
            
            response = await provider._generate(request)
            
            # Check response
            assert "Python is a programming language" in response.text
            assert len(response.metadata.citations) == 2
            assert any("python.org/about" in c.url for c in response.metadata.citations)
            assert any("docs.python.org" in c.url for c in response.metadata.citations) 