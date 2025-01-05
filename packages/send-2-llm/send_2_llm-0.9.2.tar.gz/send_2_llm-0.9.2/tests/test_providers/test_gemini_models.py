import pytest
from unittest.mock import Mock, patch

from send_2_llm.providers.gemini import GeminiProvider
from send_2_llm.types import LLMRequest, ProviderType

class TestGeminiModels:
    @pytest.fixture
    def provider(self):
        return GeminiProvider()
        
    @pytest.mark.asyncio
    async def test_gemini_pro_vision(self, provider):
        """Test Gemini Pro Vision model with image input"""
        request = LLMRequest(
            prompt="Describe this image",
            provider_type=ProviderType.GEMINI,
            model="gemini-pro-vision",
            extra_params={
                "image_data": "base64_encoded_image_data"
            }
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_response = Mock()
            mock_response.text = "Image description"
            mock_model.return_value.generate_content.return_value = mock_response
            
            response = await provider._generate(request)
            assert response.text == "Image description"
            
    @pytest.mark.asyncio        
    async def test_gemini_ultra(self, provider):
        """Test Gemini Ultra model capabilities"""
        request = LLMRequest(
            prompt="Complex reasoning task",
            provider_type=ProviderType.GEMINI,
            model="gemini-1.5-ultra",
            temperature=0.1  # Lower temperature for more focused output
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_response = Mock()
            mock_response.text = "Detailed analytical response"
            mock_model.return_value.generate_content.return_value = mock_response
            
            response = await provider._generate(request)
            assert response.text == "Detailed analytical response"
            
    @pytest.mark.asyncio
    async def test_streaming_response(self, provider):
        """Test streaming response capability"""
        request = LLMRequest(
            prompt="Generate long response",
            provider_type=ProviderType.GEMINI,
            model="gemini-1.5-pro",
            extra_params={"stream": True}
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_chunks = [
                Mock(text="Chunk 1"),
                Mock(text="Chunk 2"),
                Mock(text="Chunk 3")
            ]
            mock_model.return_value.generate_content.return_value = mock_chunks
            
            response = await provider._generate(request)
            assert all(chunk in response.text for chunk in ["Chunk 1", "Chunk 2", "Chunk 3"])
            
    @pytest.mark.asyncio
    async def test_function_calling(self, provider):
        """Test function calling capabilities"""
        tools = [{
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "location": "string",
                "date": "string"
            }
        }]
        
        request = LLMRequest(
            prompt="What's the weather in Moscow?",
            provider_type=ProviderType.GEMINI,
            model="gemini-1.5-pro",
            extra_params={"tools": tools}
        )
        
        with patch('google.generativeai.GenerativeModel') as mock_model:
            mock_response = Mock()
            mock_response.text = "Function call response"
            mock_response.function_call = {
                "name": "get_weather",
                "arguments": {"location": "Moscow", "date": "today"}
            }
            mock_model.return_value.generate_content.return_value = mock_response
            
            response = await provider._generate(request)
            assert "function_call" in response.metadata.raw_response 