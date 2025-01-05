"""Tests for Gemini provider."""

import os
from datetime import datetime
import pytest
from unittest.mock import patch, MagicMock, Mock

from send_2_llm.types import (
    ProviderType,
    LLMRequest,
    LLMResponse,
    ProviderAPIError,
    RetryConfig
)
from send_2_llm.providers.gemini import GeminiProvider


class TestGeminiProvider:
    @pytest.fixture
    def provider(self):
        return GeminiProvider()
        
    @pytest.fixture
    def mock_genai(self):
        with patch('google.generativeai') as mock:
            yield mock
            
    @pytest.mark.asyncio
    async def test_basic_generation(self, provider, mock_genai):
        """Test basic text generation"""
        request = LLMRequest(
            prompt="Test prompt",
            provider_type=ProviderType.GEMINI,
            model="gemini-1.5-pro",
            temperature=0.7
        )
        
        mock_response = Mock()
        mock_response.text = "Generated response"
        mock_genai.GenerativeModel().generate_content.return_value = mock_response
        
        response = await provider._generate(request)
        assert response.text == "Generated response"
        
    @pytest.mark.asyncio
    async def test_retry_on_rate_limit(self, provider, mock_genai):
        """Test retry logic on rate limit error"""
        request = LLMRequest(
            prompt="Test prompt",
            retry_config=RetryConfig(
                max_retries=2,
                initial_delay=0.1
            )
        )
        
        # Mock rate limit error then success
        mock_genai.GenerativeModel().generate_content.side_effect = [
            Exception("Rate limit exceeded"),
            Mock(text="Success after retry")
        ]
        
        response = await provider._generate(request)
        assert response.text == "Success after retry"
        assert mock_genai.GenerativeModel().generate_content.call_count == 2

    @pytest.mark.asyncio
    async def test_safety_filters(self, provider, mock_genai):
        """Test safety filter handling"""
        request = LLMRequest(
            prompt="Test prompt with safety check"
        )
        
        mock_response = Mock()
        mock_response.text = "Safe response"
        mock_response.safety_ratings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "probability": "NEGLIGIBLE"}
        ]
        
        mock_genai.GenerativeModel().generate_content.return_value = mock_response
        
        response = await provider._generate(request)
        assert response.text == "Safe response"
        assert "safety_ratings" in response.metadata.raw_response 