import errno
import fnmatch
import os
import shutil
import time
from pathlib import Path
from typing import Any, List, Optional, Union

__all__ = [
    'create_directory',
    'dir_val',
    'ensure_dir',
    'get_file_age_minutes',
    'is_valid_path',
    'file_copy',
    'file_delete',
    'file_list',
    'file_move',
    'file_read',
    'file_read_safe',
    'file_write',
    'file_write_safe'
    ]


def create_directory(directory_path):
    """
    Creates a directory if it doesn't exist.
    Args:
        directory_path (str): The path to the directory to create.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def dir_val(directory_string):
    """
    Check if a directory exists. If it doesn't, then create it.
    Args:
        directory_string (str): The relative directory string (ex: settings/secrets.json)
    """
    if not os.path.exists(os.path.dirname(directory_string)):
        try:
            os.makedirs(os.path.dirname(directory_string))
            print(f"Successfully created '{directory_string}' file directory")
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

def ensure_dir(directory: str) -> bool:
    """Ensure directory exists, create if it doesn't."""
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except OSError as e:
        if e.errno != errno.EEXIST:
            return False
        return True
def get_file_age_minutes(filepath: str) -> Optional[float]:
    """Get file age in minutes."""
    try:
        stats = os.stat(filepath)
        return (time.time() - stats.st_mtime) / 60
    except OSError:
        return None


def is_valid_path(path: str) -> bool:
    """Check if a path is valid."""
    try:
        if not path or not isinstance(path, str):
            return False
        
        # Check for invalid characters in Windows paths
        if os.name == 'nt':
            invalid_chars = '<>:"|?*'
            if any(char in path for char in invalid_chars):
                return False
            
            # Check for reserved names in Windows
            parts = path.split(os.path.sep)
            reserved_names = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4',
                            'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3',
                            'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'}
            if any(part.upper() in reserved_names for part in parts):
                return False
        
        # Try to create an absolute path
        abs_path = os.path.abspath(path)
        
        # Check if the path is too long
        if os.name == 'nt' and len(abs_path) > 260:
            return False
        
        return True
    except (TypeError, ValueError, AttributeError):
        return False

def is_valid_path(path: str) -> bool:
    """Check if a path is valid for the current OS."""
    try:
        if os.path.sep == '\\':  # Windows
            return '\\\\?\\' + os.path.abspath(path)
        return os.path.abspath(path)
    except:
        return False

def file_copy(src: Union[str, Path], dst: Union[str, Path]) -> bool:
    """Copy file from source to destination."""
    try:
        shutil.copy2(str(src), str(dst))
        return True
    except:
        return False

def file_delete(filepath: Union[str, Path]) -> bool:
    """Delete file if it exists."""
    try:
        if os.path.exists(str(filepath)):
            os.remove(str(filepath))
            return True
    except:
        pass
    return False

def file_list(directory: Union[str, Path], pattern: str = '*') -> List[str]:
    """List files in directory matching pattern."""
    try:
        return [f for f in os.listdir(str(directory)) 
                if os.path.isfile(os.path.join(str(directory), f))
                and fnmatch.fnmatch(f, pattern)]
    except:
        return []

def file_move(src: Union[str, Path], dst: Union[str, Path]) -> bool:
    """Move file from source to destination."""
    try:
        shutil.move(str(src), str(dst))
        return True
    except:
        return False

def file_read(file_path):
    """
    Reads the contents of a file.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file, or None if the file does not exist.
    """
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

def file_read_safe(filepath: str, default: Any = None) -> Optional[str]:
    """Safely read file content with error handling."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except IOError:
        return default


def file_write(file_path: str, content: str, mode: str = 'w', encoding: str = 'utf-8') -> bool:
    """Write content to a file."""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
        
        # Write content to file
        with open(file_path, mode=mode, encoding=encoding) as f:
            f.write(content)
            if not content.endswith('\n'):
                f.write('\n')
        return True
    except (IOError, OSError) as e:
        return False

def file_write_safe(filepath: str, content: str, mode: str = 'w') -> bool:
    """Safely write content to file with directory creation if needed."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, mode) as f:
            f.write(content)
        return True
    except IOError:
        return False

