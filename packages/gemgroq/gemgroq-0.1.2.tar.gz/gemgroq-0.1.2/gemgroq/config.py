import os
import json
from pathlib import Path
from getpass import getpass

def get_config_dir() -> Path:
    """Get the configuration directory for storing API keys."""
    config_dir = Path.home() / '.gemgroq'
    config_dir.mkdir(exist_ok=True)
    return config_dir

def get_config_file() -> Path:
    """Get the configuration file path."""
    return get_config_dir() / 'config.json'

def load_config() -> dict:
    """Load configuration from file."""
    config_file = get_config_file()
    if config_file.exists():
        with open(config_file, 'r') as f:
            return json.load(f)
    return {}

def save_config(config: dict):
    """Save configuration to file."""
    config_file = get_config_file()
    with open(config_file, 'w') as f:
        json.dump(config, f)
    
    # Set restrictive permissions
    config_file.chmod(0o600)

def setup_keys(force: bool = False) -> dict:
    """
    Interactive setup for API keys.
    
    Args:
        force (bool): If True, force new key setup even if keys exist
        
    Returns:
        dict: Configuration with API keys
    """
    config = load_config()
    
    if not force and 'groq_api_key' in config and 'gemini_api_key' in config:
        return config
        
    print("\nWelcome to Gemgroq! Let's set up your API keys.")
    print("These will be stored securely in ~/.gemgroq/config.json\n")
    
    # Get Groq API key
    if force or 'groq_api_key' not in config:
        print("Please enter your Groq API key (get it from https://console.groq.com)")
        print("It should start with 'gsk_'")
        groq_key = getpass("Groq API key: ").strip()
        if not groq_key:
            raise ValueError("Groq API key is required")
        config['groq_api_key'] = groq_key
    
    # Get Gemini API key
    if force or 'gemini_api_key' not in config:
        print("\nPlease enter your Gemini API key (get it from https://makersuite.google.com/app/apikey)")
        gemini_key = getpass("Gemini API key: ").strip()
        if not gemini_key:
            raise ValueError("Gemini API key is required")
        config['gemini_api_key'] = gemini_key
    
    # Save configuration
    save_config(config)
    print("\nAPI keys have been saved successfully!")
    
    return config

def get_api_keys() -> tuple[str, str]:
    """
    Get API keys, prompting for setup if necessary.
    
    Returns:
        tuple[str, str]: (groq_api_key, gemini_api_key)
    """
    config = setup_keys()
    return config['groq_api_key'], config['gemini_api_key']
