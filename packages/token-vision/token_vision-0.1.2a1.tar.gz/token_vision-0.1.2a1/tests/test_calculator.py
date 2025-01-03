"""Tests for the ImageTokenCalculator class."""

import os
import sys
from pathlib import Path

import pytest
from PIL import Image
import numpy as np

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from token_vision import ImageTokenCalculator
from token_vision.models import get_model_config

# Get the path to the sample images directory
SAMPLE_IMAGES_DIR = Path(__file__).parent.parent / "examples" / "sample_images"

def test_calculator_initialization():
    """Test basic calculator initialization."""
    calc = ImageTokenCalculator()
    assert calc.default_model == "claude-3-opus"
    assert calc.detail_level == "high"

def test_calculator_with_invalid_model():
    """Test initialization with invalid model."""
    with pytest.raises(ValueError):
        ImageTokenCalculator(default_model="invalid-model")

@pytest.mark.parametrize("model", [
    "claude-3-opus",
    "claude-3-sonnet",
    "gpt-4o",
    "gemini-1-5-pro"
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
    
    # Verify cost calculation is using the correct rates
    config = get_model_config(model)
    expected_cost = (tokens * config["input_rate"] + tokens * config["output_rate"]) / 1000000
    assert abs(cost - expected_cost) < 0.0001  # Allow for floating point differences

def test_batch_processing():
    """Test batch processing of images."""
    calc = ImageTokenCalculator()
    # Get all sample images
    image_paths = list(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    tokens = calc.calculate_batch(image_paths)
    assert len(tokens) == len(image_paths)
    assert all(t > 0 for t in tokens)
    
    # Test batch cost calculation
    costs = calc.get_cost_batch(tokens)
    assert len(costs) == len(tokens)
    assert all(c > 0 for c in costs)
    
    # Verify batch costs are lower than regular costs
    regular_costs = [calc.get_cost(t) for t in tokens]
    assert all(b <= r for b, r in zip(costs, regular_costs))

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
    """Test different detail levels."""
    calc = ImageTokenCalculator()
    image_path = next(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    
    # High detail should use more tokens than low detail
    high_detail = calc.calculate(image_path, detail_level="high")
    low_detail = calc.calculate(image_path, detail_level="low")
    assert high_detail > low_detail
    assert low_detail == 85  # Low detail is always 85 tokens

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
    
    # Test that the token count is reasonable for a scaled image
    # After scaling, the image should be 2048x2048 or smaller
    scaled_tokens = calc.calculate(Image.new('RGB', (2048, 2048)))
    assert tokens == scaled_tokens  # Should give same result as max allowed size

def test_cached_rates():
    """Test cached rate calculations."""
    calc = ImageTokenCalculator()
    image_path = next(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    
    # Regular calculation
    tokens = calc.calculate(image_path)
    regular_cost = calc.get_cost(tokens)
    
    # Cached calculation
    cached_cost = calc.get_cost(tokens, use_cached_rate=True)
    assert cached_cost < regular_cost  # Cached rate should be lower
    
    # Verify the cached rate calculation
    config = get_model_config(calc.default_model)
    expected_cached_cost = (tokens * config["cached_input_rate"] + tokens * config.get("cached_output_rate", 0)) / 1000000
    assert abs(cached_cost - expected_cached_cost) < 0.0001

def test_batch_rates():
    """Test batch rate calculations."""
    calc = ImageTokenCalculator()
    image_paths = list(SAMPLE_IMAGES_DIR.glob("*.jpg"))
    
    # Regular calculation
    tokens = calc.calculate_batch(image_paths)
    regular_costs = calc.get_cost_batch(tokens, use_batch_rate=False)
    
    # Batch calculation
    batch_costs = calc.get_cost_batch(tokens, use_batch_rate=True)
    assert all(b < r for b, r in zip(batch_costs, regular_costs))  # Batch rates should be lower
    
    # Verify the batch rate calculation
    config = get_model_config(calc.default_model)
    for t, c in zip(tokens, batch_costs):
        expected_batch_cost = (t * config["batch_input_rate"] + t * config.get("batch_output_rate", 0)) / 1000000
        assert abs(c - expected_batch_cost) < 0.0001 