from typing import Dict, Any
import json
from pathlib import Path

def load_custom_models(config_path: str) -> Dict[str, Any]:
    """Load custom model configurations from a JSON file."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Model config file not found: {config_path}")
        
    with open(path) as f:
        return json.load(f)
