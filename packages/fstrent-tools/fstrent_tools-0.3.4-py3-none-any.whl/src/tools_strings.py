import re

__all__ = [
    'IsEnglish',
    'strip_formatting',
    'format_disp_age',
    'truncate_string',
    'snake_to_camel',
    'camel_to_snake',
    'remove_special_chars',
    'extract_numbers',
    'pad_string',
    'lpad',
    'rpad',
    'cpad',
    'left',
    'right',
    'mid',
    'display_length'
]

def IsEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def strip_formatting(in_str: str) -> str:
    """Remove ANSI escape sequences from string."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', in_str)

def format_disp_age(age_mins: int, fmt_style: int = 1) -> str:
    """Format age in minutes to human-readable string."""
    if fmt_style == 1:
        days = age_mins // (24 * 60)
        hours = (age_mins % (24 * 60)) // 60
        mins = age_mins % 60
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0 or days > 0:
            parts.append(f"{hours}h")
        parts.append(f"{mins}m")
        return " ".join(parts)
    return str(age_mins)

def format_disp_age2(in_age_secs):
    in_age_secs = int(in_age_secs)    
    age_days    = in_age_secs // (24 * 60 * 60)
    age_hours   = (in_age_secs // (60 * 60)) % 24
    age_minutes = (in_age_secs // 60) % 60
    age_secs    = in_age_secs % 60
    disp_age = ''
    if age_days > 0:
        disp_age += f"{age_days} "
    if age_hours > 0:
        disp_age += f"{age_hours}:"
    if age_minutes >= 0:
        disp_age += f"{age_minutes}:"
    if age_secs >= 0:
        disp_age += f"{age_secs}"
    return disp_age

def truncate_string(text: str, max_length: int, suffix: str = '...') -> str:
    """Truncate string to max_length, adding suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def snake_to_camel(snake_str: str) -> str:
    """Convert snake_case to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str: str) -> str:
    """Convert camelCase to snake_case."""
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', camel_str).lower()

def remove_special_chars(text: str, keep_spaces: bool = True) -> str:
    """Remove special characters from string."""
    pattern = r'[^a-zA-Z0-9\s]' if keep_spaces else r'[^a-zA-Z0-9]'
    return re.sub(pattern, '', text)

def extract_numbers(text: str) -> list:
    """Extract only numbers from string."""
    return re.findall(r'\d+', text)

def pad_string(text: str, length: int, char: str = ' ', align: str = 'left') -> str:
    """
    Pad string to specified length.
    align: 'left', 'right', or 'center'
    """
    if align == 'left':
        return text.ljust(length, char)
    elif align == 'right':
        return text.rjust(length, char)
    else:  # center
        return text.center(length, char)

def lpad(in_str: str, length: int, pad_char: str = ' ') -> str:
    """Left pad string to specified length."""
    return str(in_str).rjust(length, pad_char)

def rpad(in_str: str, length: int, pad_char: str = ' ') -> str:
    """Right pad string to specified length."""
    return str(in_str).ljust(length, pad_char)

def cpad(in_str: str, length: int, pad_char: str = ' ') -> str:
    """Center pad string to specified length."""
    return str(in_str).center(length, pad_char)

def left(in_str: str, length: int) -> str:
    """Get left substring of specified length."""
    return str(in_str)[:length]

def right(in_str: str, length: int) -> str:
    """Get right substring of specified length."""
    return str(in_str)[-length:]

def mid(in_str: str, start_position: int, length: int) -> str:
    """Get substring from start_position of specified length."""
    return str(in_str)[start_position:start_position + length]

def display_length(in_str: str) -> int:
    """Get display length of string (excluding ANSI escape sequences)."""
    return len(strip_formatting(in_str))
