"""Tests for Perplexity web search functionality."""

import pytest
from unittest.mock import patch, MagicMock
from send_2_llm.providers.perplexity import PerplexityProvider
from send_2_llm.types import LLMRequest, ProviderType


@pytest.mark.asyncio
async def test_web_search_integration():
    """Test web search integration."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="What's new in Python 3.12?",
            extra_params={
                "search_domain_filter": ["python.org", "docs.python.org"],
                "search_recency_filter": "1y"
            }
        )
        
        mock_response = {
            "choices": [{
                "message": {"content": "Python 3.12 includes:..."}
            }],
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 50,
                "total_tokens": 60
            },
            "citations": [
                {"url": "https://docs.python.org/3.12/whatsnew/3.12.html"},
                {"url": "https://python.org/downloads/release/python-3120/"}
            ]
        }
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.return_value = MagicMock(**mock_response)
            
            response = await provider._generate(request)
            
            # Check that web search parameters were passed
            call_args = mock_client.return_value.chat.completions.create.call_args[1]
            assert call_args["search_domain_filter"] == ["python.org", "docs.python.org"]
            assert call_args["search_recency_filter"] == "1y"
            
            # Check response
            assert "Python 3.12" in response.text
            assert len(response.metadata.citations) == 2
            assert all(c.url.startswith("https://") for c in response.metadata.citations)


@pytest.mark.asyncio
async def test_web_search_with_related_questions():
    """Test web search with related questions."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="What is quantum computing?",
            extra_params={
                "return_related_questions": True
            }
        )
        
        mock_response = {
            "choices": [{
                "message": {"content": "Quantum computing is..."}
            }],
            "usage": {
                "prompt_tokens": 5,
                "completion_tokens": 40,
                "total_tokens": 45
            },
            "related_questions": [
                "How does quantum entanglement work?",
                "What are qubits?",
                "When will quantum computers be practical?"
            ]
        }
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.return_value = MagicMock(**mock_response)
            
            response = await provider._generate(request)
            
            # Check that related questions were requested
            call_args = mock_client.return_value.chat.completions.create.call_args[1]
            assert call_args["return_related_questions"] is True
            
            # Check response
            assert "quantum" in response.text.lower()
            assert len(response.metadata.related_questions) == 3
            assert any("entanglement" in q.text.lower() for q in response.metadata.related_questions)


@pytest.mark.asyncio
async def test_web_search_error_handling():
    """Test web search error handling."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="Invalid search",
            extra_params={
                "search_domain_filter": "invalid_filter",  # Should be list
                "search_recency_filter": "invalid_period"
            }
        )
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.side_effect = ValueError("Invalid search parameters")
            
            with pytest.raises(Exception) as exc_info:
                await provider._generate(request)
            
            assert "Invalid search parameters" in str(exc_info.value)


@pytest.mark.asyncio
async def test_web_search_with_images():
    """Test web search with image results."""
    with patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'test_key'}):
        provider = PerplexityProvider()
        
        request = LLMRequest(
            prompt="Show me pictures of quantum computers",
            extra_params={
                "return_images": True
            }
        )
        
        mock_response = {
            "choices": [{
                "message": {"content": "Here are some quantum computers:..."}
            }],
            "usage": {
                "prompt_tokens": 7,
                "completion_tokens": 30,
                "total_tokens": 37
            },
            "images": [
                {"url": "https://example.com/quantum1.jpg"},
                {"url": "https://example.com/quantum2.jpg"}
            ]
        }
        
        with patch('openai.AsyncOpenAI') as mock_client:
            mock_client.return_value.chat.completions.create.return_value = MagicMock(**mock_response)
            
            response = await provider._generate(request)
            
            # Check that images were requested
            call_args = mock_client.return_value.chat.completions.create.call_args[1]
            assert call_args["return_images"] is True
            
            # Check response
            assert "quantum computers" in response.text.lower()
            assert len(response.metadata.images) == 2
            assert all(img.url.endswith(".jpg") for img in response.metadata.images) 