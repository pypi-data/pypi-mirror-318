#!/usr/bin/env python3
"""NVIDIA-specific GPU monitoring implementation."""

import os
import subprocess
import logging
from pathlib import Path
from typing import List, Optional

from .base import BaseGPUMonitor, GPUInfo


class NvidiaGPUMonitor(BaseGPUMonitor):
    """NVIDIA GPU monitoring implementation."""
    
    def _find_smi(self) -> Optional[Path]:
        """Find nvidia-smi executable."""
        try:
            # Try running nvidia-smi directly first
            result = subprocess.run(['nvidia-smi', '--version'],
                         capture_output=True, text=True, check=True)
            self.logger.debug("nvidia-smi version check succeeded: " + result.stdout.strip())
            # Use the known working path
            return Path('/usr/bin/nvidia-smi')
            
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            # Fallback to common locations
            self.logger.debug("Direct nvidia-smi check failed: " + str(e))
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
                        self.logger.debug("Found working nvidia-smi at " + str(p))
                        return p
                    except (subprocess.CalledProcessError, Exception) as e:
                        self.logger.debug("nvidia-smi at " + str(p) + " failed: " + str(e))
                        continue
                        
        self.logger.warning("No working nvidia-smi found in common locations")
        return None

    def get_gpu_info(self) -> List[GPUInfo]:
        """Get NVIDIA GPU information using nvidia-smi."""
        self.logger.debug("Starting GPU info collection")
        if not self.smi_path:
            self.logger.warning("Cannot get GPU info - no nvidia-smi available")
            return []

        try:
            # Get GPU information
            cmd = [
                str(self.smi_path),
                '--query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw,power.limit,compute_mode',
                '--format=csv,noheader,nounits'
            ]
            self.logger.debug("Executing nvidia-smi command: " + " ".join(cmd))
            result = self._run_smi_command(cmd)
            if not result:
                self.logger.error("Failed to get GPU information from nvidia-smi")
                return []
            
            self.logger.debug("Successfully retrieved GPU information")
            
            # Get process information
            cmd_proc = [
                str(self.smi_path),
                '--query-compute-apps=gpu_uuid,pid,used_memory,process_name',
                '--format=csv,nounits,noheader'
            ]
            self.logger.debug("Executing nvidia-smi process query: " + " ".join(cmd_proc))
            try:
                proc_result = self._run_smi_command(cmd_proc)
                if not proc_result or not proc_result.strip():
                    self.logger.debug("No GPU processes currently running")
                    proc_result = ""
                else:
                    self.logger.debug("Found " + str(len(proc_result.strip().split('\n'))) + " GPU processes")
            except Exception as e:
                self.logger.error("Failed to get process information: " + str(e))
                proc_result = ""
            
            gpus = []
            self.logger.debug("Parsing GPU information")
            gpu_lines = result.strip().split('\n')
            self.logger.debug("Found " + str(len(gpu_lines)) + " GPUs to parse")
            
            for line in gpu_lines:
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
                        
                        self.logger.debug("Parsed values for GPU " + values[0] + ": " +
                                        "util=" + values[2] + "%, " +
                                        "mem=" + values[3] + "/" + values[4] + "MB, " +
                                        "temp=" + values[5] + "°C, " +
                                        "power=" + str(power_draw) + "/" + str(power_limit) + "W")
                        
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
                    except ValueError as e:
                        self.logger.error("Failed to parse GPU values: " + str(e))
                        continue
            
            self.logger.debug("Successfully parsed information for " + str(len(gpus)) + " GPUs")
            return gpus
        except (ValueError, IndexError) as e:
            self.logger.error("Failed to get GPU information: " + str(e))
            return []
