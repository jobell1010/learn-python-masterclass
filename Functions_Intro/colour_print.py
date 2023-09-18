import colorama

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour etc

    :param text: The text to print
    :param effects: The effect we want, from the constants
        defined at the start of this module.
    """
    effect_string = "".join(effects)
    output_string="{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red in bold", RED, BOLD)
print("This should be the default colour")
colour_print("Hello, blue", BLUE)
colour_print("Hello, blue reversed", BLUE, REVERSE)
colour_print("Hello, blue reversed and underlined", BLUE, REVERSE, UNDERLINE)
colour_print("Hello, yellow", YELLOW)
colour_print("Hello, yellow in bold", YELLOW, BOLD)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, reverse", REVERSE)
colorama.deinit()
