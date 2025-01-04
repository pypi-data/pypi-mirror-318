#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
from typing import Dict, Tuple


class ColorManager:
    """Manages color allocation and conversion for the terminal UI."""

    def __init__(self):
        """Initialize the color manager with proper terminal color support detection."""
        self.color_cache: Dict[str, int] = {}  # Maps hex colors to allocated indices
        self.next_color_index = 16  # Start after basic colors (0-15)
        self.max_colors = curses.COLORS if hasattr(curses, 'COLORS') else 8
        self.can_change = curses.can_change_color() if hasattr(curses, 'can_change_color') else False
        
        # Standard color map for fallback
        self.color_map = {
            'BLACK': curses.COLOR_BLACK,
            'RED': curses.COLOR_RED,
            'GREEN': curses.COLOR_GREEN,
            'YELLOW': curses.COLOR_YELLOW,
            'BLUE': curses.COLOR_BLUE,
            'MAGENTA': curses.COLOR_MAGENTA,
            'CYAN': curses.COLOR_CYAN,
            'WHITE': curses.COLOR_WHITE
        }

    def get_color_index(self, color_spec: str) -> int:
        """
        Convert a color specification (hex or named) to a curses color index.
        
        Args:
            color_spec: Either a hex color (#RRGGBB) or a named color
            
        Returns:
            int: A curses color index
        """
        # Handle named colors
        if not color_spec.startswith('#'):
            color_upper = color_spec.upper()
            return self.color_map.get(color_upper, -1)

        # Handle hex colors
        if color_spec in self.color_cache:
            return self.color_cache[color_spec]

        # Try to allocate new color if possible
        if self.can_change and self.next_color_index < self.max_colors:
            try:
                r, g, b = self._hex_to_curses_rgb(color_spec)
                color_index = self.next_color_index
                curses.init_color(color_index, r, g, b)
                self.color_cache[color_spec] = color_index
                self.next_color_index += 1
                return color_index
            except curses.error:
                pass  # Fall through to approximation

        # Fallback to approximation
        return self._approximate_color(color_spec)

    def _hex_to_curses_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """
        Convert hex color (#RRGGBB) to curses RGB values (0-1000 range).
        
        Args:
            hex_color: Color in #RRGGBB format
            
        Returns:
            tuple: (r, g, b) values in 0-1000 range
        """
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Convert to curses 0-1000 range
        return (
            int((r / 255) * 1000),
            int((g / 255) * 1000),
            int((b / 255) * 1000)
        )

    def _approximate_color(self, hex_color: str) -> int:
        """
        Approximate a hex color using available terminal colors.
        
        Args:
            hex_color: Color in #RRGGBB format
            
        Returns:
            int: Best matching curses color constant
        """
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Simple approximation logic
        if max(r, g, b) < 85:  # Very dark
            return curses.COLOR_BLACK
        elif r > max(g, b) + 50:  # Predominantly red
            return curses.COLOR_RED
        elif g > max(r, b) + 50:  # Predominantly green
            return curses.COLOR_GREEN
        elif b > max(r, g) + 50:  # Predominantly blue
            return curses.COLOR_BLUE
        elif r > 200 and g > 200 and b < 100:  # Yellow-ish
            return curses.COLOR_YELLOW
        elif r > 200 and b > 200 and g < 100:  # Magenta-ish
            return curses.COLOR_MAGENTA
        elif g > 200 and b > 200 and r < 100:  # Cyan-ish
            return curses.COLOR_CYAN
        elif min(r, g, b) > 170:  # Very light
            return curses.COLOR_WHITE
            
        # Default fallback
        return curses.COLOR_WHITE
