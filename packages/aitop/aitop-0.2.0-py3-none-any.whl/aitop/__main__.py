#!/usr/bin/env python3
"""AITop - A system monitor focused on AI/ML workload monitoring."""

import curses
import signal
import sys
import threading
import time
from dataclasses import dataclass
from queue import Queue
from typing import Optional, List, Tuple, Any

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


@dataclass
class SystemData:
    """Container for system monitoring data."""
    gpu_info: List[Tuple[Any, str]]
    gpu_processes: List[Any]
    processes: List[Any]
    memory_stats: Any
    memory_types: Any
    cpu_stats: Any
    primary_vendor: str


class DataCollector(threading.Thread):
    """Background thread for collecting system data."""
    
    def __init__(self, update_interval: float):
        """Initialize the data collector.
        
        Args:
            update_interval: Time between updates in seconds
        """
        super().__init__(daemon=True)  # Daemon thread will exit when main thread exits
        self.update_interval = update_interval
        self.queue = Queue(maxsize=1)  # Only keep latest data
        self.running = True
        
        # Initialize monitors
        self.gpu_monitors = GPUMonitorFactory.create_monitors()
        self.ai_monitor = AIProcessMonitor()
        self.memory_monitor = SystemMemoryMonitor()
        self.vendors = GPUMonitorFactory.detect_vendors()
    
    def run(self) -> None:
        """Run the data collection loop."""
        while self.running:
            try:
                # Get GPU info
                gpu_info = []
                for monitor, vendor in zip(self.gpu_monitors, self.vendors):
                    gpus = monitor.get_gpu_info() if monitor else []
                    gpu_info.extend([(gpu, vendor) for gpu in gpus])
                
                # Extract GPU processes
                gpu_processes = []
                for monitor, _ in zip(self.gpu_monitors, self.vendors):
                    if monitor:
                        gpus = monitor.get_gpu_info()
                        for gpu in gpus:
                            gpu_processes.extend(gpu.processes)
                
                # Update all stats
                processes = self.ai_monitor.get_ai_processes(gpu_processes)
                memory_stats = self.memory_monitor.get_memory_stats()
                memory_types = self.memory_monitor.get_memory_by_type()
                cpu_stats = CPUStats.get_stats()
                primary_vendor = self.vendors[0] if self.vendors else 'none'
                
                # Package data
                data = SystemData(
                    gpu_info=gpu_info,
                    gpu_processes=gpu_processes,
                    processes=processes,
                    memory_stats=memory_stats,
                    memory_types=memory_types,
                    cpu_stats=cpu_stats,
                    primary_vendor=primary_vendor
                )
                
                # Update queue, removing old data if necessary
                if self.queue.full():
                    try:
                        self.queue.get_nowait()
                    except:
                        pass
                self.queue.put(data)
                
                time.sleep(self.update_interval)
            except Exception:
                # Log error but keep running
                time.sleep(self.update_interval)
    
    def stop(self) -> None:
        """Stop the data collection thread."""
        self.running = False


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
        
        # Application state
        self.running = True
        self.selected_tab = 0
        self.sort_by = 'cpu_percent'
        self.sort_reverse = True
        self.scroll_position = 0
        self.input_timeout = 50    # milliseconds - balanced input checking
        self.needs_redraw = True   # Track if UI needs updating
        
        # Initialize data collector thread
        self.collector = DataCollector(update_interval=1.0)
        self.collector.start()
        
        # Initialize system data
        self.system_data = None
    
    def handle_input(self) -> None:
        """Handle user input."""
        try:
            key = self.display.stdscr.getch()
            
            if key == curses.ERR:  # No input available
                return
                
            self.needs_redraw = True  # Input usually requires redraw
            
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
            elif key in [curses.KEY_UP, curses.KEY_DOWN] and self.system_data:
                if self.selected_tab == 1:  # AI Processes tab
                    self.scroll_position = self.process_panel.handle_scroll(
                        key, self.scroll_position, self.system_data.processes
                    )
        except curses.error:
            pass
    
    def render(self) -> None:
        """Render the complete interface."""
        try:
            # Check for resize first to avoid unnecessary renders
            height, width = self.display.get_dimensions()
            if (height, width) != (self.display.height, self.display.width):
                self.display.handle_resize()
                self.needs_redraw = True
            
            # Get latest data if available
            try:
                new_data = self.collector.queue.get_nowait()
                self.system_data = new_data
                self.needs_redraw = True
            except:
                pass
            
            # Only redraw if needed and we have data
            if self.needs_redraw and self.system_data:
                self.display.clear()
                
                # Render common elements
                self.header.render(self.system_data.primary_vendor)
                self.tabs.render(self.selected_tab, 1)
                
                # Render tab-specific content
                if self.selected_tab == 0:  # Overview
                    self.overview.render(
                        self.system_data.gpu_info,
                        self.system_data.processes,
                        self.system_data.memory_stats,
                        self.system_data.cpu_stats,
                        self.system_data.primary_vendor
                    )
                elif self.selected_tab == 1:  # AI Processes
                    self.process_panel.render(
                        self.system_data.processes,
                        [gpu for gpu, _ in self.system_data.gpu_info],
                        3, 2,
                        self.sort_by,
                        self.sort_reverse,
                        self.scroll_position
                    )
                elif self.selected_tab == 2:  # GPU
                    self.gpu_panel.render(self.system_data.gpu_info)
                elif self.selected_tab == 3:  # Memory
                    self.memory_panel.render(
                        self.system_data.memory_stats,
                        self.system_data.memory_types
                    )
                elif self.selected_tab == 4:  # CPU
                    self.cpu_panel.render(self.system_data.cpu_stats)
                    
                self.footer.render()
                self.display.refresh()
                self.needs_redraw = False
            
        except curses.error:
            pass
    
    def cleanup(self) -> None:
        """Clean up resources."""
        if self.collector:
            self.collector.stop()
            self.collector.join(timeout=1.0)
    
    def run(self) -> None:
        """Main application loop."""
        try:
            while self.running:
                self.handle_input()
                self.render()
        finally:
            self.cleanup()


def handle_resize(signo, frame):
    """Handle terminal resize event."""
    curses.endwin()  # End current window
    curses.initscr()  # Reinitialize screen
    
def _main(stdscr) -> int:
    """Initialize and run the application.
    
    Args:
        stdscr: Curses window object
        
    Returns:
        Exit code
    """
    # Handle terminal resize
    signal.signal(signal.SIGWINCH, handle_resize)
    
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


def main():
    """Entry point for the application."""
    try:
        return curses.wrapper(_main)
    except KeyboardInterrupt:
        return 0

if __name__ == "__main__":
    sys.exit(main())
