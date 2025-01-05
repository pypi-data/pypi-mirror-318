import pytest
from unittest.mock import Mock, patch
import google.generativeai as genai

from send_2_llm.providers.gemini import GeminiProvider
from send_2_llm.types import LLMRequest, ProviderType

class TestGeminiFlash:
    @pytest.fixture
    def provider(self):
        return GeminiProvider()
        
    @pytest.fixture
    def default_config(self):
        return {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain"
        }
        
    @pytest.mark.asyncio
    async def test_flash_model_initialization(self, provider, default_config):
        """Test initialization of Gemini 2.0 Flash model with default config"""
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.start_chat.return_value = Mock()
            
            request = LLMRequest(
                prompt="Test prompt",
                provider_type=ProviderType.GEMINI,
                model="gemini-2.0-flash-exp"
            )
            
            await provider._generate(request)
            
            mock_model.assert_called_once_with(
                model_name="gemini-2.0-flash-exp",
                generation_config=default_config
            )
            
    @pytest.mark.asyncio
    async def test_chat_session_handling(self, provider):
        """Test chat session creation and message handling"""
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_chat = Mock()
            mock_chat.send_message.return_value = Mock(text="Response text")
            mock_model.return_value.start_chat.return_value = mock_chat
            
            request = LLMRequest(
                prompt="Test prompt",
                provider_type=ProviderType.GEMINI,
                model="gemini-2.0-flash-exp"
            )
            
            response = await provider._generate(request)
            
            assert response.text == "Response text"
            mock_chat.send_message.assert_called_once_with("Test prompt")
            
    @pytest.mark.asyncio
    async def test_custom_generation_config(self, provider):
        """Test custom generation configuration"""
        custom_config = {
            "temperature": 0.5,
            "top_p": 0.8,
            "top_k": 20,
            "max_output_tokens": 4096
        }
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.start_chat.return_value = Mock()
            
            request = LLMRequest(
                prompt="Test prompt",
                provider_type=ProviderType.GEMINI,
                model="gemini-2.0-flash-exp",
                temperature=0.5,
                top_p=0.8,
                top_k=20,
                max_tokens=4096
            )
            
            await provider._generate(request)
            
            called_config = mock_model.call_args[1]['generation_config']
            assert called_config["temperature"] == custom_config["temperature"]
            assert called_config["top_p"] == custom_config["top_p"]
            assert called_config["top_k"] == custom_config["top_k"]
            assert called_config["max_output_tokens"] == custom_config["max_output_tokens"]
            
    @pytest.mark.asyncio
    async def test_mime_type_handling(self, provider):
        """Test response MIME type handling"""
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_model.return_value.start_chat.return_value = Mock()
            
            request = LLMRequest(
                prompt="Test prompt",
                provider_type=ProviderType.GEMINI,
                model="gemini-2.0-flash-exp",
                response_format="text/markdown"
            )
            
            await provider._generate(request)
            
            called_config = mock_model.call_args[1]['generation_config']
            assert called_config["response_mime_type"] == "text/markdown" 