"""Tests for the models configuration module."""

import pytest

from image_token_calculator.models import (
    MODELS,
    get_model_provider,
    get_model_config,
    ModelProvider,
    DetailLevel
)

def test_models_structure():
    """Test that the MODELS dictionary has the correct structure."""
    assert isinstance(MODELS, dict)
    for provider in ["claude", "openai", "gemini"]:
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
            assert "input_rate" in model_config
            assert isinstance(model_config["input_rate"], (int, float))
            assert model_config["input_rate"] > 0

def test_get_model_provider():
    """Test the get_model_provider function."""
    assert get_model_provider("claude-3-sonnet") == "claude"
    assert get_model_provider("gpt-4-vision") == "openai"
    assert get_model_provider("gemini-1.5-pro") == "gemini"
    
    with pytest.raises(ValueError):
        get_model_provider("invalid-model")

def test_get_model_config():
    """Test the get_model_config function."""
    # Test Claude model
    claude_config = get_model_config("claude-3-sonnet")
    assert claude_config["name"] == "Claude 3.5 Sonnet"
    assert claude_config["input_rate"] == 0.003
    assert claude_config["output_rate"] == 0.015
    
    # Test OpenAI model
    openai_config = get_model_config("gpt-4-vision")
    assert openai_config["name"] == "GPT-4V"
    assert openai_config["input_rate"] == 0.01
    assert "output_rate" not in openai_config
    
    # Test invalid model
    with pytest.raises(ValueError):
        get_model_config("invalid-model")

def test_model_provider_type():
    """Test that ModelProvider type includes all providers."""
    providers: list[ModelProvider] = ["claude", "openai", "gemini"]
    for provider in providers:
        assert provider in MODELS

def test_detail_level_type():
    """Test that DetailLevel type includes valid options."""
    levels: list[DetailLevel] = ["high", "low"]
    assert len(levels) == 2

def test_max_images_constraints():
    """Test that max_images values are correctly set."""
    assert MODELS["claude"]["max_images"] == 3000
    assert MODELS["openai"]["max_images"] == 1
    assert MODELS["gemini"]["max_images"] == 3000

def test_model_name_consistency():
    """Test that model names are consistent throughout the configuration."""
    for provider, config in MODELS.items():
        for model_id, model_config in config["models"].items():
            # Model IDs should follow naming conventions
            if provider == "openai":
                assert model_id.startswith("gpt-")
            elif provider == "gemini":
                assert model_id.startswith("gemini-")
            else:
                assert model_id.startswith(provider)
            
            # Names should be non-empty strings
            assert isinstance(model_config["name"], str)
            assert len(model_config["name"]) > 0 