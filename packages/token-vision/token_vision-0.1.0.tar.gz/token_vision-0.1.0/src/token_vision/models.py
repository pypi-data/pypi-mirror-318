"""
Model configurations and constants for Token Vision.
This module contains the definitions of supported AI models and their token calculation parameters.
"""

import json
from pathlib import Path
from typing import Dict, TypedDict, Literal, Optional, Union

class ModelRate(TypedDict, total=False):
    """Token rate configuration for a model."""
    name: str
    input_rate: float
    output_rate: float  # Optional for models that don't have output costs
    batch_input_rate: Optional[float]  # Optional batch processing rate
    batch_output_rate: Optional[float]  # Optional batch processing rate
    cached_input_rate: Optional[float]  # Optional cached input rate

class ModelConfig(TypedDict):
    """Configuration for a model provider."""
    name: str
    max_images: int
    models: Dict[str, ModelRate]

# Supported model types
ModelProvider = Literal["claude", "openai", "gemini", "custom"]
DetailLevel = Literal["high", "low"]

# Default model configurations
DEFAULT_MODELS: Dict[ModelProvider, ModelConfig] = {
    "claude": {
        "name": "Claude",
        "max_images": 3000,
        "models": {
            "claude-3-sonnet": {
                "name": "Claude 3.5 Sonnet",
                "input_rate": 0.003,
                "output_rate": 0.015
            },
            "claude-3-haiku": {
                "name": "Claude 3.5 Haiku",
                "input_rate": 0.0008,
                "output_rate": 0.004
            },
            "claude-3-opus": {
                "name": "Claude 3 Opus",
                "input_rate": 0.015,
                "output_rate": 0.075
            }
        }
    },
    "openai": {
        "name": "OpenAI",
        "max_images": 1,
        "models": {
            "gpt-4o": {
                "name": "GPT-4o",
                "input_rate": 0.0025,
                "output_rate": 0.01,
                "batch_input_rate": 0.00125,
                "batch_output_rate": 0.005,
                "cached_input_rate": 0.00125
            },
            "gpt-4o-2024-11-20": {
                "name": "GPT-4o (Nov 2024)",
                "input_rate": 0.0025,
                "output_rate": 0.01,
                "batch_input_rate": 0.00125,
                "batch_output_rate": 0.005,
                "cached_input_rate": 0.00125
            },
            "gpt-4o-2024-08-06": {
                "name": "GPT-4o (Aug 2024)",
                "input_rate": 0.0025,
                "output_rate": 0.01,
                "batch_input_rate": 0.00125,
                "batch_output_rate": 0.005,
                "cached_input_rate": 0.00125
            },
            "gpt-4o-2024-05-13": {
                "name": "GPT-4o (May 2024)",
                "input_rate": 0.005,
                "output_rate": 0.015,
                "batch_input_rate": 0.0025,
                "batch_output_rate": 0.0075
            }
        }
    },
    "gemini": {
        "name": "Google Gemini",
        "max_images": 3000,
        "models": {
            "gemini-1.5-pro": {
                "name": "Gemini 1.5 Pro",
                "input_rate": 0.00125,
                "output_rate": 0.005
            },
            "gemini-1.5-flash": {
                "name": "Gemini 1.5 Flash",
                "input_rate": 0.000075,
                "output_rate": 0.0003
            }
        }
    }
}

# Global models configuration
MODELS = DEFAULT_MODELS.copy()

def load_custom_models(file_path: Union[str, Path]) -> None:
    """Load custom model configurations from a JSON file.
    
    Args:
        file_path: Path to the JSON configuration file
        
    The JSON file should follow the same structure as the DEFAULT_MODELS dictionary.
    Custom models will be merged with default models, overwriting any duplicates.
    
    Example JSON structure:
    {
        "provider_name": {
            "name": "Provider Display Name",
            "max_images": 1,
            "models": {
                "model-id": {
                    "name": "Model Display Name",
                    "input_rate": 0.001,
                    "output_rate": 0.002
                }
            }
        }
    }
    """
    try:
        with open(file_path, 'r') as f:
            custom_models = json.load(f)
        
        # Validate and merge custom models
        for provider, config in custom_models.items():
            if not isinstance(config, dict) or not all(k in config for k in ["name", "max_images", "models"]):
                raise ValueError(f"Invalid configuration for provider: {provider}")
            
            if provider not in MODELS:
                MODELS[provider] = config
            else:
                # Update existing provider
                MODELS[provider]["models"].update(config["models"])
                
    except Exception as e:
        raise ValueError(f"Failed to load custom models: {e}")

def get_model_provider(model_name: str) -> ModelProvider:
    """Get the provider for a given model name."""
    for provider, config in MODELS.items():
        if model_name in config["models"]:
            return provider
    raise ValueError(f"Unknown model: {model_name}")

def get_model_config(model_name: str) -> ModelRate:
    """Get the configuration for a specific model."""
    provider = get_model_provider(model_name)
    return MODELS[provider]["models"][model_name]

def reset_models() -> None:
    """Reset models to default configuration."""
    global MODELS
    MODELS = DEFAULT_MODELS.copy() 