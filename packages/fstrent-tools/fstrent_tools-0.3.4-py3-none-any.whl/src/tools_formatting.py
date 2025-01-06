from pprint import pformat
from typing import Any, Optional

__all__ = [
    'format_table',
    'format_list',
    'format_dict',
    'indent_text',
    'print_adv',
    'print_func_name',
    'print_line',
    'print_obj'
]


def format_table(data: list, headers: Optional[list] = None, padding: int = 2) -> str:
    """Format data as a table with optional headers."""
    if not data:
        return ""
    
    # Determine column widths
    if headers:
        all_rows = [headers] + data
    else:
        all_rows = data
    
    widths = []
    for i in range(len(all_rows[0])):
        widths.append(max(len(str(row[i])) for row in all_rows) + padding)
    
    # Build table
    result = []
    if headers:
        result.append(''.join(str(h).ljust(w) for h, w in zip(headers, widths)))
        result.append('-' * (sum(widths) - padding))
    
    for row in data:
        result.append(''.join(str(cell).ljust(w) for cell, w in zip(row, widths)))
    
    return '\n'.join(result)

def format_list(items: list, bullet: str = '•', indent: int = 2) -> str:
    """Format a list with bullets and indentation."""
    indent_str = ' ' * indent
    return '\n'.join(f"{indent_str}{bullet} {item}" for item in items)

def format_dict(d: dict, indent: int = 2) -> str:
    """Format a dictionary with indentation."""
    return pformat(d, indent=indent)

def indent_text(text: str, indent: int = 4) -> str:
    """Indent each line of text by specified number of spaces."""
    indent_str = ' ' * indent
    return '\n'.join(indent_str + line for line in text.splitlines())

def print_adv(*args: Any, sep: str = ' ', end: str = '\n', indent: int = 0) -> None:
    """Advanced print with indentation support."""
    print(' ' * indent + sep.join(str(arg) for arg in args), end=end, flush=True)

def print_func_name(func_name: str, args: Optional[dict] = None) -> None:
    """Print function name with optional arguments."""
    if args:
        args_str = ', '.join(f'{k}={v}' for k, v in args.items())
        print(f"{func_name}({args_str})", flush=True)
    else:
        print(func_name, flush=True)

def print_line(char: str = '-', length: int = 80) -> None:
    """Print a line of specified character and length."""
    print(char * length, flush=True)

def print_obj(obj: Any, indent: int = 4, width: int = 80) -> None:
    """Pretty print an object."""
    print(pformat(obj, indent=indent, width=width))

