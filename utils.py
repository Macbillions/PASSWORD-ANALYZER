"""
Utility functions for Password Strength Checker
"""

import sys
from config import VULNERABILITY_COLORS, CRACK_TIME_THRESHOLDS

# Fix Unicode encoding on Windows
if sys.platform == 'win32':
    import os
    os.system('chcp 65001 > nul')  # UTF-8 code page


def format_crack_time_human(seconds: float) -> str:
    """
    Format time in seconds to human-readable format.
    
    Args:
        seconds: Time in seconds
        
    Returns:
        Human-readable time string
    """
    if seconds < 1:
        return f"< 1 second"
    elif seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f} minutes"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.1f} hours"
    elif seconds < 2592000:
        days = seconds / 86400
        return f"{days:.1f} days"
    elif seconds < 31536000:
        months = seconds / 2592000
        return f"{months:.1f} months"
    elif seconds < 3153600000:
        years = seconds / 31536000
        return f"{years:.1f} years"
    else:
        trillions = seconds / 31536000 / 1e12
        return f"{trillions:.1f} trillion years"


def get_vulnerability_status(seconds: float) -> tuple:
    """
    Get vulnerability status and color based on crack time.
    
    Args:
        seconds: Time to crack in seconds
        
    Returns:
        Tuple of (emoji_color, description)
    """
    if seconds < 1:
        return VULNERABILITY_COLORS['instant'], "🔴 Extremely vulnerable - instant crack"
    elif seconds < 60:
        return VULNERABILITY_COLORS['seconds'], "🔴 Very vulnerable - cracks in seconds"
    elif seconds < 3600:
        return VULNERABILITY_COLORS['minutes'], "🟠 Vulnerable - cracks in minutes"
    elif seconds < 86400:
        return VULNERABILITY_COLORS['hours'], "🟠 Weak - cracks in hours"
    elif seconds < 2592000:
        return VULNERABILITY_COLORS['days'], "🟡 Fair - cracks in days/weeks"
    elif seconds < 31536000:
        return VULNERABILITY_COLORS['months'], "🟢 Good - would take months to crack"
    elif seconds < 3153600000:
        return VULNERABILITY_COLORS['years'], "🟢 Strong - would take decades to crack"
    else:
        return VULNERABILITY_COLORS['uncrackable'], "🟢🟢 Very Strong - practically uncrackable"


def print_header(title: str) -> None:
    """
    Print a formatted header.
    
    Args:
        title: Header title
    """
    green = "\033[92m"
    reset = "\033[0m"
    print("\n" + green + "="*60)
    print(f"[PASS-INFO] {title}")
    print("="*60 + reset + "\n")


def print_section(title: str) -> None:
    """
    Print a formatted section title.
    
    Args:
        title: Section title
    """
    print(f"\n{title}:")


def print_item(label: str, value: str, icon: str = "   ") -> None:
    """
    Print a formatted item.
    
    Args:
        label: Item label
        value: Item value
        icon: Icon prefix
    """
    print(f"{icon} {label}: {value}")


def clear_screen() -> None:
    """Clear the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
