import json

__all__ = [
    'DEFAULT_SETTINGS_PATH',
    'get_setting',
    'load_settings',
    'reset_settings',
    'save_settings',
    'set_setting',
    'update_settings'
]

DEFAULT_SETTINGS_PATH = "settings.json"

def get_setting(key, default=None, file_path=DEFAULT_SETTINGS_PATH):
    """
    Retrieves a specific setting.

    Args:
        key (str): The key of the setting to retrieve.
        default (any, optional): The default value to return if the key is not found. Defaults to None.
        file_path (str, optional): The path to the settings file. Defaults to 'settings.json'.

    Returns:
        any: The value of the setting, or the default value if the key is not found.
    """
    settings = load_settings(file_path)
    return settings.get(key, default)

def load_settings(file_path=DEFAULT_SETTINGS_PATH):
    """
    Loads settings from a JSON file.

    Args:
        file_path (str, optional): The path to the settings file. Defaults to 'settings.json'.

    Returns:
        dict: The loaded settings, or an empty dictionary if the file does not exist or is invalid.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def reset_settings(file_path=DEFAULT_SETTINGS_PATH):
    """
    Resets the settings file to an empty dictionary.

    Args:
        file_path (str, optional): The path to the settings file. Defaults to 'settings.json'.
    """
    save_settings({}, file_path)

def save_settings(settings, file_path=DEFAULT_SETTINGS_PATH):
    """
    Saves settings to a JSON file.

    Args:
        settings (dict): The settings to save.
        file_path (str, optional): The path to the settings file. Defaults to 'settings.json'.
    """
    with open(file_path, "w") as f:
        json.dump(settings, f, indent=4)

def set_setting(key, value, file_path=DEFAULT_SETTINGS_PATH):
    """
    Sets a specific setting.

    Args:
        key (str): The key of the setting to set.
        value (any): The value to set.
        file_path (str, optional): The path to the settings file. Defaults to 'settings.json'.
    """
    settings = load_settings(file_path)
    settings[key] = value
    save_settings(settings, file_path)

def update_settings(new_settings, file_path=DEFAULT_SETTINGS_PATH):
    """
    Updates existing settings with new values.

    Args:
        new_settings (dict): The new settings to merge.
        file_path (str, optional): The path to the settings file. Defaults to 'settings.json'.
    """
    settings = load_settings(file_path)
    settings.update(new_settings)
    save_settings(settings, file_path)
