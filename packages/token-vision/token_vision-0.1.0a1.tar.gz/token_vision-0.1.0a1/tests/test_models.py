"""Tests for the models configuration module."""

import sys
import json
import tempfile
from pathlib import Path

import pytest

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from token_vision.models import (
    MODELS,
    get_model_provider,
    get_model_config,
    ModelProvider,
    DetailLevel,
    load_models,
    reset_models
)

@pytest.fixture(autouse=True)
def reset_models_after_test():
    """Reset models after each test."""
    yield
    reset_models()

def test_models_structure():
    """Test that the MODELS dictionary has the correct structure."""
    assert isinstance(MODELS, dict)
    for provider in ["anthropic", "openai", "google"]:
        assert provider in MODELS
        provider_config = MODELS[provider]
        assert "name" in provider_config
        assert "max_images" in provider_config
        assert "models" in provider_config
        assert isinstance(provider_config["models"], dict)

def test_model_rates():
    """Test that all models have valid rate configurations."""
    for provider_config in MODELS.values():
        for model_config in provider_config["models"].values():
            assert "name" in model_config
            assert "provider" in model_config
            assert "input_rate" in model_config
            assert "output_rate" in model_config
            assert isinstance(model_config["input_rate"], (int, float))
            assert isinstance(model_config["output_rate"], (int, float))
            assert model_config["input_rate"] > 0
            assert model_config["output_rate"] > 0

def test_get_model_provider():
    """Test the get_model_provider function."""
    assert get_model_provider("claude-3-opus") == "anthropic"
    assert get_model_provider("gpt-4o") == "openai"
    assert get_model_provider("gemini-1-5-pro") == "google"
    
    with pytest.raises(ValueError):
        get_model_provider("invalid-model")

def test_get_model_config():
    """Test the get_model_config function."""
    # Test Anthropic model
    claude_config = get_model_config("claude-3-opus")
    assert claude_config["name"] == "Claude 3 Opus"
    assert claude_config["provider"] == "anthropic"
    assert claude_config["input_rate"] == 15000
    assert claude_config["output_rate"] == 75000
    
    # Test OpenAI model
    openai_config = get_model_config("gpt-4o")
    assert openai_config["name"] == "GPT-4o"
    assert openai_config["provider"] == "openai"
    assert openai_config["input_rate"] == 2.5
    assert openai_config["output_rate"] == 10
    
    # Test Google model
    google_config = get_model_config("gemini-1-5-pro")
    assert google_config["name"] == "Gemini 1.5 Pro"
    assert google_config["provider"] == "google"
    assert google_config["input_rate"] == 0.3125
    assert google_config["output_rate"] == 1.25
    
    # Test invalid model
    with pytest.raises(ValueError):
        get_model_config("invalid-model")

def test_model_provider_type():
    """Test that ModelProvider type includes all providers."""
    providers: list[ModelProvider] = ["anthropic", "openai", "google"]
    for provider in providers:
        assert provider in MODELS

def test_detail_level_type():
    """Test that DetailLevel type includes valid options."""
    levels: list[DetailLevel] = ["high", "low"]
    assert len(levels) == 2

def test_max_images_constraints():
    """Test that max_images values are correctly set."""
    assert MODELS["anthropic"]["max_images"] == 3000
    assert MODELS["openai"]["max_images"] == 1
    assert MODELS["google"]["max_images"] == 3000

def test_model_name_consistency():
    """Test that model names are consistent throughout the configuration."""
    for provider, config in MODELS.items():
        for model_id, model_config in config["models"].items():
            # Model IDs should follow naming conventions
            if provider == "openai":
                assert model_id.startswith("gpt-")
            elif provider == "google":
                assert model_id.startswith("gemini-")
            else:
                assert model_id.startswith("claude-")
            
            # Names should be non-empty strings
            assert isinstance(model_config["name"], str)
            assert len(model_config["name"]) > 0

def test_load_custom_models():
    """Test loading models from a custom JSON file."""
    # Create a temporary test model configuration
    test_config = {
        "test_provider": {
            "name": "Test Provider",
            "max_images": 1000,
            "models": {
                "test-model": {
                    "name": "Test Model",
                    "provider": "test_provider",
                    "input_rate": 1.0,
                    "output_rate": 2.0,
                    "batch_input_rate": 0.5,
                    "batch_output_rate": 1.0,
                    "cached_input_rate": 0.25,
                    "cached_output_rate": 0.5
                }
            }
        }
    }
    
    # Create a temporary file and write the test configuration
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_config, f)
        test_path = Path(f.name)
    
    try:
        # Test loading the configuration
        load_models(test_path)
        
        # Verify the test model was loaded correctly
        assert "test_provider" in MODELS
        test_model = get_model_config("test-model")
        assert test_model["name"] == "Test Model"
        assert test_model["provider"] == "test_provider"
        assert test_model["input_rate"] == 1.0
        assert test_model["output_rate"] == 2.0
        assert test_model["batch_input_rate"] == 0.5
        assert test_model["batch_output_rate"] == 1.0
        assert test_model["cached_input_rate"] == 0.25
        assert test_model["cached_output_rate"] == 0.5
    finally:
        # Clean up the temporary file
        test_path.unlink() 