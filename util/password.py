# password.py

import bcrypt

class Password:
    
    def __init__(self):
        pass

    def hash_password(self, password: str) -> str:
        """
        This method hashes a password using bcrypt and returns the hashed password.
        bcrypt automatically handles salting (adding random data to the password before hashing).
        """
        # Generate a salt
        salt = bcrypt.gensalt()
        # Hash the password with the salt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        # Return the hashed password as a string (in utf-8)
        return hashed_password.decode('utf-8')
    
    
    def check_password(self, password: str, hashed_password: str) -> bool:
        """
        This method checks if a given password matches the hashed password.
        """
        # Check if the given password matches the stored hashed password
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    def encrypt(self, input_string: str, shift: int = 3) -> str:
        """
        This method encrypts a string by shifting the ASCII value of each character.
        """
        encrypted_string = ''.join([chr(ord(char) + shift) for char in input_string])
        return encrypted_string
    
    def decrypt(self, encrypted_string: str, shift: int = 3) -> str:
        """
        This method decrypts the encrypted string by shifting the ASCII value back.
        """
        decrypted_string = ''.join([chr(ord(char) - shift) for char in encrypted_string])
        return decrypted_string
