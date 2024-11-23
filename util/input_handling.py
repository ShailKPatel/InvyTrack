#input_handling.py
import re
import getpass

class InputValidator:
    def __init__(self):
        pass

    # Helper methods to validate inputs
    def is_valid_string(self, input_string, min_length=None, max_length=None):
        if min_length is not None and len(input_string) < min_length:
            print(f"String must be at least {min_length} characters long.")
            return False
        if max_length is not None and len(input_string) > max_length:
            print(f"String must be no more than {max_length} characters long.")
            return False
        return True

    def is_valid_int(self, input_value, min_val=None, max_val=None):
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

    # Main input methods that keep re-prompting
    def get_string_input(self, prompt="Enter a string: ", min_length=None, max_length=None):
        while True:
            user_input = input(prompt)
            if self.is_valid_string(user_input, min_length, max_length):
                return user_input

    def get_int_input(self, prompt="Enter an integer: ", min_val=None, max_val=None):
        while True:
            user_input = input(prompt)
            if self.is_valid_int(user_input, min_val, max_val):
                return int(user_input)

    def get_float_input(self, prompt="Enter a float: ", min_val=None, max_val=None):
        while True:
            user_input = input(prompt)
            if self.is_valid_float(user_input, min_val, max_val):
                return float(user_input)

    # Validate regex patterns
    def is_valid_email(self, email):
        """Validates if the given email address is in a proper format."""
        email_pattern = r"^(?=.{1,64}@.{1,255}$)(?=.{6,256}$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.match(email_pattern, email))

    def is_valid_phone(self, phone):
        """
        Validates if the given phone number is a valid Indian mobile number.
        Accepts numbers in the format with an optional "+91" country code prefix.
        """
        phone_pattern = r"^(\+91[-\s]?)?[6-9]\d{9}$"
        return bool(re.match(phone_pattern, phone))

    def is_valid_password(self, password, min_length=None, max_length=None):
        """Validates if the password meets minimum and maximum length constraints."""
        if min_length is not None and len(password) < min_length:
            return False
        if max_length is not None and len(password) > max_length:
            return False
        return True

    # Methods for getting valid information with prompts
    def get_email_input(self, prompt="Enter an email address: "):
        """Prompts the user to enter a valid email address."""
        while True:
            email = input(prompt)
            if self.is_valid_email(email):
                return email
            else:
                print("Invalid email format. Please enter a valid email address.")

    def get_phone_input(self, prompt="Enter a phone number: "):
        """Prompts the user to enter a valid phone number."""
        while True:
            phone = input(prompt)
            if self.is_valid_phone(phone):
                return phone
            else:
                print("Phone number must be 10 digits, optionally starting with '+91'. And first number must me 6/7/8/9 for indian numbers.")

    def get_password_input(self, prompt="Enter a password: ", min_length=None, max_length=None):
        """Prompts the user to enter a password with optional min and max length constraints."""
        while True:
            password = getpass.getpass(prompt)
            if self.is_valid_password(password, min_length=min_length, max_length=max_length):
                return password
            else:
                if min_length is not None and len(password) < min_length:
                    print(f"Password must be at least {min_length} characters long.")
                elif max_length is not None and len(password) > max_length:
                    print(f"Password must be no more than {max_length} characters long.")

# Example usage:
# validator = InputValidator()
# user_email = validator.get_email_input()
# user_password = validator.get_password_input(min_length=8, max_length=16)
