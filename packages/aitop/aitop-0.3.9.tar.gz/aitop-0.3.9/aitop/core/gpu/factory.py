#!/usr/bin/env python3
"""GPU Monitor factory and vendor detection."""

import os
import subprocess
from typing import List, Optional
from pathlib import Path

from .nvidia import NvidiaGPUMonitor
from .amd import AMDGPUMonitor
from .intel import IntelGPUMonitor
from .base import BaseGPUMonitor


class GPUMonitorFactory:
    """Factory class for creating appropriate GPU monitor instances."""
    
    @staticmethod
    def detect_vendors() -> list[str]:
        """Detect all available GPU vendors."""
        vendors = []
        
        # Add common GPU tool locations to PATH
        os.environ['PATH'] = os.environ['PATH'] + ':/opt/rocm/bin:/usr/local/bin:/usr/bin'
        
        # Check NVIDIA first since it's specified in the task
        # First try running nvidia-smi directly to see if it's in PATH
        try:
            result = subprocess.run(['nvidia-smi', '--version'], 
                                 capture_output=True, text=True, check=True)
            nvidia_smi_paths = [Path('/usr/bin/nvidia-smi')]  # Use full path
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to common locations
            nvidia_smi_paths = [
                Path('/usr/bin/nvidia-smi'),
                Path('/usr/local/bin/nvidia-smi')
            ]
        
        nvidia_found = False
        for nvidia_smi in nvidia_smi_paths:
            if nvidia_smi.exists():
                try:
                    # First try basic nvidia-smi
                    subprocess.run([str(nvidia_smi)],
                                 capture_output=True, text=True, check=True)
                    
                    # Then try nvidia-smi -L
                    subprocess.run([str(nvidia_smi), '-L'],
                                 capture_output=True, text=True, check=True)
                    
                    # If we can run nvidia-smi successfully, we have a GPU
                    vendors.append('nvidia')
                    nvidia_found = True
                    break
                except (subprocess.CalledProcessError, Exception):
                    continue

        # Then check AMD
        try:
            result = subprocess.run(['rocm-smi', '-i'], 
                                  capture_output=True, text=True)
            if 'GPU ID' in result.stdout or 'GPU[' in result.stdout:
                vendors.append('amd')
        except Exception:
            pass
            
        # Finally check Intel
        try:
            subprocess.run(['intel_gpu_top'], capture_output=True, check=True)
            vendors.append('intel')
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
            
        return vendors if vendors else ['none']

    @classmethod
    def create_monitors(cls) -> List[BaseGPUMonitor]:
        """Create appropriate GPU monitors for all detected vendors."""
        monitors = []
        vendors = cls.detect_vendors()
        
        for vendor in vendors:
            if vendor == 'nvidia':
                monitors.append(NvidiaGPUMonitor())
            elif vendor == 'amd':
                monitors.append(AMDGPUMonitor())
            elif vendor == 'intel':
                monitors.append(IntelGPUMonitor())
        return monitors
