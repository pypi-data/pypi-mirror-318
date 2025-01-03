from typing import Union, Dict, Any, Tuple
from pathlib import Path
import math
import numpy as np
from PIL import Image

from .models import MODELS, get_model_info, get_provider_for_model

class ImageTokenCalculator:
    def __init__(self, default_model: str = "gemini-1-5-flash", detail_level: str = "high"):
        self.default_model = default_model
        self.detail_level = detail_level
        
    def _get_image_dimensions(self, image_path: Union[str, Path, np.ndarray]) -> Tuple[int, int]:
        """Get image dimensions from various input types."""
        if isinstance(image_path, (str, Path)):
            with Image.open(image_path) as img:
                return img.size
        elif isinstance(image_path, np.ndarray):
            return image_path.shape[1], image_path.shape[0]  # width, height
        else:
            raise ValueError("Unsupported image input type")
            
    def _calculate_claude_tokens(self, width: int, height: int) -> int:
        """Calculate tokens for Claude models."""
        if width * height <= 384 * 384:
            return 258
            
        tile_size = min(max(256, min(width, height) / 1.5), 768)
        tiles_x = math.ceil(width / tile_size)
        tiles_y = math.ceil(height / tile_size)
        return tiles_x * tiles_y * 258
        
    def _calculate_other_tokens(self, width: int, height: int) -> int:
        """Calculate tokens for OpenAI and Gemini models."""
        if self.detail_level == "low":
            return 85
            
        # Scale down if dimensions exceed 2048
        scaled_width = width
        scaled_height = height
        if width > 2048 or height > 2048:
            scale = min(2048 / width, 2048 / height)
            scaled_width = math.floor(width * scale)
            scaled_height = math.floor(height * scale)
            
        # Scale to 768px on shortest side
        shortest_side = min(scaled_width, scaled_height)
        scale = 768 / shortest_side
        scaled_width = math.floor(scaled_width * scale)
        scaled_height = math.floor(scaled_height * scale)
        
        # Calculate tiles
        tiles_x = math.ceil(scaled_width / 512)
        tiles_y = math.ceil(scaled_height / 512)
        total_tiles = tiles_x * tiles_y
        
        return total_tiles * 170 + 85
        
    def calculate(self, 
                 image_path: Union[str, Path, np.ndarray],
                 model: str = None,
                 detail_level: str = None) -> int:
        """Calculate tokens for an image."""
        model = model or self.default_model
        self.detail_level = detail_level or self.detail_level
        
        # Get image dimensions
        width, height = self._get_image_dimensions(image_path)
        
        # Get provider
        provider = get_provider_for_model(model)
        
        # Calculate tokens based on provider
        if provider == "claude":
            return self._calculate_claude_tokens(width, height)
        else:
            return self._calculate_other_tokens(width, height)
            
    def get_cost(self, tokens: int, model: str = None) -> float:
        """Calculate cost for given tokens."""
        model = model or self.default_model
        model_info = get_model_info(model)
        
        input_cost = tokens * model_info["input_rate"] / 1_000_000
        output_cost = tokens * model_info.get("output_rate", 0) / 1_000_000
        
        return input_cost + output_cost
        
    def calculate_batch(self, image_paths: list, model: str = None) -> list:
        """Calculate tokens for multiple images."""
        model = model or self.default_model
        provider = get_provider_for_model(model)
        max_images = MODELS[provider]["max_images"]
        
        if len(image_paths) > max_images:
            raise ValueError(f"Maximum {max_images} images allowed for {provider}")
            
        return [self.calculate(img, model) for img in image_paths]
        
    def get_cost_batch(self, tokens: list, model: str = None) -> float:
        """Calculate total cost for batch of images."""
        return sum(self.get_cost(t, model) for t in tokens)
