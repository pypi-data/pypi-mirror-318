import os
from typing import Optional, Dict, Any, List
import groq
import google.generativeai as genai
from dotenv import load_dotenv
from .config import get_api_keys

class GemgroqAPI:
    """
    A unified API interface for both Groq and Gemini AI models.
    """
    
    def __init__(self, groq_api_key: Optional[str] = None, gemini_api_key: Optional[str] = None):
        """
        Initialize the API with either environment variables, direct API keys, or interactive setup.
        
        Args:
            groq_api_key (Optional[str]): Groq API key. If None, will look for saved key or prompt
            gemini_api_key (Optional[str]): Gemini API key. If None, will look for saved key or prompt
        """
        # Try to get keys from parameters, then environment, then saved config
        if groq_api_key is None or gemini_api_key is None:
            load_dotenv()
            saved_groq_key, saved_gemini_key = get_api_keys()
            
            groq_api_key = groq_api_key or os.getenv('GROQ_API_KEY') or saved_groq_key
            gemini_api_key = gemini_api_key or os.getenv('GEMINI_API_KEY') or saved_gemini_key
        
        # Initialize Groq
        self.groq_client = groq.Client(api_key=groq_api_key)
        
        # Initialize Gemini
        genai.configure(api_key=gemini_api_key)
        self.gemini_model = genai.GenerativeModel('gemini-pro')
        
        # Available models
        self.groq_models = ["mixtral-8x7b-32768", "llama2-70b-4096"]
        self.gemini_models = ["gemini-pro"]
        
    def generate(
        self,
        prompt: str,
        model: str = "groq",
        model_name: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """
        Generate a response using either Groq or Gemini model.
        
        Args:
            prompt (str): The input prompt
            model (str): Either "groq" or "gemini"
            model_name (str, optional): Specific model name
            temperature (float): Controls randomness (0-1)
            max_tokens (int, optional): Maximum tokens in response
            **kwargs: Additional model-specific parameters
            
        Returns:
            str: Generated response
            
        Raises:
            ValueError: If model type is invalid or API keys are missing
            Exception: For other API-related errors
        """
        try:
            if model.lower() == "groq":
                return self._generate_groq(prompt, model_name, temperature, max_tokens, **kwargs)
            elif model.lower() == "gemini":
                return self._generate_gemini(prompt, temperature, max_tokens, **kwargs)
            else:
                raise ValueError(f"Unknown model type: {model}. Use 'groq' or 'gemini'")
        except Exception as e:
            raise Exception(f"Error generating response: {str(e)}")

    def _generate_groq(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """Generate response using Groq API."""
        if model_name is None:
            model_name = self.groq_models[0]
        
        if model_name not in self.groq_models:
            raise ValueError(f"Invalid Groq model. Choose from: {self.groq_models}")
            
        completion = self.groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens if max_tokens else 1024,
            **kwargs
        )
        
        return completion.choices[0].message.content

    def _generate_gemini(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """Generate response using Gemini API."""
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens if max_tokens else 1024,
            **kwargs
        }
        
        response = self.gemini_model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        return response.text

    def list_models(self) -> Dict[str, List[str]]:
        """
        List all available models.
        
        Returns:
            Dict[str, List[str]]: Dictionary of available models for each provider
        """
        return {
            "groq": self.groq_models,
            "gemini": self.gemini_models
        }
