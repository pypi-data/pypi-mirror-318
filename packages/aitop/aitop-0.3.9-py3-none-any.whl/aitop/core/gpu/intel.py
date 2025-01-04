#!/usr/bin/env python3
"""Intel-specific GPU monitoring implementation."""

import re
import subprocess
from pathlib import Path
from typing import List, Optional, Dict, Any

from .base import BaseGPUMonitor, GPUInfo


class IntelGPUMonitor(BaseGPUMonitor):
    """Intel GPU monitoring implementation."""
    
    def _find_smi(self) -> Optional[Path]:
        """Find Intel GPU monitoring tool."""
        common_paths = [
            '/usr/bin/intel_gpu_top',
            '/usr/local/bin/intel_gpu_top'
        ]
        for path in common_paths:
            if Path(path).exists():
                return Path(path)
        return None

    def _parse_gpu_info(self, output: str) -> List[Dict[str, Any]]:
        """Parse intel_gpu_top output for all GPUs."""
        if not output:
            return []

        gpus = []
        current_gpu = {}
        
        # Parse output for each GPU
        gpu_sections = output.split('Intel GPU device')
        for section in gpu_sections[1:]:  # Skip first empty split
            try:
                # Extract device info
                device_match = re.search(r'(\d+):\s*([^\n]+)', section)
                if device_match:
                    index = int(device_match.group(1))
                    name = device_match.group(2).strip()
                    
                    # Extract utilization
                    util_match = re.search(r'Render/3D/0\s+([0-9.]+)%', section)
                    utilization = float(util_match.group(1)) if util_match else 0.0
                    
                    # Extract memory info (if available)
                    mem_match = re.search(r'Memory: (\d+)MB used / (\d+)MB total', section)
                    if mem_match:
                        memory_used = float(mem_match.group(1))
                        memory_total = float(mem_match.group(2))
                    else:
                        memory_used = 0.0
                        memory_total = 0.0
                    
                    # Extract temperature (if available)
                    temp_match = re.search(r'GPU temperature: (\d+)°C', section)
                    temperature = float(temp_match.group(1)) if temp_match else 0.0
                    
                    # Extract power (if available)
                    power_match = re.search(r'Power: (\d+\.\d+)W', section)
                    power = float(power_match.group(1)) if power_match else 0.0
                    
                    # Extract processes
                    processes = []
                    proc_section = re.search(r'Processes:\n(.*?)(?=\n\n|\Z)', section, re.DOTALL)
                    if proc_section:
                        proc_lines = proc_section.group(1).strip().split('\n')
                        for line in proc_lines:
                            if line.strip():
                                parts = line.split()
                                if len(parts) >= 2:
                                    try:
                                        pid = int(parts[0])
                                        processes.append({
                                            'pid': pid,
                                            'name': ' '.join(parts[1:]),
                                            'memory': 0.0  # Memory per process not available
                                        })
                                    except (ValueError, IndexError):
                                        continue
                    
                    gpus.append({
                        'index': index,
                        'name': name,
                        'utilization': utilization,
                        'memory_used': memory_used,
                        'memory_total': memory_total,
                        'temperature': temperature,
                        'power_draw': power,
                        'processes': processes
                    })
                    
            except (ValueError, AttributeError, IndexError):
                continue
                
        return gpus

    def get_gpu_info(self) -> List[GPUInfo]:
        """Get Intel GPU information for all devices."""
        if not self.smi_path:
            return []

        try:
            # Get initial device list
            cmd = [str(self.smi_path), '-L']
            result = self._run_smi_command(cmd)
            if not result:
                return []
                
            # Get detailed info
            cmd = [str(self.smi_path), '-J']  # JSON output if supported
            result = self._run_smi_command(cmd)
            if not result:
                return []
                
            gpu_info = self._parse_gpu_info(result)
            
            return [GPUInfo(
                index=info['index'],
                name=info['name'],
                utilization=info['utilization'],
                memory_used=info['memory_used'],
                memory_total=info['memory_total'],
                temperature=info['temperature'],
                power_draw=info['power_draw'],
                power_limit=0.0,  # Power limit not available
                processes=info['processes']
            ) for info in gpu_info]
            
        except Exception:
            return []

    def _run_smi_command(self, cmd: List[str]) -> Optional[str]:
        """Run an Intel GPU monitoring command."""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=5
            )
            return result.stdout
        except (subprocess.SubprocessError, FileNotFoundError, subprocess.TimeoutExpired):
            return None
