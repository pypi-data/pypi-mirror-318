from decimal import Decimal
from pprint import pprint
import sys
import traceback
import decimal
from tools_object import EmptyObject
from typing import Any

__all__ = [
    'convert_2_boolean',
    'convert_2_dict',
    'convert_2_float',
    'convert_2_integer',
    'convert_2_list',
    'convert_2_string',
    'dec',
    'dec_2_float',
    'dec_prec',
    'dict_2_obj',
    'int_2_tf',
    'tf',
    'tf_2_int',
    'to_int',
    'to_float',
    'to_str'
]


def convert_2_boolean(value):
    """
    Converts a value to a boolean.

    Args:
        value (any): The value to convert.

    Returns:
        bool: The boolean representation of the value.
    """
    if isinstance(value, str):
        return value.lower() in ["true", "1", "yes", "y", "on"]
    else:
        return bool(value)

def convert_2_dict(value):
    """
    Converts a value to a dictionary.

    Args:
        value (any): The value to convert.

    Returns:
        dict: The dictionary representation of the value.
    """
    if isinstance(value, dict):
        return value
    elif isinstance(value, (list, tuple)):
        try:
            return dict(value)
        except (ValueError, TypeError):
            return {}
    else:
        return {}

def convert_2_float(value):
    """
    Converts a value to a float.

    Args:
        value (any): The value to convert.

    Returns:
        float: The float representation of the value.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def convert_2_integer(value):
    """
    Converts a value to an integer.

    Args:
        value (any): The value to convert.

    Returns:
        int: The integer representation of the value.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def convert_2_list(value, delimiter=","):
    """
    Converts a value to a list.

    Args:
        value (any): The value to convert.
        delimiter (str, optional): The delimiter to use if the value is a string. Defaults to ','.

    Returns:
        list: The list representation of the value.
    """
    if isinstance(value, str):
        return value.split(delimiter)
    elif isinstance(value, (list, tuple)):
        return list(value)
    else:
        return [value]

def convert_2_string(value):
    """
    Converts a value to a string.

    Args:
        value (any): The value to convert.

    Returns:
        str: The string representation of the value.
    """
    return str(value)

def dec(val):
    if val is None:
        val = Decimal(0)
    else:
        val = Decimal(str(val))
    return val

def dec_2_float(in_data):
    func_name = "dec_2_float"
    """
    Cycles Through Dict Keys And Converts decimal.Decimal to float
    """
    try:
        if isinstance(in_data, Decimal):
            return float(in_data)
        elif isinstance(in_data, list):
            return [dec_2_float(item) for item in in_data]
        elif isinstance(in_data, dict):
            return {key: dec_2_float(value) for key, value in in_data.items()}
        else:
            return in_data
    except Exception as e:
        print("{} ==> errored... {}".format(func_name, e))
        traceback.print_exc()
        traceback.print_stack()
        print(type(e))
        print(e)
        print("in_data : ({})".format(type(in_data)))
        pprint(in_data)
        sys.exit()

def dec_prec(number, prec=28):
    with decimal.localcontext() as ctx:
        ctx.prec = prec
        d = decimal.Decimal(number)
        pprint(d)
        return d

def dict_2_obj(in_dict, i=0):
    out_obj = EmptyObject()
    for k in in_dict:
        v = in_dict[k]
        print("{} => k : {}, v : ({}) {}".format("    " * i, k, type(v), v))
        if isinstance(v, dict):
            i += 1
            v = dict_2_obj(v)
        setattr(out_obj, k, v)
    return out_obj

def int_2_tf(val):
    if val == 1:
        val = True
    else:
        val = 0
    return val

def tf(val):
    if val == 1:
        tf = True
    else:
        tf = False
    return tf

def tf_2_int(val):
    if val:
        val = int(1)
    else:
        val = int(0)
    return val

def to_int(val: Any, default: int = 0) -> int:
    """Convert value to integer with fallback default."""
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

def to_float(val: Any, default: float = 0.0) -> float:
    """Convert value to float with fallback default."""
    try:
        return float(val)
    except (ValueError, TypeError):
        return default

def to_str(val: Any) -> str:
    """Convert value to string."""
    return str(val)
