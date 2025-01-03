"""
Gemgroq - A unified API interface for Groq and Google's Gemini AI models
"""

from .api import GemgroqAPI
from .config import setup_keys, get_api_keys

__version__ = "0.1.2"
__all__ = ["GemgroqAPI", "setup_keys", "get_api_keys"]
