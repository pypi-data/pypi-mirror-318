import re
from typing import Optional
from .tools_eval import is_valid_url

__all__ = [
    'short_link',
    'make_clickable',
    'extract_url',
    'is_valid_url',
    'print_clickable_link'
]

def short_link(url: str, display_text: Optional[str] = None) -> str:
    """Create a clickable terminal hyperlink with optional display text."""
    display = display_text or url
    return f'\033]8;;{url}\033\\{display}\033]8;;\033\\'

def make_clickable(text: str, url: str) -> str:
    """Make text clickable with a URL."""
    return short_link(url, text)

def extract_url(hyperlink: str) -> Optional[str]:
    """Extract URL from a terminal hyperlink."""
    pattern = r'\033\]8;;(.*?)\033\\'
    match = re.search(pattern, hyperlink)
    return match.group(1) if match else None

def is_valid_url(url: str) -> bool:
    """Check if string is a valid URL."""
    pattern = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    return bool(re.match(pattern, url)) 

def print_clickable_link(url, display_text):
    # Use the OSC 8 escape sequence to start the hyperlink
    # Then use the ST escape to stop it.
    print(f'\033]8;;{url}\033\\{display_text}\033]8;;\033\\')

