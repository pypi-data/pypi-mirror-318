#!/usr/bin/env python3
"""Theme-aware display handling functionality."""

import curses
import json
import os
from pathlib import Path
from typing import Tuple, Optional, Dict, Any, List, Union


class Display:
    """Handles the terminal UI display with theme support."""
    
    def __init__(self, stdscr, theme_file: Optional[Path] = None):
        """Initialize the display.
        
        Args:
            stdscr: curses window object
            theme_file: Optional path to theme configuration file
        """
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.themes = self._load_themes(theme_file)
        self.current_theme = self._detect_terminal_theme()
        
        # Initialize curses settings
        self.stdscr.keypad(1)  # Enable keypad
        curses.halfdelay(1)    # Set input mode to avoid blocking
        curses.use_env(True)   # Enable terminal size detection
        
        # Create a pad for double buffering
        self.pad = curses.newpad(self.height + 1, self.width + 1)
        self.pad.keypad(1)
        
        # Setup colors and hide cursor
        self.setup_colors()
        try:
            curses.curs_set(0)
        except curses.error:
            pass

    def _load_themes(self, theme_file: Optional[Path] = None) -> Dict:
        """Load theme configurations from JSON file."""
        if theme_file is None:
            # Use the same config folder as ai_process_patterns.json
            theme_file = Path(__file__).parent.parent.parent / 'config' / 'themes.json'
            
        try:
            with open(theme_file) as f:
                return json.load(f)['themes']
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            # Return minimal default theme if file loading fails
            return {
                "dark": {
                    "colors": {
                        "normal": {"fg": "GREEN", "bg": -1, "attrs": []},
                        "selected": {"fg": "BLACK", "bg": "GREEN", "attrs": []},
                        "warning": {"fg": "YELLOW", "bg": -1, "attrs": []},
                        "critical": {"fg": "RED", "bg": -1, "attrs": []},
                        "info": {"fg": "CYAN", "bg": -1, "attrs": []},
                        "ai_process": {"fg": "MAGENTA", "bg": -1, "attrs": []},
                        "header": {"fg": "BLUE", "bg": -1, "attrs": []},
                        "footer": {"fg": "WHITE", "bg": -1, "attrs": []}
                    },
                    "progress_bar": {
                        "filled": "█",
                        "empty": "░",
                        "thresholds": {"critical": 80, "warning": 60}
                    }
                }
            }

    def _detect_terminal_theme(self) -> str:
        """Detect appropriate terminal theme."""
        # Check for Ubuntu-specific indicators
        if os.getenv('UBUNTU_MENUPROXY') or \
           os.getenv('GNOME_DESKTOP_SESSION_ID') or \
           os.path.exists('/etc/ubuntu-release'):
            return 'ubuntu'
            
        # Check for explicit dark/light indicators
        if os.getenv('COLORFGBG'):
            try:
                fg, bg = map(int, os.getenv('COLORFGBG', '').split(';'))
                return 'dark' if bg < 8 else 'light'
            except ValueError:
                pass
                
        # Check terminal name hints
        term = os.getenv('TERM', '').lower()
        if any(x in term for x in ['dark', 'black']):
            return 'dark'
        elif any(x in term for x in ['light', 'white']):
            return 'light'
            
        return 'dark'  # Default to dark theme

    def _get_curses_color(self, color_name: str) -> int:
        """Convert color name to curses color constant."""
        color_map = {
            'BLACK': curses.COLOR_BLACK,
            'RED': curses.COLOR_RED,
            'GREEN': curses.COLOR_GREEN,
            'YELLOW': curses.COLOR_YELLOW,
            'BLUE': curses.COLOR_BLUE,
            'MAGENTA': curses.COLOR_MAGENTA,
            'CYAN': curses.COLOR_CYAN,
            'WHITE': curses.COLOR_WHITE
        }
        return color_map.get(color_name.upper(), -1)

    def _get_curses_attr(self, attr_name: str) -> int:
        """Convert attribute name to curses attribute constant."""
        attr_map = {
            'BOLD': curses.A_BOLD,
            'REVERSE': curses.A_REVERSE,
            'UNDERLINE': curses.A_UNDERLINE,
            'BLINK': curses.A_BLINK
        }
        return attr_map.get(attr_name.upper(), 0)

    def setup_colors(self) -> None:
        """Initialize color pairs based on current theme."""
        try:
            curses.start_color()
            curses.use_default_colors()
            
            theme = self.themes.get(self.current_theme, self.themes['dark'])
            colors = theme['colors']
            
            # Map color roles to pair numbers
            self.color_pairs = {
                'normal': 1,
                'selected': 2,
                'warning': 3,
                'critical': 4,
                'info': 5,
                'ai_process': 6,
                'header': 7,
                'footer': 8
            }
            
            # Initialize each color pair
            for role, pair_id in self.color_pairs.items():
                if role in colors:
                    fg = self._get_curses_color(colors[role]['fg'])
                    bg = self._get_curses_color(colors[role]['bg']) \
                        if isinstance(colors[role]['bg'], str) else colors[role]['bg']
                    curses.init_pair(pair_id, fg, bg)

        except Exception:
            pass

    def get_theme_attr(self, role: str) -> int:
        """Get color and attributes for a theme role."""
        theme = self.themes.get(self.current_theme, self.themes['dark'])
        colors = theme['colors']
        
        if role in colors and role in self.color_pairs:
            attr = curses.color_pair(self.color_pairs[role])
            for attr_name in colors[role].get('attrs', []):
                attr |= self._get_curses_attr(attr_name)
            return attr
            
        return curses.A_NORMAL

    def get_color(self, value: float) -> int:
        """Get appropriate color based on value percentage."""
        theme = self.themes.get(self.current_theme, self.themes['dark'])
        thresholds = theme['progress_bar']['thresholds']
        
        try:
            if value >= thresholds['critical']:
                return self.get_theme_attr('critical')
            elif value >= thresholds['warning']:
                return self.get_theme_attr('warning')
            return self.get_theme_attr('normal')
        except Exception:
            return curses.A_NORMAL

    def get_dimensions(self) -> Tuple[int, int]:
        """Get current terminal dimensions."""
        self.height, self.width = self.stdscr.getmaxyx()
        return self.height, self.width

    def create_bar(self, value: float, width: int) -> Tuple[str, int]:
        """Create a progress bar with theme-aware styling."""
        theme = self.themes.get(self.current_theme, self.themes['dark'])
        bar_chars = theme['progress_bar']
        
        filled_width = int(value * width / 100)
        bar = (bar_chars['filled'] * filled_width + 
               bar_chars['empty'] * (width - filled_width))
        color = self.get_color(value)
        
        return bar, color

    def safe_addstr(self, y: int, x: int, text: str, attr: Optional[int] = None) -> None:
        """Safely add a string to the screen."""
        try:
            if y >= self.height or x >= self.width:
                return
                
            max_length = self.width - x
            if len(text) > max_length:
                text = text[:max_length]
                
            if attr is not None:
                self.pad.addstr(y, x, text, attr)
            else:
                self.pad.addstr(y, x, text, self.get_theme_attr('normal'))
        except curses.error:
            pass

    def clear(self) -> None:
        """Clear the screen."""
        self.pad.clear()
    
    def refresh(self) -> None:
        """Refresh the screen using double buffering."""
        try:
            # Copy pad content to screen
            self.pad.noutrefresh(0, 0, 0, 0, self.height - 1, self.width - 1)
            curses.doupdate()
        except curses.error:
            pass
    
    def handle_resize(self) -> None:
        """Handle terminal resize event."""
        # Get new dimensions
        new_height, new_width = self.stdscr.getmaxyx()
        
        # Only process if dimensions actually changed
        if new_height != self.height or new_width != self.width:
            self.height = new_height
            self.width = new_width
            
            # Recreate pad with new dimensions
            self.pad = curses.newpad(self.height + 1, self.width + 1)
            self.pad.keypad(1)
            
            # Clear and resize
            curses.resize_term(self.height, self.width)
            curses.flushinp()  # Flush input buffer
            
            # Reset terminal state
            self.stdscr.clear()
            self.stdscr.refresh()
            
            # Force immediate refresh of pad
            self.refresh()
    
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

    def render_table(self, headers: Dict[str, int], rows: List[Dict[str, Any]], 
                    start_y: int, start_x: int, 
                    max_rows: Optional[int] = None) -> int:
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
                           self.get_theme_attr('info') | curses.A_BOLD)
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

    def set_theme(self, theme_name: str) -> None:
        """Switch to a different theme.
        
        Args:
            theme_name: Name of the theme to use
        """
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.setup_colors()