#!/usr/bin/env python3
"""AITop - A system monitor focused on AI/ML workload monitoring."""

import curses
import signal
import sys
from typing import Optional

from aitop.core.gpu.factory import GPUMonitorFactory
from aitop.core.process.monitor import AIProcessMonitor
from aitop.core.system.memory import SystemMemoryMonitor
from aitop.core.system.cpu import CPUStats
from aitop.ui.display import Display
from aitop.ui.components.header import HeaderComponent
from aitop.ui.components.footer import FooterComponent
from aitop.ui.components.tabs import TabsComponent
from aitop.ui.components.overview import OverviewPanel
from aitop.ui.components.gpu_panel import GPUPanel
from aitop.ui.components.process_panel import ProcessPanel
from aitop.ui.components.memory_panel import MemoryPanel
from aitop.ui.components.cpu_panel import CPUPanel


class AITop:
    """Main application class."""
    
    def __init__(self, stdscr):
        """Initialize the application.
        
        Args:
            stdscr: Curses window object
        """
        # Initialize display and UI components
        self.display = Display(stdscr)
        self.header = HeaderComponent(self.display)
        self.footer = FooterComponent(self.display)
        self.tabs = TabsComponent(self.display)
        self.overview = OverviewPanel(self.display)
        self.gpu_panel = GPUPanel(self.display)
        self.process_panel = ProcessPanel(self.display)
        self.memory_panel = MemoryPanel(self.display)
        self.cpu_panel = CPUPanel(self.display)
        
        # Initialize monitors
        self.gpu_monitors = GPUMonitorFactory.create_monitors()
        self.ai_monitor = AIProcessMonitor()
        self.memory_monitor = SystemMemoryMonitor()
        
        # Application state
        self.running = True
        self.selected_tab = 0
        self.sort_by = 'cpu_percent'
        self.sort_reverse = True
        self.scroll_position = 0
        self.update_interval = 1.0  # seconds
        
        # Get GPU vendors
        self.vendors = GPUMonitorFactory.detect_vendors()
    
    def handle_input(self) -> None:
        """Handle user input."""
        try:
            self.display.stdscr.timeout(int(self.update_interval * 1000))
            key = self.display.stdscr.getch()
            
            if key == ord('q'):
                self.running = False
            elif key == ord('c'):
                self.sort_by = 'cpu_percent'
                self.sort_reverse = True
            elif key == ord('m'):
                self.sort_by = 'memory_percent'
                self.sort_reverse = True
            elif key == ord('h'):
                self.sort_reverse = not self.sort_reverse
            elif key in [curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.selected_tab = self.tabs.handle_tab_input(key, self.selected_tab)
                self.scroll_position = 0
            elif key in [curses.KEY_UP, curses.KEY_DOWN]:
                if self.selected_tab == 1:  # AI Processes tab (new position)
                    # Extract GPU processes from all GPUs
                    gpu_processes = []
                    for monitor, _ in zip(self.gpu_monitors, self.vendors):
                        if monitor:
                            gpus = monitor.get_gpu_info()
                            for gpu in gpus:
                                gpu_processes.extend(gpu.processes)
                    
                    processes = self.ai_monitor.get_ai_processes(gpu_processes)
                    self.scroll_position = self.process_panel.handle_scroll(
                        key, self.scroll_position, processes
                    )
        except curses.error:
            pass
    
    def render(self) -> None:
        """Render the complete interface."""
        try:
            self.display.clear()
            
            # Get current data
            gpu_info = []
            for monitor, vendor in zip(self.gpu_monitors, self.vendors):
                gpus = monitor.get_gpu_info() if monitor else []
                gpu_info.extend([(gpu, vendor) for gpu in gpus])
            
            # Extract GPU processes from all GPUs
            gpu_processes = []
            for monitor, _ in zip(self.gpu_monitors, self.vendors):
                if monitor:
                    gpus = monitor.get_gpu_info()
                    for gpu in gpus:
                        gpu_processes.extend(gpu.processes)
            
            processes = self.ai_monitor.get_ai_processes(gpu_processes)
            memory_stats = self.memory_monitor.get_memory_stats()
            memory_types = self.memory_monitor.get_memory_by_type()
            cpu_stats = CPUStats.get_stats()
            
            # Get primary vendor for header (first detected GPU)
            primary_vendor = self.vendors[0] if self.vendors else 'none'
            
            # Render common elements
            self.header.render(primary_vendor)
            self.tabs.render(self.selected_tab, 1)
            
            # Render tab-specific content
            if self.selected_tab == 0:  # Overview
                self.overview.render(gpu_info, processes, memory_stats, 
                                  cpu_stats, primary_vendor)
            elif self.selected_tab == 1:  # AI Processes
                self.process_panel.render(processes, [gpu for gpu, _ in gpu_info], 3, 2,
                                       self.sort_by, self.sort_reverse,
                                       self.scroll_position)
            elif self.selected_tab == 2:  # GPU
                self.gpu_panel.render(gpu_info)
            elif self.selected_tab == 3:  # Memory
                self.memory_panel.render(memory_stats, memory_types)
            elif self.selected_tab == 4:  # CPU
                self.cpu_panel.render(cpu_stats)
                
            self.footer.render()
            self.display.refresh()
            
        except curses.error:
            pass
    
    def run(self) -> None:
        """Main application loop."""
        while self.running:
            self.handle_input()
            self.render()


def main(stdscr) -> int:
    """Initialize and run the application.
    
    Args:
        stdscr: Curses window object
        
    Returns:
        Exit code
    """
    # Handle terminal resize
    signal.signal(signal.SIGWINCH, lambda signo, frame: 
                 curses.resizeterm(*stdscr.getmaxyx()))
    
    try:
        app = AITop(stdscr)
        app.run()
    except Exception as e:
        # Restore terminal
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1
        
    return 0


if __name__ == "__main__":
    try:
        sys.exit(curses.wrapper(main))
    except KeyboardInterrupt:
        sys.exit(0)
