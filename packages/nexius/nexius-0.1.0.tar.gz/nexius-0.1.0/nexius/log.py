"""
Nexius Logging Module
Provides colored logging with custom formatting
"""

from datetime import datetime
from typing import Optional, Union, TextIO
import sys
import colorama
colorama.init(autoreset=True)

class Colors:
    """ANSI color codes"""
    c_SECO: str = colorama.Fore.LIGHTBLACK_EX
    GRAY = colorama.Fore.LIGHTBLACK_EX
    GREEN = colorama.Fore.GREEN
    YELLOW = colorama.Fore.YELLOW
    RED = colorama.Fore.RED
    BLUE = colorama.Fore.BLUE
    MAGENTA = colorama.Fore.MAGENTA
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE
    RESET = colorama.Fore.RESET
    
    # Custom darker colors
    DARK_RED = '\033[38;5;160m'    # Intense, bright red
    DARK_ORANGE = '\033[38;5;172m'  # More yellow-orange

    @staticmethod
    def secondary(text: str, main_color: str = RESET) -> str:
        """
        Wrap text with secondary color
        
        Args:
            text (str): Text to wrap
            main_color (str, optional): Main color to reset to. Defaults to RESET.
        
        Returns:
            str: Colored text
        """
        return f"{Colors.c_SECO}{text}{main_color}"

