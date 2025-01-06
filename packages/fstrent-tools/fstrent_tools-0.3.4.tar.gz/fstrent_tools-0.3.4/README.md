# FSTrent Tools

A collection of utility functions commonly used in Python scripts and projects, organized into specialized modules.

## Installation

```bash
pip install fstrent_tools
```

## Modules

The package includes several specialized utility modules:

- **tools_convert**: Utilities for data type conversion and transformation
- **tools_debug**: Debugging helpers and troubleshooting utilities
- **tools_decorators**: Collection of useful Python decorators
- **tools_dicts**: Dictionary manipulation and advanced operations
- **tools_errors**: Custom error handling and exception utilities
- **tools_eval**: Safe evaluation and expression parsing utilities
- **tools_files**: File system operations and path management
- **tools_formatting**: Text and data formatting utilities
- **tools_hyperlinks**: URL and hyperlink manipulation tools
- **tools_json**: JSON handling, parsing, and manipulation utilities
- **tools_logging**: Advanced logging setup and management
- **tools_object**: Object manipulation and introspection utilities
- **tools_print**: Enhanced console printing and output formatting
- **tools_python**: Python language helpers and utility functions
- **tools_settings**: Configuration and settings management
- **tools_sounds**: Audio file handling and sound processing
- **tools_speak**: Text-to-speech and voice synthesis utilities
- **tools_strings**: String manipulation and processing functions
- **tools_terminal**: Terminal/console interaction utilities
- **tools_time**: Date, time, and duration handling utilities
- **tools_video**: Video file processing and manipulation
- **tools_voice**: Voice recognition and processing utilities

## Usage Examples

```python
# Import specific tools
from fstrent_tools.tools_logging import setup_logger
from fstrent_tools.tools_json import load_json, save_json
from fstrent_tools.tools_time import get_timestamp
from fstrent_tools.tools_formatting import format_number
from fstrent_tools.tools_object import AttDict

# Setup logging
logger = setup_logger("my_app")

# JSON operations
data = load_json("config.json")
save_json("output.json", data)

# Time operations
current_time = get_timestamp()

# Formatting
formatted_num = format_number(1234567.89)

# Using AttDict for attribute-style dictionary access
config = AttDict({
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'api_key': 'secret123'
})

# Access nested values using dot notation
print(config.database.host)  # outputs: localhost
print(config.api_key)        # outputs: secret123

# Still works like a regular dictionary
print(config['database']['port'])  # outputs: 5432

# Modify values using either notation
config.database.name = 'newdb'
config['api_key'] = 'newsecret'
```

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies: `pip install -r requirements.txt`
3. Make your changes
4. Submit a pull request

## Version Control

This project uses `bumpversion` for version management. To bump the version:

```bash
# For patch updates (0.0.x)
.\gh_push.bat
# Enter 'patch' when prompted

# For minor updates (0.x.0)
.\gh_push.bat
# Enter 'minor' when prompted

# For major updates (x.0.0)
.\gh_push.bat
# Enter 'major' when prompted
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.