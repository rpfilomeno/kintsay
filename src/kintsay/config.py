import logging
import os
from typing import Dict, Any

# Default configuration
DEFAULT_CONFIG: Dict[str, Any] = {
    "namespace": "kintsay",
    "model": "gemini/gemini-1.5-flash",
    "temperature": 0.7,
    "max_steps": 5,
    "api_key": os.getenv("GEMINI_API_KEY", None),
    "broker": "redis://redis:6379",
    "backend": "redis://redis:6379",
}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kinsay")
