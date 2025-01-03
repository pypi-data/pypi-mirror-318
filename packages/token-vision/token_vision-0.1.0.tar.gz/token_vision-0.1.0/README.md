# Token Vision

A fast, offline token calculator for images with various AI models (Claude, GPT-4o, Gemini). Calculate image tokens and costs without making API calls or hitting rate limits.

## Advantages

- **Offline Operation**: Calculate tokens without internet connectivity or API keys
- **No Rate Limits**: Process unlimited images without worrying about API quotas
- **Ultra Fast**: Get instant results without network latency
- **Cost Efficient**: Plan and estimate costs without spending API credits
- **Multi-Model Support**: One library for all major vision models
- **Accurate**: Uses the same tiling and scaling algorithms as the official implementations
- **Developer Friendly**: Clean API with type hints and comprehensive documentation
- **Extensible**: Support for custom models and pricing configurations

## Installation

```bash
pip install token-vision
```

## Quick Start

```python
from token_vision import ImageTokenCalculator

# Initialize calculator
calculator = ImageTokenCalculator()

# Calculate tokens for an image
tokens = calculator.calculate(
    image_path="path/to/image.jpg",
    model="gpt-4o"
)

# Get cost
cost = calculator.get_cost(tokens)
print(f"Tokens: {tokens:,}")
print(f"Cost: ${cost:.6f}")
```

## Features

- Support for multiple AI models:
  - Claude (Sonnet, Haiku, Opus)
  - GPT-4o (Latest, Nov 2024, Aug 2024, May 2024)
  - Gemini (Pro, Flash)
- Accurate token calculation based on image dimensions
- Cost estimation for both input and output tokens
- Support for various image input formats
- Batch processing capabilities
- Memory efficient processing
- Custom model configuration support

## Documentation

### Supported Models

The library supports the following models with their respective token calculation methods:

#### Claude Models
- claude-3-sonnet
- claude-3-haiku
- claude-3-opus

#### OpenAI Models
- gpt-4o
- gpt-4o-2024-11-20
- gpt-4o-2024-08-06
- gpt-4o-2024-05-13

#### Google Models
- gemini-1.5-pro
- gemini-1.5-flash

### Custom Models

You can add your own models or override existing ones using a JSON configuration file:

```python
from token_vision import ImageTokenCalculator
from token_vision.models import load_custom_models

# Load custom models
load_custom_models("path/to/custom_models.json")

# Use custom model
calculator = ImageTokenCalculator()
tokens = calculator.calculate("image.jpg", model="custom-model-v1")
```

Example custom_models.json:
```json
{
    "custom-provider": {
        "name": "Custom Provider",
        "max_images": 10,
        "models": {
            "custom-model-v1": {
                "name": "Custom Model V1",
                "input_rate": 0.001,
                "output_rate": 0.005,
                "batch_input_rate": 0.0005,
                "batch_output_rate": 0.0025
            }
        }
    }
}
```

### Advanced Usage

```python
# Custom configuration
calculator = ImageTokenCalculator(
    default_model="gpt-4o",
    detail_level="high"
)

# Process multiple images
results = calculator.calculate_batch([
    "image1.jpg",
    "image2.jpg"
])

# Using numpy arrays
import numpy as np
image_array = np.array(...)  # Your image data
result = calculator.calculate(
    image=image_array,
    model="gpt-4o",
    detail_level="low"
)
```

## Development

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nerveband/token-vision.git
cd token-vision
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 