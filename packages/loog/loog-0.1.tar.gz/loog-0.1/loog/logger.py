import inspect
from contextlib import contextmanager
from datetime import datetime
from typing import Optional, TextIO

from .log_level import LogLevel
from .text_color import TextColor


class Logger:
    """Main logger class that handles all logging functionality.

    Class Attributes:
        display_level: The minimum log level to display.
        do_log: Whether logging is enabled.
        do_log_to_file: Whether file logging is enabled.
        log_file_name: Name of the log file.
        _log_file: File handle for logging.
        _default_log_file_name: Default log file name pattern.
    """

    display_level = LogLevel.INFO
    do_log = True
    do_log_to_file = False
    _default_log_file_name = "%Y-%m-%d_%H-%M-%S.log"
    log_file_name = datetime.now().strftime(_default_log_file_name)
    _log_file: Optional[TextIO] = None

    color_map = {
        LogLevel.WARNING: TextColor.yellow,
        LogLevel.ERROR: TextColor.orange,
        LogLevel.CRITICAL: TextColor.red,
    }

    @staticmethod
    def _get_caller_info() -> str:
        """Gets information about the caller of the logging function.

        Returns:
            str: A string containing the caller's function name, file name, line number, and arguments.
        """
        stack = inspect.stack()
        current_frame = stack[3]  # The caller's frame

        current_function_name = current_frame.function
        current_file_name = current_frame.filename
        current_lineno = current_frame.lineno

        # return f"{current_function_name} @ {current_file_name}:{current_lineno}"
        return f"File {current_file_name}, line {current_lineno}, in {current_function_name}"

    @classmethod
    @contextmanager
    def _log_file_context(cls):
        """Context manager for handling log file operations.

        Yields:
            Optional[TextIO]: A file handle if file logging is enabled, None otherwise.
        """
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
        """Writes messages to the log file if file logging is enabled.

        Args:
            file: File handle to write to.
            *messages: Variable number of messages to write.
        """
        if file:
            for message in messages:
                file.write(f"{message}\n")

    @classmethod
    def log(cls, msg: str, logging_level: LogLevel) -> None:
        """Logs a message with the specified logging level.

        Args:
            msg: The message to log.
            logging_level: The severity level of the log message.
        """
        if not cls.do_log or logging_level.value < cls.display_level.value:
            return

        time_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        caller_info = cls._get_caller_info()
        log_level_str = logging_level.name

        color = cls._get_color_for_level(logging_level)
        if color:
            print(color, end="", flush=True)

        with cls._log_file_context() as log_file:
            header = f"{time_string} | {caller_info}"
            detail = f"{log_level_str:>23} | {msg}"
            print(header)
            print(detail)
            cls._write_log(log_file, header, detail)

        if color:
            print(TextColor.reset, end="", flush=True)

    @classmethod
    def _get_color_for_level(cls, level: LogLevel) -> str:
        """Gets the appropriate color for a logging level.

        Args:
            level: The logging level to get the color for.

        Returns:
            str: ANSI color code for the specified level.
        """
        return cls.color_map.get(level, "")

    @classmethod
    def set_display_level(cls, display_level: LogLevel) -> None:
        """Sets the minimum logging level to display.

        Args:
            display_level: The minimum level of logs to display.
        """
        cls.display_level = display_level

    @classmethod
    def log_on(cls) -> None:
        """Enables logging."""
        cls.do_log = True

    @classmethod
    def log_off(cls) -> None:
        """Disables logging."""
        cls.do_log = False

    @classmethod
    def _set_log_file_name(cls, log_file_name: Optional[str] = None) -> None:
        """Sets the name of the log file.

        Args:
            log_file_name: Name of the file to log to. If None, uses default name format
                          based on current timestamp (YYYY-MM-DD_HH-MM-SS.log).
        """
        if log_file_name is not None:
            cls.log_file_name = log_file_name

    @classmethod
    def log_to_file(cls, log_file_name: Optional[str] = None) -> None:
        """Enables logging to a file.

        Args:
            log_file_name: Optional name of the file to log to. If None, uses default name
                          format based on current timestamp (YYYY-MM-DD_HH-MM-SS.log).
        """
        cls._set_log_file_name(log_file_name)
        cls.do_log_to_file = True

    @classmethod
    def set_loglevel_color(cls, loglevel: LogLevel, color: str) -> None:
        """Sets the color for a log level.

        Args:
            loglevel: The log level to set the color for.
            color: The color to set for the log level. Can be either:
                  - A TextColor attribute name (e.g., 'green')
                  - A hex color code (e.g., '#FF0000')

        Raises:
            ValueError: If the color string is not a valid TextColor name or hex color code.
        """
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
            cls.color_map[loglevel] = ansi_color
            return

        # If it's a TextColor name
        color_name = color.lower()
        if hasattr(TextColor, color_name):
            cls.color_map[loglevel] = getattr(TextColor, color_name)
        else:
            valid_colors = [
                attr
                for attr in dir(TextColor)
                if not attr.startswith("_") and attr != "reset"
            ]
            raise ValueError(
                f"Invalid color name. Must be a hex color code or one of: {', '.join(valid_colors)}"
            )


# Convenience functions
def log(msg: str, logging_level: LogLevel) -> None:
    """Logs a message with the specified logging level.

    Args:
        msg: The message to log.
        logging_level: The severity level of the log message.
    """
    Logger.log(msg, logging_level)


def set_display_level(display_level: LogLevel) -> None:
    """Sets the minimum logging level to display (default: INFO).

    Args:
        display_level: The minimum level of logs to display.
    """
    Logger.set_display_level(display_level)


def log_on() -> None:
    """Enables logging."""
    Logger.log_on()


def log_off() -> None:
    """Disables logging."""
    Logger.log_off()


def log_to_file(log_file_name: Optional[str] = None) -> None:
    """Enables logging to a file.

    Args:
        log_file_name: Optional name of the file to log to. If None, uses default name
                      format based on current timestamp (YYYY-MM-DD_HH-MM-SS.log).
    """
    Logger.log_to_file(log_file_name)


def set_loglevel_color(loglevel: LogLevel, color: str | TextColor) -> None:
    """Sets the color for a log level.

    Args:
        loglevel: The log level to set the color for.
        color: The color to set for the log level.
    """
    Logger.set_loglevel_color(loglevel, color)
