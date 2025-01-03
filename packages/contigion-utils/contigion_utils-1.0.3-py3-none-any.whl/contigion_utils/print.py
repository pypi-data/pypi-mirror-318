def colour_print(text, color):
    """Print text in the specified color."""
    color_codes = {
        'black': '\033[90m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
        'bold_red': '\033[1;91m',
        'bold_green': '\033[1;92m',
        'bold_yellow': '\033[1;93m',
        'bold_blue': '\033[1;94m',
        'bold_purple': '\033[1;95m',
        'bold_cyan': '\033[1;96m',
        'bold_white': '\033[1;97m',
    }

    color_code = color_codes.get(color.lower(), color_codes['reset'])
    print(f'{color_code}{text}{color_codes["reset"]}')


def print_info(text):
    """Print an info message in purple."""
    colour_print(text, 'purple')


def print_debug(text):
    """Print a notice message in blue."""
    colour_print(text, 'blue')


def print_warning(text):
    """Print a warning message in yellow."""
    colour_print(text, 'yellow')


def print_success(text):
    """Print a success message in green."""
    colour_print(text, 'green')


def print_error(text):
    """Print an error message in red."""
    colour_print(text, 'red')
