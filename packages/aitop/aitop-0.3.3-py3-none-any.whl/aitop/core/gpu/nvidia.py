#!/usr/bin/env python3
"""NVIDIA-specific GPU monitoring implementation."""

import os
import subprocess
from pathlib import Path
from typing import List, Optional

from .base import BaseGPUMonitor, GPUInfo


class NvidiaGPUMonitor(BaseGPUMonitor):
    """NVIDIA GPU monitoring implementation."""
    
    def _find_smi(self) -> Optional[Path]:
        """Find nvidia-smi executable."""
        try:
            # Try running nvidia-smi directly first
            subprocess.run(['nvidia-smi', '--version'],
                         capture_output=True, text=True, check=True)
            # Use the known working path
            return Path('/usr/bin/nvidia-smi')
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to common locations
            common_paths = [
                '/usr/bin/nvidia-smi',
                '/usr/local/bin/nvidia-smi'
            ]
            
            for path in common_paths:
                p = Path(path)
                if p.exists():
                    try:
                        subprocess.run([str(p), '--version'],
                                    capture_output=True, text=True, check=True)
                        return p
                    except (subprocess.CalledProcessError, Exception):
                        continue
                        
        return None

    def get_gpu_info(self) -> List[GPUInfo]:
        """Get NVIDIA GPU information using nvidia-smi."""
        if not self.smi_path:
            return []

        try:
            # Get GPU information
            cmd = [
                str(self.smi_path),
                '--query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw,power.limit,compute_mode',
                '--format=csv,noheader,nounits'
            ]
            result = self._run_smi_command(cmd)
            if not result:
                return []
            
            # Get process information
            cmd_proc = [
                str(self.smi_path),
                '--query-compute-apps=gpu_uuid,pid,used_memory,process_name',
                '--format=csv,nounits,noheader'
            ]
            try:
                proc_result = self._run_smi_command(cmd_proc)
                if not proc_result or not proc_result.strip():
                    proc_result = ""
            except Exception:
                proc_result = ""
            
            gpus = []
            for line in result.strip().split('\n'):
                if not line.strip():
                    continue
                    
                values = line.split(', ')
                if len(values) >= 8:
                    index = int(values[0])
                    
                    # Parse processes
                    processes = []
                    for proc_line in proc_result.strip().split('\n'):
                        if proc_line.strip():
                            try:
                                proc_values = proc_line.split(', ')
                                if len(proc_values) >= 4:
                                    processes.append({
                                        'pid': int(proc_values[1]),
                                        'memory': float(proc_values[2]),
                                        'name': proc_values[3].strip()
                                    })
                            except (ValueError, IndexError):
                                continue
                    
                    try:
                        power_draw = float(values[6]) if values[6] != '[N/A]' else 0
                        power_limit = float(values[7]) if values[7] != '[N/A]' else 0
                        
                        gpu_info = GPUInfo(
                            index=index,
                            name=values[1].strip(),
                            utilization=float(values[2]),
                            memory_used=float(values[3]),
                            memory_total=float(values[4]),
                            temperature=float(values[5]),
                            power_draw=power_draw,
                            power_limit=power_limit,
                            processes=processes
                        )
                        gpus.append(gpu_info)
                    except ValueError:
                        continue
            
            return gpus
        except (ValueError, IndexError):
            return []
