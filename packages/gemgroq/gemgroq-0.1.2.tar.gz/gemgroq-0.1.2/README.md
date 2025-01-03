# Gemgroq API

A unified API interface that combines both Groq and Google's Gemini AI models into a single, easy-to-use package.

## Installation

```bash
pip install gemgroq
```

## Setup

After installation, you have two ways to set up your API keys:

1. **Interactive Setup (Recommended)**:
   ```bash
   gemgroq --setup
   ```
   This will prompt you for your API keys and save them securely.

2. **Manual Setup**:
   - Create a `.env` file with your API keys:
     ```env
     GROQ_API_KEY=your_groq_api_key
     GEMINI_API_KEY=your_gemini_api_key
     ```
   - Or pass them directly in code:
     ```python
     api = GemgroqAPI(
         groq_api_key="your_groq_api_key",
         gemini_api_key="your_gemini_api_key"
     )
     ```

Get your API keys from:
- Groq: https://console.groq.com
- Gemini: https://makersuite.google.com/app/apikey

## Usage

```python
from gemgroq import GemgroqAPI

# Initialize the API (will prompt for keys if not set up)
api = GemgroqAPI()

# Get response from either model
response = api.generate(
    prompt="Tell me a joke",
    model="groq"  # or "gemini"
)

print(response)
```

## Features

- Unified interface for both Groq and Gemini models
- Interactive API key setup and secure storage
- Easy switching between models
- Consistent response format
- Error handling and retries
- Environment variable based configuration

## CLI Commands

- Set up API keys: `gemgroq --setup`
- Force update API keys: `gemgroq --setup --force`

## Supported Models

- Groq: mixtral-8x7b-32768, llama2-70b-4096
- Gemini: gemini-pro

## License

MIT
