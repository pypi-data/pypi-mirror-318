"""
fstrent_tools - A comprehensive collection of Python utility functions.
"""

__version__ = "0.3.3"

# Import all tools modules
from .tools_convert import *
from .tools_debug import *
from .tools_decorators import *
from .tools_dicts import *
from .tools_errors import *
from .tools_eval import *
from .tools_files import *
from .tools_formatting import *
from .tools_hyperlinks import *
from .tools_json import *
from .tools_logging import *
from .tools_object import *
from .tools_print import *
from .tools_python import *
from .tools_settings import *
from .tools_sounds import *
from .tools_speak import *
from .tools_strings import *
from .tools_terminal import *
from .tools_time import *
from .tools_video import *
from .tools_voice import *

# Dynamically generate __all__
import os
import importlib

__all__ = []

# Get the directory of the current file
package_dir = os.path.dirname(os.path.abspath(__file__))

# List of all tool modules
tool_modules = [
    'tools_convert',
    'tools_debug',
    'tools_decorators',
    'tools_dicts',
    'tools_errors',
    'tools_eval',
    'tools_files',
    'tools_formatting',
    'tools_hyperlinks',
    'tools_json',
    'tools_logging',
    'tools_object',
    'tools_print',
    'tools_python',
    'tools_settings',
    'tools_sounds',
    'tools_speak',
    'tools_strings',
    'tools_terminal',
    'tools_time',
    'tools_video',
    'tools_voice'
]

# Import each module and extend __all__
for module_name in tool_modules:
    try:
        module = importlib.import_module(f".{module_name}", package=__name__)
        if hasattr(module, "__all__"):
            __all__.extend(module.__all__)
    except ImportError as e:
        print(f"Warning: Could not import {module_name}: {e}")
