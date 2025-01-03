#!/usr/bin/env python3
"""Base GPU monitoring functionality."""

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from pathlib import Path


@dataclass
class GPUInfo:
    """Container for GPU information."""
    index: int
    name: str
    utilization: float
    memory_used: float
    memory_total: float
    temperature: float
    power_draw: float
    power_limit: float
    processes: List[Dict[str, Any]]


class BaseGPUMonitor(ABC):
    """Abstract base class for GPU monitoring."""
    
    def __init__(self):
        """Initialize the GPU monitor with common setup."""
        self.smi_path = self._find_smi()
        
    @abstractmethod
    def _find_smi(self) -> Optional[Path]:
        """Find the vendor-specific SMI tool."""
        pass
        
    @abstractmethod
    def get_gpu_info(self) -> List[GPUInfo]:
        """Get GPU information for this vendor."""
        pass
        
    def _run_smi_command(self, cmd: List[str]) -> Optional[str]:
        """Run an SMI command and return its output."""
        try:
            import subprocess
            
            # First check if we have a valid command
            if not self.smi_path:
                return None
                
            # If it's a full path, check if it exists and is executable
            if str(self.smi_path) != self.smi_path.name:  # If path contains directory components
                if not self.smi_path.exists():
                    return None
                if not os.access(self.smi_path, os.X_OK):
                    return None
                
            # Run the command with a timeout to prevent hanging
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=5  # 5 second timeout
            )
            
            return result.stdout
            
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, 
                FileNotFoundError, PermissionError, Exception):
            return None
