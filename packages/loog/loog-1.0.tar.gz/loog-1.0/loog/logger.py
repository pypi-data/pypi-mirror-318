import inspect
import warnings
from contextlib import contextmanager
from datetime import datetime
from typing import Optional, TextIO

from .text_color import TextColor


class Logger:
    """Main logger class that handles all logging functionality."""

    log_levels = {
        "debug": 0,
        "info": 1,
        "warning": 2,
        "error": 3,
        "critical": 4,
    }

    color_map = {
        "warning": TextColor.yellow,
        "error": TextColor.orange,
        "critical": TextColor.red,
    }

    display_level = "info"
    do_log = True
    do_log_to_file = False
    _default_log_file_name = "%Y-%m-%d_%H-%M-%S.log"
    log_file_name = datetime.now().strftime(_default_log_file_name)
    _log_file: Optional[TextIO] = None

    @staticmethod
    def _get_caller_info() -> str:
        """Gets information about the caller of the logging function."""
        stack = inspect.stack()
        current_frame = stack[2]  # The caller's frame

        current_function_name = current_frame.function
        current_file_name = current_frame.filename
        current_lineno = current_frame.lineno

        return f'File "{current_file_name}", line {current_lineno}, in {current_function_name}'

    @classmethod
    def _get_color_for_level(cls, level: str) -> str:
        """Gets the appropriate color for a logging level.

        Args:
            level: The logging level to get the color for.

        Returns:
            str: The color for the logging level.
        """
        return cls.color_map.get(level, "")

    @classmethod
    def _set_log_file_name(cls, log_file_name: Optional[str] = None) -> None:
        """Sets the name of the log file.

        Args:
            log_file_name: The name of the log file to set.
        """
        if log_file_name is not None:
            cls.log_file_name = log_file_name

    @classmethod
    @contextmanager
    def _log_file_context(cls):
        """Context manager for handling log file operations."""
        if cls.do_log_to_file:
            file = open(cls.log_file_name, "a")
            try:
                yield file
            finally:
                file.close()
        else:
            yield None

    @classmethod
    def _write_log(cls, file: Optional[TextIO], *messages: str) -> None:
        """Writes messages to the log file if file logging is enabled."""
        if file:
            for message in messages:
                file.write(f"{message}\n")

    @classmethod
    def _check_loglevel_is_valid(cls, logging_level: str) -> None:
        """Checks if a logging level is valid.

        Args:
            logging_level: The logging level to check.

        Raises:
            ValueError: If the logging level is not valid.
        """
        if logging_level.lower() not in cls.log_levels:
            raise ValueError(
                f"Invalid logging level: {logging_level}, must be one of: {list(cls.log_levels.keys())}"
            )

    @classmethod
    def __call__(cls, msg: str, logging_level: str = "info") -> None:
        """Logs a message with the specified logging level.

        Args:
            msg: The message to log.
            logging_level: The severity level of the log message (default: info).

        Raises:
            ValueError: If the logging level is not a valid logging level.
        """
        logging_level = logging_level.lower()

        if logging_level not in cls.log_levels:
            raise ValueError(
                f"Invalid logging level: {logging_level}, must be one of: {list(cls.log_levels.keys())}"
            )

        if (
            not cls.do_log
            or cls.log_levels[logging_level] < cls.log_levels[cls.display_level]
        ):
            return

        time_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        caller_info = cls._get_caller_info()

        color = cls._get_color_for_level(logging_level)
        if color:
            print(color, end="", flush=True)

        with cls._log_file_context() as log_file:
            header = f"{time_string} | {caller_info}"
            detail = f"{logging_level.upper():>23} | {msg}"
            print(header)
            print(detail)
            cls._write_log(log_file, header, detail)

        if color:
            print(TextColor.reset, end="", flush=True)

    @classmethod
    def set_display_level(cls, display_level: str) -> None:
        """Sets the minimum logging level to display (default: info).

        Args:
            display_level: The minimum logging level to display.
        """
        cls._check_loglevel_is_valid(display_level)

        cls.display_level = display_level.lower()

    @classmethod
    def log_on(cls) -> None:
        """Enables logging."""
        cls.do_log = True

    @classmethod
    def log_off(cls) -> None:
        """Disables logging."""
        cls.do_log = False

    @classmethod
    def log_to_file(cls, log_file_name: Optional[str] = None) -> None:
        """Enables logging to a file.

        Args:
            log_file_name: The name of the log file to write to.
        """
        cls._set_log_file_name(log_file_name)
        cls.do_log_to_file = True

    @classmethod
    def set_loglevel_color(cls, logging_level: str, color: str) -> None:
        """Sets the color for a log level.

        Args:
            logging_level: The log level to set the color for.
            color: The color to set for the log level.

        Raises:
            ValueError: If the color is not a valid color name or hex code.
        """
        cls._check_loglevel_is_valid(logging_level)

        # If it's a hex color code
        if color.startswith("#"):
            # Validate hex format
            if len(color) != 7 or not all(
                c in "0123456789ABCDEFabcdef" for c in color[1:]
            ):
                raise ValueError("Invalid hex color code. Must be in format '#RRGGBB'")

            # Convert hex to ANSI escape code
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            ansi_color = f"\u001b[38;2;{r};{g};{b}m"
            cls.color_map[logging_level] = ansi_color
            return

        # If it's a TextColor name
        color_name = color.lower()
        if hasattr(TextColor, color_name):
            cls.color_map[logging_level] = getattr(TextColor, color_name)
        else:
            valid_colors = [
                attr
                for attr in dir(TextColor)
                if not attr.startswith("_") and attr != "reset"
            ]
            raise ValueError(
                f"Invalid color name. Must be a hex color code or one of: {', '.join(valid_colors)}"
            )

    @classmethod
    def create_custom_loglevel(cls, name: str, color: str = None) -> None:
        """Creates a custom log level with highest priority.

        Args:
            name: The name of the custom log level.
            color: The color of the custom log level.
        """
        try:
            cls._check_loglevel_is_valid(name)
            warnings.warn(f'Log level "{name}" already exists. Ignoring creation.')
            return
        except ValueError:
            pass

        cls.log_levels[name.lower()] = len(cls.log_levels)

        if color:
            cls.set_loglevel_color(name.lower(), color)


log = Logger()
