import re
import getpass
from util.password import Password

class InputValidator:
    """
    A utility class for validating user inputs and providing safe, guided prompts for collecting data.

    This class includes methods to validate various types of inputs (e.g., strings, integers, floats), 
    validate specific formats like email or phone numbers, and handle password inputs securely.
    """

    def __init__(self):
        """
        Initializes an instance of the InputValidator class. Currently, no instance-specific attributes are defined.
        """
        pass

    def is_valid_string(self, input_string, min_length=None, max_length=None):
        """
        Validates if a string meets the specified length constraints.

        Parameters:
        - input_string (str): The string to validate.
        - min_length (int, optional): Minimum allowable length of the string.
        - max_length (int, optional): Maximum allowable length of the string.

        Returns:
        - bool: True if the string meets the constraints, False otherwise.
        """
        if min_length is not None and len(input_string) < min_length:
            print(f"String must be at least {min_length} characters long.")
            return False
        if max_length is not None and len(input_string) > max_length:
            print(f"String must be no more than {max_length} characters long.")
            return False
        return True

    def is_valid_int(self, input_value, min_val=None, max_val=None):
        """
        Validates if a value is an integer within the specified range.

        Parameters:
        - input_value (str): The input to validate.
        - min_val (int, optional): Minimum allowable value.
        - max_val (int, optional): Maximum allowable value.

        Returns:
        - bool: True if the value is a valid integer and within range, False otherwise.
        """
        try:
            int_value = int(input_value)
            if min_val is not None and int_value < min_val:
                print(f"Value must be at least {min_val}.")
                return False
            if max_val is not None and int_value > max_val:
                print(f"Value must be no more than {max_val}.")
                return False
            return True
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return False

    def is_valid_float(self, input_value, min_val=None, max_val=None):
        """
        Validates if a value is a floating-point number within the specified range.

        Parameters:
        - input_value (str): The input to validate.
        - min_val (float, optional): Minimum allowable value.
        - max_val (float, optional): Maximum allowable value.

        Returns:
        - bool: True if the value is a valid float and within range, False otherwise.
        """
        try:
            float_value = float(input_value)
            if min_val is not None and float_value < min_val:
                print(f"Value must be at least {min_val}.")
                return False
            if max_val is not None and float_value > max_val:
                print(f"Value must be no more than {max_val}.")
                return False
            return True
        except ValueError:
            print("Invalid input. Please enter a floating-point number.")
            return False

    def get_string_input(self, prompt="Enter a string: ", min_length=None, max_length=None):
        """
        Prompts the user to enter a string that meets the specified length constraints.

        Parameters:
        - prompt (str): The message to display to the user.
        - min_length (int, optional): Minimum allowable length of the string.
        - max_length (int, optional): Maximum allowable length of the string.

        Returns:
        - str: A validated string input.
        """
        while True:
            user_input = input(prompt)
            if self.is_valid_string(user_input, min_length, max_length):
                return user_input

    def get_int_input(self, prompt="Enter an integer: ", min_val=None, max_val=None):
        """
        Prompts the user to enter an integer within the specified range.

        Parameters:
        - prompt (str): The message to display to the user.
        - min_val (int, optional): Minimum allowable value.
        - max_val (int, optional): Maximum allowable value.

        Returns:
        - int: A validated integer input.
        """
        while True:
            user_input = input(prompt)
            if self.is_valid_int(user_input, min_val, max_val):
                return int(user_input)

    def get_float_input(self, prompt="Enter a float: ", min_val=None, max_val=None):
        """
        Prompts the user to enter a float within the specified range.

        Parameters:
        - prompt (str): The message to display to the user.
        - min_val (float, optional): Minimum allowable value.
        - max_val (float, optional): Maximum allowable value.

        Returns:
        - float: A validated floating-point input.
        """
        while True:
            user_input = input(prompt)
            if self.is_valid_float(user_input, min_val, max_val):
                return float(user_input)

    def is_valid_email(self, email):
        """
        Validates if the given email address is in a proper format.

        Parameters:
        - email (str): The email address to validate.

        Returns:
        - bool: True if the email address is valid, False otherwise.
        """
        email_pattern = r"^(?=.{1,64}@.{1,255}$)(?=.{6,256}$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.match(email_pattern, email))

    def is_valid_phone(self, phone):
        """
        Validates if the given phone number is a valid Indian mobile number.

        Parameters:
        - phone (str): The phone number to validate. Can optionally include the "+91" country code prefix.

        Returns:
        - bool: True if the phone number is valid, False otherwise.
        """
        phone_pattern = r"^(\+91[-\s]?)?[6-9]\d{9}$"
        return bool(re.match(phone_pattern, phone))

    def is_valid_password(self, password, min_length=None, max_length=None):
        """
        Validates if the password meets specified length constraints.

        Parameters:
        - password (str): The password to validate.
        - min_length (int, optional): Minimum allowable length.
        - max_length (int, optional): Maximum allowable length.

        Returns:
        - bool: True if the password is valid, False otherwise.
        """
        if min_length is not None and len(password) < min_length:
            return False
        if max_length is not None and len(password) > max_length:
            return False
        return True

    def get_email_input(self, prompt="Enter an email address: "):
        """
        Prompts the user to enter a valid email address.

        Parameters:
        - prompt (str): The message to display to the user.

        Returns:
        - str: A validated email address.
        """
        while True:
            email = input(prompt)
            if self.is_valid_email(email):
                return email
            else:
                print("Invalid email format. Please enter a valid email address.")

    def get_phone_input(self, prompt="Enter a phone number: "):
        """
        Prompts the user to enter a valid Indian phone number.

        Parameters:
        - prompt (str): The message to display to the user.

        Returns:
        - str: A validated phone number.
        """
        while True:
            phone = input(prompt)
            if self.is_valid_phone(phone):
                return phone
            else:
                print("Phone number must be 10 digits, optionally starting with '+91'. First digit must be 6-9.")

    def get_password_input(self, prompt="Enter a password: ", min_length=8, max_length=20):
        """
        Prompts the user to enter a password that meets length constraints.

        Parameters:
        - prompt (str): The message to display to the user.
        - min_length (int): Minimum allowable password length.
        - max_length (int): Maximum allowable password length.

        Returns:
        - str: A hashed version of the validated password.
        """
        while True:
            password = getpass.getpass(prompt)
            
            # Check if password is empty
            if len(password) == 0:
                print("Password cannot be empty. Please enter a valid password.")
                continue
            
            # Validate the password length
            if not self.is_valid_password(password, min_length, max_length):
                if min_length is not None and len(password) < min_length:
                    print(f"Password must be at least {min_length} characters long.")
                elif max_length is not None and len(password) > max_length:
                    print(f"Password must be no longer than {max_length} characters.")
            else:
                password_handler = Password()
                return password_handler.hash_password(password)