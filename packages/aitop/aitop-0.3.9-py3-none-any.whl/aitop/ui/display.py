#!/usr/bin/env python3
"""Theme-aware display handling functionality."""

import curses
import os
from pathlib import Path
from typing import Tuple, Optional, Dict, Any, List, Union

from ..config import load_themes


class Display:
    """Handles the terminal UI display with theme support."""
    
    def __init__(self, stdscr, theme_file: Optional[Path] = None):
        """Initialize the display.
        
        Args:
            stdscr: curses window object
            theme_file: Optional path to theme configuration file
        """
        self.stdscr = stdscr
        
        # Initialize curses settings first
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        curses.use_env(True)   # Enable terminal size detection
        
        # Set non-blocking mode with minimal delay
        self.stdscr.nodelay(1)  # Make getch() non-blocking
        self.stdscr.timeout(0)  # Set timeout to 0ms
        
        # Configure window
        self.stdscr.keypad(1)  # Enable keypad
        
        # Save original terminal state
        try:
            curses.def_prog_mode()  # Save current terminal mode
        except curses.error:
            pass
            
        # Load themes before handling dimensions
        self.themes = self._load_themes(theme_file)
        self.current_theme = self._detect_terminal_theme()
        
        # Set minimum required dimensions
        self.min_height = 24  # Minimum height needed for basic display
        self.min_width = 80   # Minimum width needed for basic display
        
        # Get initial dimensions
        self.height, self.width = stdscr.getmaxyx()
        
        # Calculate actual dimensions
        actual_height = max(self.height, self.min_height)
        actual_width = max(self.width, self.min_width)
        
        # Create pad with actual dimensions
        self.pad = curses.newpad(actual_height, actual_width)
        self.pad.keypad(1)
        
        # Set initial display area
        self.display_height = actual_height
        self.display_width = actual_width
        
        # Calculate visible area
        visible_height = min(self.height, self.display_height)
        visible_width = min(self.width, self.display_width)
        
        # Ensure initial display matches visible area
        self.pad.noutrefresh(0, 0, 0, 0, visible_height - 1, visible_width - 1)
        curses.doupdate()
        
        # Save original cursor state and hide cursor
        try:
            self.original_cursor = curses.curs_set(0)
        except:
            self.original_cursor = None
            
        # Setup colors
        self.setup_colors()

    def _load_themes(self, theme_file: Optional[Path] = None) -> Dict:
        """Load theme configurations from JSON file."""
        try:
            return load_themes(theme_file)
        except RuntimeError:
            # Return minimal default theme if file loading fails
            return {
                "default": {
                    "name": "Default Terminal",
                    "description": "Standard theme based on htop colors",
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
        """Detect appropriate terminal theme based on terminal environment."""
        try:
            # First check if user has explicitly set a preferred theme
            if os.getenv('AITOP_THEME'):
                theme = os.getenv('AITOP_THEME').lower()
                if theme in self.themes:
                    return theme

            # Check for explicit background color indication
            if os.getenv('COLORFGBG'):
                try:
                    fg, bg = map(int, os.getenv('COLORFGBG', '').split(';'))
                    return 'light' if bg >= 8 else 'default'
                except ValueError:
                    pass

            # Check for common terminal environments
            term = os.getenv('TERM', '').lower()
            term_program = os.getenv('TERM_PROGRAM', '').lower()
            colorterm = os.getenv('COLORTERM', '').lower()
            
            # Modern terminal detection
            if term_program in ['vscode', 'vscode-integrated-terminal', 'visual-studio-code']:
                return 'default'
            if term_program in ['apple_terminal', 'iterm.app', 'terminator']:
                return 'default'
            
            # Check for true color support
            if 'truecolor' in colorterm or '24bit' in colorterm:
                return 'default'
                
            # Check common terminal types
            if any(x in term for x in ['xterm', 'rxvt', 'konsole']):
                return 'default'
            if 'screen' in term or 'tmux' in term:
                return 'default'
                
            # For basic terminals, prefer high contrast
            if term in ['linux', 'dumb']:
                return 'high_contrast'

            return 'default'  # Safe default for modern terminals
        except Exception:
            return 'default'

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
            if not curses.has_colors():
                return

            curses.start_color()
            curses.use_default_colors()
            
            theme = self.themes.get(self.current_theme, self.themes['default'])
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
                    color_config = colors[role]
                    # Get foreground color
                    fg = self._get_curses_color(color_config['fg'])
                    
                    # Handle background color
                    bg = -1  # Default to terminal's default background
                    if isinstance(color_config['bg'], str):
                        bg = self._get_curses_color(color_config['bg'])
                    elif isinstance(color_config['bg'], int) and color_config['bg'] != -1:
                        bg = color_config['bg']
                    
                    try:
                        curses.init_pair(pair_id, fg, bg)
                    except curses.error:
                        # Fallback to simpler color pair if initialization fails
                        curses.init_pair(pair_id, fg, -1)

        except Exception as e:
            # Log error but continue with default attributes
            import sys
            print(f"Color setup error: {str(e)}", file=sys.stderr)

    def get_theme_attr(self, role: str) -> int:
        """Get color and attributes for a theme role."""
        try:
            theme = self.themes.get(self.current_theme)
            if not theme:
                theme = self.themes.get('default')
                if not theme:
                    return curses.A_NORMAL
                    
            colors = theme['colors']
            
            if role in colors and role in self.color_pairs:
                attr = curses.color_pair(self.color_pairs[role])
                for attr_name in colors[role].get('attrs', []):
                    attr |= self._get_curses_attr(attr_name)
                return attr
                
            return curses.A_NORMAL
        except Exception:
            return curses.A_NORMAL

    def get_color(self, value: float) -> int:
        """Get appropriate color based on value percentage."""
        theme = self.themes.get(self.current_theme, self.themes['default'])
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
        """Create a progress bar with theme-aware styling.
        
        Args:
            value: Percentage value (0-100)
            width: Desired width of the progress bar
            
        Returns:
            Tuple of (bar_string, color_attribute)
        """
        # Ensure value is within bounds
        value = max(0, min(100, value))
        
        # Get theme characters and color
        theme = self.themes.get(self.current_theme, self.themes['default'])
        bar_chars = theme['progress_bar']
        color = self.get_color(value)
        
        # Calculate available width
        available_width = min(width, self.width)
        if available_width <= 0:
            return '', color
            
        # Calculate filled portion
        filled_width = int((value * available_width) / 100)
        empty_width = available_width - filled_width
        
        # Create bar with exact width
        bar = (bar_chars['filled'] * filled_width + 
               bar_chars['empty'] * empty_width)
               
        return bar, color

    def safe_addstr(self, y: int, x: int, text: str, attr: Optional[int] = None) -> None:
        """Safely add a string to the screen."""
        try:
            # Update current dimensions
            self.height, self.width = self.stdscr.getmaxyx()
            
            # Calculate visible area
            visible_height = min(self.height, self.display_height)
            visible_width = min(self.width, self.display_width)
            
            # Don't write if position is outside visible area
            if y >= visible_height or x >= visible_width:
                return
                
            # Calculate available space
            remaining_width = visible_width - x
            if remaining_width <= 0:
                return
                
            # Get current pad dimensions
            pad_height, pad_width = self.pad.getmaxyx()
            if y >= pad_height or x >= pad_width:
                return
                
            # Truncate text if needed
            if len(text) > remaining_width:
                text = text[:remaining_width]
            
            # Write text with appropriate attributes
            try:
                if attr is not None:
                    self.pad.addstr(y, x, text, attr)
                else:
                    self.pad.addstr(y, x, text, self.get_theme_attr('normal'))
            except curses.error:
                # Handle specific error cases
                if y == visible_height - 1 and x + len(text) == visible_width:
                    # Special case: writing to bottom-right corner
                    if len(text) > 0:
                        self.pad.addstr(y, x, text[:-1], attr or self.get_theme_attr('normal'))
        except curses.error:
            pass

    def clear(self) -> None:
        """Clear the screen."""
        self.pad.clear()
    
    def _enforce_min_dimensions(self) -> None:
        """Enforce minimum terminal dimensions."""
        try:
            # Get current dimensions
            self.height, self.width = self.stdscr.getmaxyx()
            
            # Check if resize is needed
            if self.height < self.min_height or self.width < self.min_width:
                # Calculate new dimensions
                new_height = max(self.height, self.min_height)
                new_width = max(self.width, self.min_width)
                
                # Only resize if dimensions actually changed
                if (new_height != self.display_height or 
                    new_width != self.display_width):
                    # Create new pad with exact dimensions
                    new_pad = curses.newpad(new_height, new_width)
                    new_pad.keypad(1)
                    
                    try:
                        # Copy content from old pad
                        old_height, old_width = self.pad.getmaxyx()
                        copy_height = min(old_height, new_height)
                        copy_width = min(old_width, new_width)
                        
                        # Copy content line by line
                        for y in range(copy_height):
                            for x in range(copy_width):
                                try:
                                    char = self.pad.inch(y, x)
                                    new_pad.addch(y, x, char)
                                except curses.error:
                                    continue
                        
                        # Resize terminal and update dimensions
                        curses.resize_term(new_height, new_width)
                        self.height = new_height
                        self.width = new_width
                        self.display_height = new_height
                        self.display_width = new_width
                        
                        # Switch to new pad and update immediately
                        old_pad = self.pad
                        self.pad = new_pad
                        self.pad.noutrefresh(0, 0, 0, 0, self.height - 1, self.width - 1)
                        curses.doupdate()
                        
                        # Clean up old pad
                        del old_pad
                    except curses.error:
                        # Fallback to new pad if copy fails
                        self.pad = new_pad
                        self.pad.clear()
                        self.pad.noutrefresh(0, 0, 0, 0, self.height - 1, self.width - 1)
                        curses.doupdate()
        except curses.error:
            pass

    def refresh(self) -> None:
        """Refresh the screen using double buffering."""
        try:
            # Get current dimensions
            self.height, self.width = self.stdscr.getmaxyx()
            
            # Always ensure minimum dimensions
            actual_height = max(self.height, self.min_height)
            actual_width = max(self.width, self.min_width)
            
            # Check if dimensions changed
            if (actual_height != self.display_height or 
                actual_width != self.display_width):
                
                # Create new pad with actual dimensions
                new_pad = curses.newpad(actual_height, actual_width)
                new_pad.keypad(1)
                
                try:
                    # Copy content from old pad
                    old_height, old_width = self.pad.getmaxyx()
                    copy_height = min(old_height, actual_height)
                    copy_width = min(old_width, actual_width)
                    
                    # Copy content line by line
                    for y in range(copy_height):
                        for x in range(copy_width):
                            try:
                                char = self.pad.inch(y, x)
                                new_pad.addch(y, x, char)
                            except curses.error:
                                continue
                    
                    # Switch to new pad and update immediately
                    old_pad = self.pad
                    self.pad = new_pad
                    
                    # Update display area
                    self.display_height = actual_height
                    self.display_width = actual_width
                    
                    # Clean up old pad
                    del old_pad
                except curses.error:
                    # Fallback to new pad if copy fails
                    self.pad = new_pad
                    self.pad.clear()
            
            # Calculate visible area
            visible_height = min(self.height, self.display_height)
            visible_width = min(self.width, self.display_width)
            
            # Refresh only the visible portion
            self.pad.noutrefresh(0, 0, 0, 0, visible_height - 1, visible_width - 1)
            curses.doupdate()
        except curses.error:
            pass
    
    def handle_resize(self) -> None:
        """Handle terminal resize event."""
        try:
            # Get current dimensions
            self.height, self.width = self.stdscr.getmaxyx()
            
            # Always ensure minimum dimensions
            actual_height = max(self.height, self.min_height)
            actual_width = max(self.width, self.min_width)
            
            # Check if dimensions changed
            if (actual_height != self.display_height or 
                actual_width != self.display_width):
                
                # Create new pad with actual dimensions
                new_pad = curses.newpad(actual_height, actual_width)
                new_pad.keypad(1)
                
                try:
                    # Copy content from old pad
                    old_height, old_width = self.pad.getmaxyx()
                    copy_height = min(old_height, actual_height)
                    copy_width = min(old_width, actual_width)
                    
                    # Copy content line by line
                    for y in range(copy_height):
                        for x in range(copy_width):
                            try:
                                char = self.pad.inch(y, x)
                                new_pad.addch(y, x, char)
                            except curses.error:
                                continue
                    
                    # Switch to new pad and update immediately
                    old_pad = self.pad
                    self.pad = new_pad
                    
                    # Update display area
                    self.display_height = actual_height
                    self.display_width = actual_width
                    
                    # Clean up old pad
                    del old_pad
                except curses.error:
                    # Fallback to new pad if copy fails
                    self.pad = new_pad
                    self.pad.clear()
            
            # Calculate visible area
            visible_height = min(self.height, self.display_height)
            visible_width = min(self.width, self.display_width)
            
            # Refresh only the visible portion
            self.pad.noutrefresh(0, 0, 0, 0, visible_height - 1, visible_width - 1)
            curses.doupdate()
        except curses.error:
            pass
    
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
        # Update current dimensions
        self.height, self.width = self.stdscr.getmaxyx()
        
        # Use provided width or current terminal width
        target_width = width if width is not None else self.width
        
        # Ensure width is positive
        target_width = max(0, target_width)
        
        # Handle empty or zero width cases
        if not text or target_width == 0:
            return ''
            
        # Truncate text if longer than width
        if len(text) > target_width:
            return self.truncate_text(text, target_width)
            
        # Calculate padding
        padding = target_width - len(text)
        left_pad = padding // 2
        right_pad = padding - left_pad
        
        # Return centered text
        return ' ' * left_pad + text + ' ' * right_pad
    
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
        # Get current dimensions
        self.height, self.width = self.stdscr.getmaxyx()
        
        # Calculate visible area
        visible_height = min(self.height, self.display_height)
        visible_width = min(self.width, self.display_width)
        
        # Calculate available space
        available_width = max(0, visible_width - start_x)
        if available_width <= 0 or start_y >= visible_height:
            return 0
            
        # Calculate total width needed including spacing
        total_width = sum(headers.values()) + len(headers) - 1
        
        # Scale column widths if necessary
        scaled_headers = headers.copy()
        if total_width > available_width:
            # Calculate scale factor
            scale = available_width / total_width
            # Scale each column width, ensuring minimum of 3 characters
            scaled_headers = {k: max(int(v * scale), 3) for k, v in headers.items()}
            
            # Adjust for any remaining width due to rounding
            total_scaled = sum(scaled_headers.values()) + len(scaled_headers) - 1
            if total_scaled < available_width:
                # Distribute extra space to largest columns first
                extra = available_width - total_scaled
                sorted_cols = sorted(scaled_headers.items(), key=lambda x: (-x[1], x[0]))
                for i in range(min(extra, len(sorted_cols))):
                    scaled_headers[sorted_cols[i][0]] += 1
        
        # Calculate visible rows
        visible_height = max(0, self.height - start_y - 1)
        if visible_height <= 0:
            return 0
            
        # Determine number of rows to render
        if max_rows is None:
            max_rows = visible_height
        max_rows = min(max_rows, visible_height, len(rows))
        
        # Render headers
        y = start_y
        x = start_x
        for header, width in scaled_headers.items():
            header_text = self.truncate_text(header, width)
            self.safe_addstr(y, x, header_text.ljust(width), 
                           self.get_theme_attr('info') | curses.A_BOLD)
            x += width + 1
        
        # Render rows
        rendered_rows = 0
        for row in rows[:max_rows]:
            y += 1
            x = start_x
            for col, width in scaled_headers.items():
                value = str(row.get(col, ''))
                cell_text = self.truncate_text(value, width)
                self.safe_addstr(y, x, cell_text.ljust(width))
                x += width + 1
            rendered_rows += 1
            
        return rendered_rows

    def set_theme(self, theme_name: str) -> None:
        """Switch to a different theme.
        
        Args:
            theme_name: Name of the theme to use
        """
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.setup_colors()
            
    def get_terminal_info(self) -> Dict[str, str]:
        """Get terminal environment information for debugging.
        
        Returns:
            Dictionary containing terminal environment details
        """
        return {
            'TERM': os.getenv('TERM', ''),
            'TERM_PROGRAM': os.getenv('TERM_PROGRAM', ''),
            'COLORTERM': os.getenv('COLORTERM', ''),
            'COLORFGBG': os.getenv('COLORFGBG', ''),
            'AITOP_THEME': os.getenv('AITOP_THEME', ''),
            'has_colors': str(curses.has_colors()),
            'can_change_color': str(curses.can_change_color()),
            'colors': str(curses.COLORS if hasattr(curses, 'COLORS') else 'unknown'),
            'color_pairs': str(curses.COLOR_PAIRS if hasattr(curses, 'COLOR_PAIRS') else 'unknown'),
            'current_theme': self.current_theme,
            'available_themes': ', '.join(self.themes.keys())
        }
        
    def cleanup(self) -> None:
        """Clean up display resources and restore terminal state."""
        try:
            # Restore original cursor state
            if self.original_cursor is not None:
                try:
                    curses.curs_set(self.original_cursor)
                except curses.error:
                    pass
            
            # Clear pad and screen
            if self.pad:
                try:
                    self.pad.clear()
                    self.pad.refresh()
                except curses.error:
                    pass
                
            # Reset terminal mode
            try:
                curses.reset_prog_mode()
            except curses.error:
                pass
                
            # Final screen refresh
            try:
                self.stdscr.clear()
                self.stdscr.refresh()
            except curses.error:
                pass
        except Exception:
            pass