class NexiusLogger:
    """
    A colored logger for the Nexius library
    """
    
    def __init__(self, output: Optional[Union[str, TextIO]] = None):
        """
        Initialize the Nexius logger
        
        Args:
            output (Optional[Union[str, TextIO]]): Output file path or file-like object
        """
        self.output_file = None
        if output:
            if isinstance(output, str):
                self.output_file = open(output, 'a')
            else:
                self.output_file = output

    @staticmethod
    def _format_log_message(level: str, color: str, message: str) -> str:
        """
        Static method to format log messages with timestamp and color
        
        Args:
            level (str): Log level (e.g., 'ERROR', 'INFO')
            color (str): Color to use for the log level
            message (str): Log message
        
        Returns:
            str: Formatted log message
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        return f"{Colors.c_SECO}[{timestamp}] {color}{level}{Colors.RESET}: {message}"

    def _apply_replacements(self, message: str) -> str:
        """
        Apply special replacements to log messages
        
        Args:
            message (str): Original log message
        
        Returns:
            str: Processed log message with special replacements
        """
        # Wrap square brackets
        message = message.replace(
            "[", 
            f'{Colors.c_SECO}[{Colors.RESET}'
        ).replace(
            "]", 
            f'{Colors.c_SECO}]{Colors.RESET}'
        )
        
        replacements = {
            "|": f"{Colors.c_SECO}|{Colors.RESET}",
            "->": f"{Colors.c_SECO}->{Colors.RESET}",
            "(+)": f"{Colors.c_SECO}({Colors.GREEN}+{Colors.c_SECO}){Colors.RESET}",
            "($)": f"{Colors.c_SECO}({Colors.GREEN}${Colors.c_SECO}){Colors.RESET}",
            "(-)": f"{Colors.c_SECO}({Colors.RED}-{Colors.c_SECO}){Colors.RESET}",
            "(!)": f"{Colors.c_SECO}({Colors.RED}!{Colors.c_SECO}){Colors.RESET}",
            "(~)": f"{Colors.c_SECO}({Colors.YELLOW}~{Colors.c_SECO}){Colors.RESET}",
            "(#)": f"{Colors.c_SECO}({Colors.BLUE}#{Colors.c_SECO}){Colors.RESET}",
            "(*)": f"{Colors.c_SECO}({Colors.CYAN}*{Colors.c_SECO}){Colors.RESET}",
        }
        
        # Remove extra whitespace before applying replacements
        message = message.replace("(~ )", "(~)")
        
        for find, replace in replacements.items():
            message = message.replace(find, replace)
        
        return message

    def _log(self, level: str, color: str, message: str) -> None:
        """Internal logging method"""
        # Apply replacements to the message
        message = self._apply_replacements(message)
        
        formatted_message = self._format_log_message(level, color, message)
        
        # Print to console
        print(formatted_message)
        
        # Write to file if specified (without color codes)
        if self.output_file:
            plain_message = f"[{datetime.now().strftime('%H:%M:%S')}] {level}: {message}\n"
            self.output_file.write(plain_message)
            self.output_file.flush()

    def success(self, message: str) -> None:
        """Log success message"""
        self._log("SUC", Colors.GREEN, message)

    def error(self, message: str) -> None:
        """Log error message"""
        self._log("ERR", Colors.DARK_RED, message)

    def warning(self, message: str) -> None:
        """Log warning message"""
        self._log("WAR", Colors.DARK_ORANGE, message)

    def fatal(self, message: str) -> None:
        """Log fatal message"""
        self._log("FTL", Colors.RED, message)

    def debug(self, message: str) -> None:
        """Log debug message"""
        self._log("DBG", Colors.YELLOW, message)

    def info(self, message: str) -> None:
        """Log info message"""
        self._log("INF", Colors.MAGENTA, message)

    def __del__(self):
        """Cleanup file handler if needed"""
        if self.output_file and not self.output_file.closed:
            self.output_file.close()

    @staticmethod
    def __call__(message: str, level: str = "INF", color: str = Colors.GREEN) -> None:
        """
        Allow direct calling of the logger instance
        
        Args:
            message (str): The log message
            level (str, optional): Log level. Defaults to "INF".
            color (str, optional): Color for the log level. Defaults to green.
        """
        log._log(level, color, message)

# Create default logger instance
log = NexiusLogger() 

def success(message):
    message = log._apply_replacements(message)
    print(log._format_log_message("SUC", Colors.GREEN, message))

def error(message):
    message = log._apply_replacements(message)
    print(log._format_log_message("ERR", Colors.DARK_RED, message))

def warning(message):
    message = log._apply_replacements(message)
    print(log._format_log_message("WAR", Colors.DARK_ORANGE, message))

def fatal(message):
    message = log._apply_replacements(message)
    print(log._format_log_message("FTL", Colors.RED, message))

def debug(message):
    message = log._apply_replacements(message)
    print(log._format_log_message("DBG", Colors.YELLOW, message))

def info(message):
    message = log._apply_replacements(message)
    print(log._format_log_message("INF", Colors.MAGENTA, message))

def printf(*args, **kwargs):
    """
    Print function that shows only message and timestamp with replacements
    
    Args:
        *args: Arguments to print
        **kwargs: Additional keyword arguments
    """
    message = ' '.join(str(arg) for arg in args)
    
    # Apply replacements
    replacements = {
        "|": f"{Colors.c_SECO}|{Colors.RESET}",
        "->": f"{Colors.c_SECO}->{Colors.RESET}",
        "(+)": f"{Colors.c_SECO}({Colors.GREEN}+{Colors.c_SECO}){Colors.RESET}",
        "($)": f"{Colors.c_SECO}({Colors.GREEN}${Colors.c_SECO}){Colors.RESET}",
        "(-)": f"{Colors.c_SECO}({Colors.RED}-{Colors.c_SECO}){Colors.RESET}",
        "(!)": f"{Colors.c_SECO}({Colors.RED}!{Colors.c_SECO}){Colors.RESET}",
        "(~)": f"{Colors.c_SECO}({Colors.YELLOW}~{Colors.c_SECO}){Colors.RESET}",
        "(#)": f"{Colors.c_SECO}({Colors.BLUE}#{Colors.c_SECO}){Colors.RESET}",
        "(*)": f"{Colors.c_SECO}({Colors.CYAN}*{Colors.c_SECO}){Colors.RESET}",
    }
    
    # Apply bracket replacements
    message = message.replace(
        "[", 
        f'{Colors.c_SECO}[{Colors.RESET}'
    ).replace(
        "]", 
        f'{Colors.c_SECO}]{Colors.RESET}'
    )
    
    for find, replace in replacements.items():
        message = message.replace(find, replace)
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{Colors.c_SECO}[{timestamp}]{Colors.RESET} {message}")