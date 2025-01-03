"""
Core implementation of Token Vision.
This module contains the main calculator class that handles token calculations for different models.
"""

from pathlib import Path
from typing import Union, List, Dict, Optional, Any, Tuple

import numpy as np
from PIL import Image

from .models import (
    MODELS,
    ModelProvider,
    DetailLevel,
    get_model_provider,
    get_model_config
)

class ImageTokenCalculator:
    """Calculator for determining token usage and costs for images with various AI models."""
    
    def __init__(
        self,
        default_model: str = "gpt-4o",
        detail_level: DetailLevel = "high"
    ) -> None:
        """Initialize the calculator.
        
        Args:
            default_model: The default model to use for calculations
            detail_level: The detail level for models that support it (e.g., OpenAI models)
        
        Raises:
            ValueError: If the default_model is not supported
        """
        self.default_model = default_model
        self.detail_level = detail_level
        # Validate default model
        get_model_config(default_model)

    def _load_image(
        self,
        image: Union[str, Path, np.ndarray, Image.Image]
    ) -> Tuple[int, int]:
        """Load an image and return its dimensions.
        
        Args:
            image: The image to load, can be a file path, numpy array, or PIL Image
        
        Returns:
            A tuple of (width, height) in pixels
        
        Raises:
            ValueError: If the image format is not supported or file not found
        """
        if isinstance(image, (str, Path)):
            try:
                with Image.open(image) as img:
                    return img.size
            except Exception as e:
                raise ValueError(f"Failed to load image: {e}")
        
        elif isinstance(image, np.ndarray):
            if len(image.shape) < 2 or len(image.shape) > 3:
                raise ValueError("Invalid image array: must be 2D or 3D array")
            height, width = image.shape[:2]
            return width, height
        
        elif isinstance(image, Image.Image):
            return image.size
        
        raise ValueError("Unsupported image format")

    def _calculate_tokens(
        self,
        width: int,
        height: int,
        detail: DetailLevel = "high"
    ) -> int:
        """Calculate tokens for all models.
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
            detail: Detail level ('high' or 'low')
        
        Returns:
            Number of tokens required
        """
        if detail == "low":
            return 85
        
        # Scale image if needed
        if width > 2048 or height > 2048:
            scale = min(2048 / width, 2048 / height)
            width = int(width * scale)
            height = int(height * scale)
        
        shortest_side = min(width, height)
        scale = 768 / shortest_side
        width = int(width * scale)
        height = int(height * scale)
        
        tiles_x = np.ceil(width / 512)
        tiles_y = np.ceil(height / 512)
        total_tiles = tiles_x * tiles_y
        
        return int(total_tiles * 170 + 85)

    def calculate(
        self,
        image: Union[str, Path, np.ndarray, Image.Image],
        model: Optional[str] = None,
        detail_level: Optional[DetailLevel] = None
    ) -> int:
        """Calculate the number of tokens required for an image.
        
        Args:
            image: The image to analyze
            model: The model to use (defaults to the instance's default_model)
            detail_level: Override the default detail level
        
        Returns:
            Number of tokens required for the image
        
        Raises:
            ValueError: If the model is not supported or image cannot be processed
        """
        model = model or self.default_model
        detail = detail_level or self.detail_level
        provider = get_model_provider(model)
        
        # Get image dimensions
        width, height = self._load_image(image)
        
        # Calculate tokens
        return self._calculate_tokens(width, height, detail)

    def calculate_batch(
        self,
        images: List[Union[str, Path, np.ndarray, Image.Image]],
        model: Optional[str] = None,
        detail_level: Optional[DetailLevel] = None
    ) -> List[int]:
        """Calculate tokens for multiple images.
        
        Args:
            images: List of images to analyze
            model: The model to use (defaults to the instance's default_model)
            detail_level: Override the default detail level
        
        Returns:
            List of token counts for each image
        """
        return [self.calculate(img, model, detail_level) for img in images]

    def get_cost(
        self,
        tokens: int,
        model: Optional[str] = None,
        use_batch_rate: bool = False,
        use_cached_rate: bool = False
    ) -> float:
        """Calculate the cost for a given number of tokens.
        
        Args:
            tokens: Number of tokens
            model: The model to use for cost calculation
            use_batch_rate: Whether to use batch processing rates if available
            use_cached_rate: Whether to use cached input rates if available
        
        Returns:
            Total cost in USD
        """
        model = model or self.default_model
        config = get_model_config(model)
        
        # Determine input rate
        input_rate = config["input_rate"]
        if use_cached_rate and "cached_input_rate" in config:
            input_rate = config["cached_input_rate"]
        elif use_batch_rate and "batch_input_rate" in config:
            input_rate = config["batch_input_rate"]
        
        # Determine output rate
        output_rate = config.get("output_rate", 0)
        if use_batch_rate and "batch_output_rate" in config:
            output_rate = config["batch_output_rate"]
        
        input_cost = tokens * input_rate / 1000000
        output_cost = tokens * output_rate / 1000000
        
        return input_cost + output_cost 