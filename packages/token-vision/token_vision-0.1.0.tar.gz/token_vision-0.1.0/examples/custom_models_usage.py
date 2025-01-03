"""
Example demonstrating custom model configurations in Token Vision.
"""

from pathlib import Path
from token_vision import ImageTokenCalculator
from token_vision.models import load_custom_models, reset_models

def main():
    # Load custom models configuration
    custom_models_path = Path("examples/custom_models.json")
    load_custom_models(custom_models_path)

    # Initialize calculator
    calculator = ImageTokenCalculator()

    # Get sample image path
    sample_image = next(Path("examples/sample_images").glob("*.jpg"))

    print("\nStandard Model Example:")
    print("-" * 50)
    try:
        # Try with a standard GPT-4o model
        tokens = calculator.calculate(sample_image, model="gpt-4o")
        cost = calculator.get_cost(tokens, model="gpt-4o")
        print(f"GPT-4o:")
        print(f"  Tokens: {tokens:,}")
        print(f"  Cost: ${cost:.6f}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nCustom Models Example:")
    print("-" * 50)
    for model in ["custom-gpt-4", "custom-claude", "custom-gemini"]:
        try:
            tokens = calculator.calculate(sample_image, model=model)
            cost = calculator.get_cost(tokens, model=model)
            print(f"{model}:")
            print(f"  Tokens: {tokens:,}")
            print(f"  Cost: ${cost:.6f}")
            print("-" * 30)
        except ValueError as e:
            print(f"Error with {model}: {e}")
            print("-" * 30)

    # Reset models to default configuration
    reset_models()
    print("\nAfter Reset - Available Models:")
    print("-" * 50)
    calculator = ImageTokenCalculator()  # Reinitialize with default models
    try:
        tokens = calculator.calculate(sample_image, model="gpt-4o")
        print("Successfully reset to default models")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 