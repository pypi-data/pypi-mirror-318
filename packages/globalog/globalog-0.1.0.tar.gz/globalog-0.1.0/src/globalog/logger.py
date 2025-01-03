import logging
import logging.config
from enum import Enum
from typing import Optional, Type
from .config import load_config
from .exceptions import ConfigurationError


class LoggerLevel(Enum):
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG

    def __int__(self) -> int:
        return self.value


class GlobalLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GlobalLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = False
            self._logger: Optional[logging.Logger] = None
            self._auto_init()

    def _auto_init(self):
        """Automatically initialize logger with found configuration."""
        try:
            config = load_config()
            logging.config.dictConfig(config)
            self._logger = logging.getLogger()
            self._initialized = True
        except Exception as e:
            raise ConfigurationError(f"Error during auto-initialization: {str(e)}")

    def init(self, logger_name: str = 'default_logger',
             level: LoggerLevel = LoggerLevel.INFO,
             config_file: Optional[str] = None):
        """Explicitly initialize logger with custom configuration."""
        try:
            config = load_config(config_file) if config_file else None
            if config:
                logging.config.dictConfig(config)
                self._logger = logging.getLogger(logger_name)
            else:
                logging.basicConfig(
                    level=level.value,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s'
                )
                self._logger = logging.getLogger(logger_name)
                self._logger.setLevel(level.value)

            self._initialized = True
        except Exception as e:
            raise ConfigurationError(f"Error during initialization: {str(e)}")

    def _get_logger(self) -> logging.Logger:
        if not self._initialized:
            self._auto_init()
        return self._logger

    def debug(self, msg: str, *args, **kwargs):
        self._get_logger().debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        self._get_logger().info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self._get_logger().warning(msg, *args, **kwargs)

    def error(self, msg: str, exc_info: bool = False, *args, **kwargs):
        self._get_logger().error(msg, exc_info=exc_info, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs):
        self._get_logger().critical(msg, *args, **kwargs)

    def log(self, level: int | LoggerLevel, msg: str, *args, exc_info: bool = False, **kwargs):
        log_level = int(level)
        self._get_logger().log(log_level, msg, *args, exc_info=exc_info, **kwargs)

    @staticmethod
    def levels() -> Type[LoggerLevel]:
        return LoggerLevel


LOG = GlobalLogger()
