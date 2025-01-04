#!/usr/bin/env python3
"""Process monitoring for AI/ML workloads."""

import os
import re
import psutil
from pathlib import Path
from typing import Dict, List, Any, Optional

from ...config import load_process_patterns


class AIProcessMonitor:
    """Monitors processes related to AI/ML workloads."""
    
    def __init__(self, patterns_file: Optional[Path] = None):
        """Initialize the AI process monitor.
        
        Args:
            patterns_file: Path to JSON file containing process patterns.
                         If None, uses default patterns file in config directory.
        """
        try:
            patterns = load_process_patterns(patterns_file)
            self.patterns = [re.compile(pattern, re.IGNORECASE) 
                           for pattern in patterns]
        except RuntimeError:
            # Use default patterns if file loading fails
            self.patterns = [
                re.compile(p, re.IGNORECASE) for p in [
                    "python.*",
                    ".*tensorflow.*",
                    ".*torch.*",
                    ".*cuda.*",
                    ".*nvidia.*"
                ]
            ]

    def is_ai_process(self, proc_name: str, cmdline: str = "") -> bool:
        """Check if a process name or command line matches AI/ML patterns.
        
        Args:
            proc_name: Name of the process
            cmdline: Full command line of the process (optional)
            
        Returns:
            bool: True if the process matches any AI/ML patterns
        """
        return any(pattern.search(proc_name) for pattern in self.patterns) or \
               (cmdline and any(pattern.search(cmdline) for pattern in self.patterns))

    def _get_process_cmdline(self, proc: psutil.Process) -> str:
        """Safely get process command line."""
        try:
            cmdline = proc.cmdline()
            # Get the script name if it's a Python process
            if proc.name().startswith('python'):
                # Find the .py file in the command line
                script_name = next((arg for arg in cmdline if arg.endswith('.py')), '')
                if script_name:
                    # Extract just the filename without path
                    return f"python:{os.path.basename(script_name)}"
            return ' '.join(cmdline)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return proc.name()

    def _get_process_info(self, proc: psutil.Process) -> Dict[str, Any]:
        """Get detailed information about a process."""
        try:
            with proc.oneshot():
                cpu_times = proc.cpu_times()
                memory_info = proc.memory_info()
                
                return {
                    'pid': proc.pid,
                    'name': proc.name(),
                    'cmdline': self._get_process_cmdline(proc),
                    'cpu_percent': proc.cpu_percent(),
                    'memory_percent': proc.memory_percent(),
                    'status': proc.status(),
                    'cpu_time_user': cpu_times.user,
                    'cpu_time_system': cpu_times.system,
                    'memory_rss': memory_info.rss,
                    'memory_vms': memory_info.vms,
                    'cpu_affinity': proc.cpu_affinity(),
                    'num_threads': proc.num_threads(),
                    'create_time': proc.create_time()
                }
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return {}

    def get_ai_processes(self, gpu_processes: Optional[List[Dict[str, Any]]] = None) -> List[Dict[str, Any]]:
        """Get information about AI-related processes.
        
        Args:
            gpu_processes: Optional list of GPU processes from nvidia-smi
        """
        ai_processes = []
        gpu_pids = set()
        
        # First collect GPU process PIDs
        if gpu_processes:
            for proc in gpu_processes:
                gpu_pids.add(proc['pid'])
        
        # Then check all processes
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Consider it an AI process if it's either:
                # 1. Using the GPU (in gpu_pids set)
                # 2. Matches AI patterns in name/cmdline
                cmdline = self._get_process_cmdline(proc)
                if proc.info['pid'] in gpu_pids or self.is_ai_process(proc.info['name'], cmdline):
                    proc_info = self._get_process_info(proc)
                    if proc_info:
                        # Truncate command line if too long
                        if 'cmdline' in proc_info:
                            proc_info['cmdline'] = (proc_info['cmdline'][:50] + '...' 
                                                  if len(proc_info['cmdline']) > 50 
                                                  else proc_info['cmdline'])
                        ai_processes.append(proc_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
                
        return ai_processes

    def get_process_gpu_usage(self, pid: int, gpu_processes: List[Dict[str, Any]]) -> Dict[str, float]:
        """Get GPU usage information for a specific process.
        
        Args:
            pid: Process ID to look up
            gpu_processes: List of GPU processes from GPUInfo
            
        Returns:
            Dictionary containing:
                - gpu_util: Estimated GPU utilization percentage
                - vram_percent: VRAM usage percentage
        """
        for proc in gpu_processes:
            if proc['pid'] == pid:
                return {
                    'gpu_util': proc.get('gpu_util', 0.0),
                    'vram_percent': proc.get('vram_percent', 0.0)
                }
        return {
            'gpu_util': 0.0,
            'vram_percent': 0.0
        }
