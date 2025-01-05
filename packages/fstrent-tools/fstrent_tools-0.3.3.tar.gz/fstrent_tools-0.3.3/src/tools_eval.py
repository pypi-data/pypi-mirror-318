import os
import re
from typing import Any, Dict, List, Optional, Union

__all__ = [
    # Value validation
    'HasVal',
    'AllHaveVal',
    
    # Dictionary validation
    'DictKeyVal',
    'DictKeyValMult',
    'DictValCheck',
    
    # Format validation
    'is_valid_email',
    'is_valid_url',
    'is_valid_path',
    'is_even',
    'is_odd'
]

def HasVal(val: Any = None) -> bool:
    """
    Check if a value is non-empty.
    Returns True if:
    - String with length > 0
    - Dict with length > 0
    - List with length > 0
    - Tuple with length > 0
    - Any non-None, non-empty value
    """
    if val is None:
        return False
    elif isinstance(val, (str, dict, list, tuple)):
        return bool(len(val))
    return val is not None and val != ''

def AllHaveVal(vals: Optional[Union[Any, List[Any]]] = None, itemize_yn: str = 'N') -> bool:
    """
    Check if all values have non-empty values using HasVal.
    itemize_yn - if 'Y', prints validation results for each item
    """
    if isinstance(vals, list):
        for x in vals:
            r = HasVal(x)
            if itemize_yn == 'Y':
                print(f'r : {r}, x : {x}')
            if not r:
                return False
        return True
    return HasVal(vals)

def DictKeyVal(in_dict: Dict, k: str) -> bool:
    """Check if key exists in dictionary and has a non-None value."""
    try:
        return k in in_dict and HasVal(in_dict[k])
    except Exception as e:
        print(f'DictKeyVal ==> errored... {e}')
        return False

def DictKeyValMult(in_dict: Dict, ks: List[str]) -> bool:
    """Check if all keys exist and have non-None values."""
    return all(DictKeyVal(in_dict, k) for k in ks)

def DictValCheck(in_dict: Dict = {}, ks: Union[str, List[str]] = [], show_yn: str = 'N') -> bool:
    """
    Verify all specified values in dict have value.
    ks - allows specified keys to be checked
    show_yn - if 'Y', prints keys with no value
    """
    if not HasVal(ks):
        return True
        
    if isinstance(ks, str):
        ks = [ks]
        
    for k in ks:
        if k not in in_dict:
            return False
        v = in_dict[k]
        if not HasVal(v):
            if show_yn == 'Y':
                print(f'{k} : {v}')
            return False
    return True

def is_valid_email(email: str) -> bool:
    """Check if string is a valid email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_path(path: str) -> bool:
    """Check if string is a valid file system path."""
    try:
        return os.path.exists(os.path.dirname(path))
    except:
        return False 

def is_even(number: int) -> bool:
    return number % 2 == 0

def is_odd(number: int) -> bool:
    return number % 2 != 0
