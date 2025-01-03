# Globalog

A Python package providing a global logger with automatic configuration loading.

## Installation

```bash
pip install globalog
```

## Usage

```python
from globalog import LOG

# The logger will automatically load configuration from the nearest config file
LOG.info("This is an info message")
LOG.debug("This is a debug message")

# You can also explicitly initialize with a specific config file
LOG.init(config_file="path/to/config.json")
```

## Configuration

The package looks for configuration files in the following order:
1. `logging_config.json` in the current directory
2. `logging_config.yaml` in the current directory
3. Default configuration if no config file is found

Example configuration file (logging_config.json):
```json
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": true
        }
    }
}
```
