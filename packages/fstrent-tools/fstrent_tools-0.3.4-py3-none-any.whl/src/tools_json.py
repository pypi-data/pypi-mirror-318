import json
import decimal
from tools_files import dir_val

__all__ = [
    'format_json',
    'merge_json',
    'read_json',
    'search_json',
    'validate_json',
    'write_json',
    'json_safe',
    'json_file_read',
    'json_file_write'
]

def format_json(data, indent=4):
    """
    Formats a JSON string with indentation.

    Args:
        data (str): The JSON string to format.
        indent (int, optional): The number of spaces to use for indentation. Defaults to 4.

    Returns:
        str: The formatted JSON string.
    """
    try:
        parsed_json = json.loads(data)
        return json.dumps(parsed_json, indent=indent)
    except json.JSONDecodeError:
        return data

def merge_json(json1, json2):
    """
    Merges two JSON objects.

    Args:
        json1 (dict): The first JSON object.
        json2 (dict): The second JSON object.

    Returns:
        dict: The merged JSON object.
    """
    merged_json = json1.copy()
    merged_json.update(json2)
    return merged_json

def read_json(file_path):
    """
    Reads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data read from the JSON file, or an empty dictionary if the file does not exist or is invalid.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def search_json(data, key):
    """
    Searches for a key in a JSON object.

    Args:
        data (dict): The JSON object to search.
        key (str): The key to search for.

    Returns:
        any: The value associated with the key, or None if the key is not found.
    """
    if isinstance(data, dict):
        if key in data:
            return data[key]
        for value in data.values():
            result = search_json(value, key)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = search_json(item, key)
            if result is not None:
                return result
    return None

def validate_json(data):
    """
    Validates if the given data is a valid JSON string.

    Args:
        data (str): The data to validate.

    Returns:
        bool: True if the data is a valid JSON string, False otherwise.
    """
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False

def write_json(data, file_path):
    """
    Writes data to a JSON file.

    Args:
        data (dict): The data to write.
        file_path (str): The path to the JSON file.
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def json_safe(in_data, depth=0):
    """
    Convert data to JSON-safe format, handling Decimal types.
    
    Args:
        in_data: Data to convert
        depth (int): Current recursion depth
    
    Returns:
        JSON-safe data
    """
    depth += 1
    out_data = in_data

    if isinstance(in_data, list):
        for x in in_data:
            x = json_safe(x, depth)
    elif isinstance(in_data, dict):
        for x in in_data:
            in_data[x] = json_safe(in_data[x], depth)
    elif isinstance(in_data, decimal.Decimal):
        out_data = float(in_data)
    else:
        out_data = in_data

    return out_data

def json_file_read(directory_string, default_json_content=None):
    """
    Get the contents of a JSON file. If it doesn't exist,
    create and populate it with specified or default JSON content.
    
    Args:
        directory_string (str): The relative directory string (ex: settings/secrets.json)
        default_json_content (dict, optional): Default content if file doesn't exist
    
    Returns:
        dict: The JSON file contents
    """
    dir_val(directory_string)
    try:
        with open(directory_string) as file:
            file_content = json.load(file)
            return file_content
    except (IOError, json.decoder.JSONDecodeError):
        with open(directory_string, "w") as file:
            if default_json_content is None:
                default_json_content = {}
            json.dump(default_json_content, file, indent=4)
            return default_json_content

def json_file_write(directory_string, json_content):
    """
    Write content to a JSON file.
    
    Args:
        directory_string (str): The relative directory string (ex: settings/secrets.json)
        json_content (dict): The content to write to the file
    """
    dir_val(directory_string)
    with open(directory_string, "w") as file:
        json.dump(json_content, file, indent=4)
