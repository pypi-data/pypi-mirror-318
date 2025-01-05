import pytest
from unittest.mock import Mock, patch
import google.generativeai as genai

from send_2_llm.providers.gemini import GeminiProvider
from send_2_llm.types import LLMRequest, ProviderAPIError, RetryConfig

class TestGeminiErrors:
    @pytest.fixture
    def provider(self):
        return GeminiProvider()
        
    @pytest.mark.asyncio
    async def test_api_key_error(self):
        """Test handling of missing API key"""
        with patch.dict('os.environ', clear=True):
            with pytest.raises(ProviderAPIError) as exc:
                GeminiProvider()
            assert "GEMINI_API_KEY not found" in str(exc.value)
            
    @pytest.mark.asyncio
    async def test_rate_limit_with_retry(self, provider):
        """Test rate limit handling with retry logic"""
        request = LLMRequest(
            prompt="Test prompt",
            retry_config=RetryConfig(
                max_retries=2,
                initial_delay=0.1
            )
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.generate_content.side_effect = [
                genai.types.BlockedPromptException("Rate limit"),
                Mock(text="Success")
            ]
            
            response = await provider._generate(request)
            assert response.text == "Success"
            assert response.metadata.retry_count == 1
            
    @pytest.mark.asyncio
    async def test_safety_filter_block(self, provider):
        """Test handling of content blocked by safety filters"""
        request = LLMRequest(
            prompt="Potentially unsafe content"
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.generate_content.side_effect = \
                genai.types.BlockedPromptException("Content blocked")
            
            with pytest.raises(ProviderAPIError) as exc:
                await provider._generate(request)
            assert "Content blocked" in str(exc.value)
            
    @pytest.mark.asyncio
    async def test_invalid_model(self, provider):
        """Test handling of invalid model specification"""
        request = LLMRequest(
            prompt="Test prompt",
            model="non-existent-model"
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.generate_content.side_effect = \
                ValueError("Invalid model")
            
            with pytest.raises(ProviderAPIError) as exc:
                await provider._generate(request)
            assert "Invalid model" in str(exc.value)
            
    @pytest.mark.asyncio
    async def test_network_error_retry(self, provider):
        """Test handling of network errors with retry"""
        request = LLMRequest(
            prompt="Test prompt",
            retry_config=RetryConfig(
                max_retries=3,
                initial_delay=0.1
            )
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.generate_content.side_effect = [
                ConnectionError("Network error"),
                ConnectionError("Network error"),
                Mock(text="Success")
            ]
            
            response = await provider._generate(request)
            assert response.text == "Success"
            assert response.metadata.retry_count == 2
            
    @pytest.mark.asyncio
    async def test_max_retries_exceeded(self, provider):
        """Test behavior when max retries are exceeded"""
        request = LLMRequest(
            prompt="Test prompt",
            retry_config=RetryConfig(
                max_retries=2,
                initial_delay=0.1
            )
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.generate_content.side_effect = \
                ConnectionError("Persistent network error")
            
            with pytest.raises(ProviderAPIError) as exc:
                await provider._generate(request)
            assert "Max retries exceeded" in str(exc.value) 