"""Configuration module."""

import json
from pathlib import Path

def load_process_patterns():
    """Load AI process patterns from JSON configuration."""
    patterns_path = Path(__file__).parent / 'ai_process_patterns.json'
    with open(patterns_path) as f:
        return json.load(f)

__all__ = ['load_process_patterns']