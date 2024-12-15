# ux_enhancements.py
from colorama import Fore, Style, init
from art import text2art
from .input_validator import InputValidator

init(autoreset=True)

class TerminalToolkit:
    # Central color mapping as a class attribute
    COLOR_MAP = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        'yellow': Fore.YELLOW,
        'cyan': Fore.CYAN,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE
    }

    def __init__(self):
        """Initialize the TerminalToolkit class."""
        pass

    def get_color(self, color_name):
        """
        Fetch color from COLOR_MAP, defaults to white.
        
        Parameters:
            color_name (str): Name of the color.
            
        Returns:
            str: Color escape code.
        """
        return self.COLOR_MAP.get(color_name.lower(), Fore.WHITE)

    def draw_box(self, text, color='white'):
        """
        Draws a box around the given text.

        Parameters:
            text (str): The text to be boxed.
            color (str): Color of the box border.
        """
        chosen_color = self.get_color(color)
        text = str(text)
        line_length = len(text) + 4
        top_border = f"{chosen_color}{'+' + '-' * (line_length - 2) + '+'}{Style.RESET_ALL}"
        side_border = f"{chosen_color}| {text} |{Style.RESET_ALL}"

        print(top_border)
        print(side_border)
        print(top_border)

    def print_heading(self, text, imp=1, color='red', size=1.0, uppercase=None):
        """
        Prints a formatted heading with colored decorations based on importance level.
        
        Parameters:
            text (str): The text or value to be displayed.
            imp (int): Importance level from 1 (highest) to 6 (lowest).
            color (str): Color of the text and decorations (e.g., 'red', 'green', 'blue').
            size (float): Multiplier for text size (affects the number of decorations).
            uppercase (bool): If True, converts text to uppercase; if None, uses uppercase for imp=1 by default.
        """
        chosen_color = self.get_color(color)
        text = str(text)
        if uppercase or (uppercase is None and imp == 1):
            text = text.upper()

        if imp == 1:
            decoration = '=' * int(10 * size)
        elif imp == 2:
            decoration = '*' * int(7 * size)
        elif imp == 3:
            decoration = '-' * int(5 * size)
        elif imp == 4:
            decoration = '~' * int(3 * size)
        elif imp == 5:
            decoration = '~'
        else:
            decoration = ''

        formatted_text = f"{chosen_color}{decoration} {text} {decoration}{Style.RESET_ALL}"
        print(formatted_text)

    def gigantify(self, text, color='cyan'):
        """
        Enlarges the input text using ASCII art and applies color.

        Parameters:
            text (str): The text to be enlarged.
            color (str): The color of the ASCII art text (e.g., 'cyan', 'yellow', etc.).
        """
        chosen_color = self.get_color(color)
        ascii_art = text2art(text)
        print(f"{chosen_color}{ascii_art}{Style.RESET_ALL}")

    def menu(self, question, *options):
        """
        Displays a menu with a question and numbered options. Validates user input to ensure a choice within range.
        Raises an error if no options are provided.

        Parameters:
            question (str): The prompt or question to display at the top of the menu.
            *options (str): Variable number of menu options to display.

        Returns:
            int: The number corresponding to the user's selected option.
        """
        # Check if at least one option is provided
        if not options:
            raise ValueError("At least one option must be provided for the menu.")

        # Display the question using print_heading with importance level 1
        self.print_heading(question, imp=1)

        # Print each option with a number
        for idx, option in enumerate(options, start=1):
            print(f"{idx}) {option}")

        # Prompt for and return a valid selection
        choice = InputValidator.get_int_input(prompt="Choose an option: ", min_val=1, max_val=len(options))
        return choice

# Usage Example:
# toolkit = TerminalToolkit()
# toolkit.draw_box("Hello, World!", color="blue")
# toolkit.print_heading("Welcome!", imp=2, color="green")
# toolkit.gigantify("Big Text", color="cyan")
# choice = toolkit.menu("Select an option:", "Option 1", "Option 2", "Option 3")
