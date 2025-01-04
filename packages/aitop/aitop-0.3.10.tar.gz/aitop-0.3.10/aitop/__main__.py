#!/usr/bin/env python3
"""AITop - A system monitor focused on AI/ML workload monitoring."""

import curses
import sys
import threading
import time
import logging
import concurrent.futures
from dataclasses import dataclass
from queue import Queue, Empty, Full
from typing import List, Tuple, Any

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

# Set up logging with DEBUG level
logging.basicConfig(filename='aitop.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


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
        """Initialize the data collector."""
        super().__init__(daemon=True)
        self.update_interval = update_interval
        self.queue = Queue(maxsize=1)  # Only keep the latest data
        self.running = True
        self.last_update = 0

        # Initialize monitors
        self.gpu_monitors = GPUMonitorFactory.create_monitors()
        self.ai_monitor = AIProcessMonitor()
        self.memory_monitor = SystemMemoryMonitor()
        self.vendors = GPUMonitorFactory.detect_vendors()
        
        # Create a single ThreadPoolExecutor for reuse with minimal workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        logging.debug("DataCollector initialized.")

    def collect_gpu_data(self):
        """Collect GPU information and processes."""
        gpu_info = []
        gpu_processes = []
        
        # Single pass through monitors to collect both info and processes
        for monitor, vendor in zip(self.gpu_monitors, self.vendors):
            if monitor:
                gpus = monitor.get_gpu_info()
                gpu_info.extend([(gpu, vendor) for gpu in gpus])
                for gpu in gpus:
                    gpu_processes.extend(gpu.processes)
                    
        return gpu_info, gpu_processes

    def run(self) -> None:
        """Run the data collection loop."""
        logging.debug("DataCollector thread started.")
        while self.running:
            try:
                current_time = time.time()
                # Only collect if enough time has passed
                if current_time - self.last_update >= self.update_interval:
                    # Collect GPU data in single pass
                    gpu_info, gpu_processes = self.collect_gpu_data()

                    # Update all stats concurrently using the shared executor
                    futures = {
                        'processes': self.executor.submit(self.ai_monitor.get_ai_processes, gpu_processes),
                        'memory': self.executor.submit(self.memory_monitor.get_memory_stats),
                        'memory_types': self.executor.submit(self.memory_monitor.get_memory_by_type),
                        'cpu': self.executor.submit(CPUStats.get_stats)
                    }
                    
                    # Get results as they complete
                    processes = futures['processes'].result()
                    memory_stats = futures['memory'].result()
                    memory_types = futures['memory_types'].result()
                    cpu_stats = futures['cpu'].result()

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

                    # Update queue without blocking
                    try:
                        if self.queue.full():
                            self.queue.get_nowait()
                        self.queue.put_nowait(data)
                        self.last_update = current_time
                    except Full:
                        pass  # Skip update if queue is full
                
                # Much longer sleep to reduce CPU usage
                time.sleep(0.5)
            except Exception as e:
                logging.error(f"DataCollector error: {e}", exc_info=True)
                time.sleep(0.5)  # Longer sleep on error

    def stop(self) -> None:
        """Stop the data collection thread."""
        self.running = False
        logging.debug("DataCollector thread stopping.")


class AITop:
    """Main application class."""

    def __init__(self, stdscr):
        """Initialize the application."""
        self.stdscr = stdscr
        logging.debug("Initializing AITop application.")

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
        self.input_timeout = 50    # milliseconds
        self.needs_redraw = True   # Track if UI needs updating
        self.last_size = self.display.get_dimensions()

        # Initialize data collector thread with 0.5s interval
        self.collector = DataCollector(update_interval=0.5)
        self.collector.start()
        logging.debug("DataCollector thread started.")

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
                logging.debug("User requested exit.")
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
            logging.debug(f"Handled user input: {key}")
        except Exception as e:
            logging.error(f"Input handling error: {e}", exc_info=True)

    def render(self) -> None:
        """Render the complete interface."""
        try:
            # Check for terminal resize
            current_size = self.display.get_dimensions()
            if current_size != self.last_size:
                self.display.handle_resize()
                self.needs_redraw = True
                self.last_size = current_size
                logging.debug("Terminal resized.")

            # Get latest data if available
            try:
                new_data = self.collector.queue.get_nowait()
                self.system_data = new_data
                self.needs_redraw = True
                logging.debug("System data updated.")
            except Empty:
                pass  # Normal case when no new data is available
            except Exception as e:
                logging.error(f"Render data fetch error: {e}", exc_info=True)

            # Only redraw if needed and we have data
            if self.needs_redraw and self.system_data:
                try:
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
                    logging.debug("UI rendered.")
                except Exception as e:
                    logging.error(f"Render error: {e}", exc_info=True)
        except Exception as e:
            logging.error(f"Render loop error: {e}", exc_info=True)

    def cleanup(self) -> None:
        """Clean up resources."""
        logging.debug("Cleaning up application.")
        if self.collector:
            self.collector.stop()
            self.collector.executor.shutdown(wait=False)  # Shutdown executor
            self.collector.join(timeout=0.5)
            logging.debug("DataCollector thread stopped.")
        if self.display:
            self.display.cleanup()
            logging.debug("Display cleaned up.")

    def run(self) -> None:
        """Main application loop."""
        logging.debug("Application run loop started.")
        try:
            last_render = 0
            last_input = 0
            render_interval = 0.5  # 2 FPS is enough for monitoring
            input_interval = 0.5  # 2 Hz input polling is still responsive
            
            while self.running:
                current_time = time.time()
                
                # Handle input at input_interval
                if current_time - last_input >= input_interval:
                    self.handle_input()
                    last_input = current_time
                
                # Render at render_interval
                if current_time - last_render >= render_interval:
                    self.render()
                    last_render = current_time
                
                # Sleep longer to reduce CPU usage
                time.sleep(0.5)
        except Exception as e:
            logging.error(f"Run loop error: {e}", exc_info=True)
        finally:
            self.cleanup()
            logging.debug("Application terminated.")


def _main(stdscr) -> int:
    """Initialize and run the application."""
    try:
        app = AITop(stdscr)
        app.run()
        return 0
    except Exception as e:
        logging.error(f"Main error: {e}", exc_info=True)
        return 1


def main():
    """Entry point for the application."""
    try:
        return curses.wrapper(_main)
    except KeyboardInterrupt:
        logging.debug("Application interrupted by user.")
        return 0
    except Exception as e:
        logging.error(f"Unhandled exception: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
