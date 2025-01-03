#!/usr/bin/env python3
"""Base display handling functionality."""

import curses
from typing import Tuple, Optional, Dict, Any


class Display:
    """Handles the terminal UI display."""
    
    def __init__(self, stdscr):
        """Initialize the display.
        
        Args:
            stdscr: curses window object
        """
        self.stdscr = stdscr
        self.setup_colors()
        self.height, self.width = stdscr.getmaxyx()
        
        try:
            curses.curs_set(0)  # Hide cursor
            self.stdscr.keypad(1)  # Enable keypad
        except Exception:
            pass
    
    def setup_colors(self) -> None:
        """Initialize color pairs safely."""
        try:
            curses.start_color()
            curses.use_default_colors()
            
            # Define color pairs
            pairs = [
                (1, curses.COLOR_GREEN, -1),     # Normal
                (2, curses.COLOR_BLACK, curses.COLOR_GREEN),  # Selected
                (3, curses.COLOR_YELLOW, -1),    # Warning
                (4, curses.COLOR_RED, -1),       # Critical
                (5, curses.COLOR_CYAN, -1),      # Info
                (6, curses.COLOR_MAGENTA, -1),   # AI Process
                (7, curses.COLOR_BLUE, -1),      # Header
                (8, curses.COLOR_WHITE, -1),     # Footer
            ]
            
            for pair_id, fg, bg in pairs:
                curses.init_pair(pair_id, fg, bg)
        except Exception:
            pass
    
    def get_dimensions(self) -> Tuple[int, int]:
        """Get current terminal dimensions."""
        self.height, self.width = self.stdscr.getmaxyx()
        return self.height, self.width
    
    def safe_addstr(self, y: int, x: int, text: str, attr: Optional[int] = None) -> None:
        """Safely add a string to the screen.
        
        Args:
            y: Y coordinate
            x: X coordinate
            text: Text to display
            attr: Curses attribute (color pair, etc.)
        """
        try:
            if y >= self.height or x >= self.width:
                return
                
            max_length = self.width - x
            if len(text) > max_length:
                text = text[:max_length]
                
            if attr is not None:
                self.stdscr.addstr(y, x, text, attr)
            else:
                self.stdscr.addstr(y, x, text)
        except curses.error:
            pass
    
    def get_color(self, value: float) -> int:
        """Get appropriate color based on value percentage.
        
        Args:
            value: Percentage value (0-100)
            
        Returns:
            Curses color pair
        """
        try:
            if value >= 80:
                return curses.color_pair(4)  # Red
            elif value >= 60:
                return curses.color_pair(3)  # Yellow
            return curses.color_pair(1)      # Green
        except Exception:
            return curses.A_NORMAL
    
    def create_bar(self, value: float, width: int) -> Tuple[str, int]:
        """Create a progress bar.
        
        Args:
            value: Percentage value (0-100)
            width: Width of the bar in characters
            
        Returns:
            Tuple of (bar_string, color_attr)
        """
        filled_width = int(value * width / 100)
        bar = '█' * filled_width + '░' * (width - filled_width)
        color = self.get_color(value)
        
        return bar, color
    
    def clear(self) -> None:
        """Clear the screen."""
        self.stdscr.clear()
    
    def refresh(self) -> None:
        """Refresh the screen."""
        self.stdscr.refresh()
    
    def handle_resize(self) -> None:
        """Handle terminal resize event."""
        self.height, self.width = self.stdscr.getmaxyx()
        self.clear()
        curses.resizeterm(self.height, self.width)
    
    def create_window(self, height: int, width: int, y: int, x: int) -> Any:
        """Create a new window.
        
        Args:
            height: Window height
            width: Window width
            y: Y coordinate
            x: X coordinate
            
        Returns:
            Curses window object
        """
        try:
            return curses.newwin(height, width, y, x)
        except curses.error:
            return None
    
    def center_text(self, text: str, width: Optional[int] = None) -> str:
        """Center text within given width.
        
        Args:
            text: Text to center
            width: Width to center within (defaults to screen width)
            
        Returns:
            Centered text string
        """
        if width is None:
            width = self.width
        return text.center(width)
    
    def truncate_text(self, text: str, max_length: int, ellipsis: str = '...') -> str:
        """Truncate text to specified length.
        
        Args:
            text: Text to truncate
            max_length: Maximum length
            ellipsis: String to indicate truncation
            
        Returns:
            Truncated text
        """
        if len(text) <= max_length:
            return text
        return text[:max_length-len(ellipsis)] + ellipsis
    
    def render_table(self, headers: Dict[str, int], rows: list, start_y: int, 
                    start_x: int, max_rows: Optional[int] = None) -> int:
        """Render a table with given headers and rows.
        
        Args:
            headers: Dict of column name to width
            rows: List of row data
            start_y: Starting Y coordinate
            start_x: Starting X coordinate
            max_rows: Maximum number of rows to display
            
        Returns:
            Number of rows rendered
        """
        y = start_y
        
        # Render headers
        x = start_x
        for header, width in headers.items():
            self.safe_addstr(y, x, header.ljust(width)[:width], 
                           curses.color_pair(5) | curses.A_BOLD)
            x += width + 1
        y += 1
        
        # Render rows
        if max_rows is None:
            max_rows = self.height - y - 1
            
        for row in rows[:max_rows]:
            x = start_x
            for col, width in headers.items():
                value = str(row.get(col, ''))
                self.safe_addstr(y, x, value.ljust(width)[:width])
                x += width + 1
            y += 1
            
        return min(len(rows), max_rows)