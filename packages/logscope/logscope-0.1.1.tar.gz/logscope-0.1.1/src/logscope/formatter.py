"""Custom formatters for Logscope."""

import logging
import textwrap
from logscope.utils import get_calling_details, format_timestamp_with_microseconds

class LogscopeFormatter(logging.Formatter):
    """Formatter that creates detailed, optionally colored log output."""

    COLOR_MAP = {
        'white': "\033[37m",
        'yellow': "\033[33m",
        'cyan': "\033[36m",
        'faded_gray': "\033[90m",
    }

    def __init__(self, style='colorful'):
        super().__init__()
        self.style = style

    def color(self, name: str, text: str) -> str:
        """Apply ANSI color to text if style is 'colorful'."""
        if self.style != 'colorful':
            return text
        start_color = self.COLOR_MAP[name]
        reset = "\033[0m"
        return f"{start_color}{text}{reset}"

    def format(self, record: logging.LogRecord) -> str:
        source, function = get_calling_details(record)
        timestamp = format_timestamp_with_microseconds(record)
        message = record.getMessage()
        filename = record.pathname
        lineno = record.lineno

        timestamp_colored = self.color('white', timestamp + ">")
        message_colored = self.color('yellow', message)
        filename_colored = self.color('faded_gray', filename)
        lineno_colored = self.color('faded_gray', str(lineno))
        function_colored = self.color('cyan', function)
        calling_expression = self.color('cyan', source)

        return textwrap.dedent(f"""
            {timestamp_colored} {message_colored}
              ⋅ {function_colored}:{calling_expression}
              ⋅ {filename_colored}:{lineno_colored}
        """).strip() + "\n"