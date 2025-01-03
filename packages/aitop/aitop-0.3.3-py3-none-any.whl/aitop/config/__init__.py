"""Configuration module."""

import json
from pathlib import Path
from typing import Dict, Optional, List

def load_process_patterns(patterns_file: Optional[Path] = None) -> List[str]:
    """Load AI process patterns from JSON configuration.
    
    Args:
        patterns_file: Optional custom patterns file path
        
    Returns:
        List of regex patterns for AI process detection
        
    Raises:
        RuntimeError: If patterns file cannot be loaded
    """
    if patterns_file is None:
        patterns_file = Path(__file__).parent / 'ai_process_patterns.json'
        
    try:
        with open(patterns_file) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load process patterns from {patterns_file}: {str(e)}")

def load_themes(theme_file: Optional[Path] = None) -> Dict:
    """Load theme configurations from JSON file.
    
    Args:
        theme_file: Optional custom theme file path
        
    Returns:
        Dictionary containing theme configurations
    """
    if theme_file is None:
        theme_file = Path(__file__).parent / 'themes.json'
        
    try:
        with open(theme_file) as f:
            return json.load(f)['themes']
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        raise RuntimeError(f"Failed to load themes from {theme_file}: {str(e)}")

__all__ = ['load_process_patterns', 'load_themes']
