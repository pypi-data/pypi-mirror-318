"""Tests for the ImageTokenCalculator class."""

import os
from pathlib import Path

import pytest
from PIL import Image
import numpy as np

from image_token_calculator import ImageTokenCalculator

# Get the path to the sample images directory
SAMPLE_IMAGES_DIR = Path("examples/sample_images")

def test_calculator_initialization():
    """Test basic calculator initialization."""
    calc = ImageTokenCalculator()
    assert calc.default_model == "claude-3-sonnet"
    assert calc.detail_level == "high"

def test_calculator_with_invalid_model():
    """Test initialization with invalid model."""
    with pytest.raises(ValueError):
        ImageTokenCalculator(default_model="invalid-model")

@pytest.mark.parametrize("model", [
    "claude-3-sonnet",
    "claude-3-opus",
    "gpt-4-vision",
    "gemini-1.5-pro"
])
def test_supported_models(model):
    """Test that all supported models work."""
    calc = ImageTokenCalculator(default_model=model)
    # Use the first sample image
    image_path = next(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    tokens = calc.calculate(image_path)
    assert tokens > 0
    
    # Test cost calculation
    cost = calc.get_cost(tokens)
    assert cost > 0

def test_batch_processing():
    """Test batch processing of images."""
    calc = ImageTokenCalculator()
    # Get all sample images
    image_paths = list(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    tokens = calc.calculate_batch(image_paths)
    assert len(tokens) == len(image_paths)
    assert all(t > 0 for t in tokens)

def test_different_input_formats():
    """Test different input formats."""
    calc = ImageTokenCalculator()
    image_path = next(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    
    # Test with file path as string
    tokens_str = calc.calculate(str(image_path))
    assert tokens_str > 0
    
    # Test with Path object
    tokens_path = calc.calculate(image_path)
    assert tokens_path == tokens_str
    
    # Test with numpy array
    with Image.open(image_path) as img:
        np_array = np.array(img)
    tokens_np = calc.calculate(np_array)
    assert tokens_np > 0
    
    # Test with PIL Image
    with Image.open(image_path) as img:
        tokens_pil = calc.calculate(img)
    assert tokens_pil == tokens_str

def test_detail_levels():
    """Test different detail levels with OpenAI models."""
    calc = ImageTokenCalculator(default_model="gpt-4-vision")
    image_path = next(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    
    # High detail should use more tokens than low detail
    high_detail = calc.calculate(image_path, detail_level="high")
    low_detail = calc.calculate(image_path, detail_level="low")
    assert high_detail > low_detail

def test_invalid_image():
    """Test handling of invalid images."""
    calc = ImageTokenCalculator()
    
    # Test non-existent file
    with pytest.raises(ValueError):
        calc.calculate("nonexistent.jpg")
    
    # Test invalid numpy array (1D array)
    invalid_array = np.zeros(10)  # 1D array is not a valid image
    with pytest.raises(ValueError):
        calc.calculate(invalid_array)
    
    # Test invalid numpy array (4D array)
    invalid_array_4d = np.zeros((10, 10, 10, 10))  # 4D array is not a valid image
    with pytest.raises(ValueError):
        calc.calculate(invalid_array_4d)
    
    # Test invalid input type
    with pytest.raises(ValueError):
        calc.calculate(123)  # Integer is not a valid image input

def test_large_image_scaling():
    """Test that large images are properly scaled."""
    calc = ImageTokenCalculator()
    # Create a large test image
    large_image = Image.new('RGB', (4096, 4096))
    tokens = calc.calculate(large_image)
    assert tokens > 0  # Should handle large images without errors 