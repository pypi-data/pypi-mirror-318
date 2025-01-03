import os
import json
import yaml
from typing import Dict, Any, Optional
from .exceptions import ConfigurationError


def find_config_file() -> Optional[str]:
    """Find the nearest configuration file."""
    config_files = ['logging_config.json', 'logging_config.yaml']

    for config_file in config_files:
        if os.path.exists(config_file):
            return config_file

    return None


def load_config(config_file: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration from file or return default configuration."""
    if config_file is None:
        config_file = find_config_file()

    if config_file is None:
        return get_default_config()

    try:
        with open(config_file, 'r') as f:
            if config_file.endswith('.json'):
                return json.load(f)
            elif config_file.endswith('.yaml'):
                return yaml.safe_load(f)
    except Exception as e:
        raise ConfigurationError(f"Error loading configuration file: {str(e)}")

    return get_default_config()


def get_default_config() -> Dict[str, Any]:
    """Return default logging configuration."""
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s"
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
                "propagate": True
            }
        }
    }