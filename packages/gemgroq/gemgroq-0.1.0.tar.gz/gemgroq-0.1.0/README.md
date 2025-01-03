# Gemgroq API

A unified API interface that combines both Groq and Google's Gemini AI models into a single, easy-to-use package.

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Create a `.env` file in your project root with your API keys:

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
```

## Usage

```python
from gemgroq import GemgroqAPI

# Initialize the API
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
- Easy switching between models
- Consistent response format
- Error handling and retries
- Environment variable based configuration

## Supported Models

- Groq: mixtral-8x7b-32768, llama2-70b-4096
- Gemini: gemini-pro

## License

MIT
