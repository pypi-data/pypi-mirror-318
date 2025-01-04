import re
from profanity_check import predict

class FortiPassValidator:
    """
    A class to validate password strength based on user-defined settings.
    """
    def __init__(self, min_length=8, require_upper=True, require_lower=True, require_numbers=True, require_special=True):
        """
        Initialize the FortiPassValidator with specific settings.

        :param min_length: Minimum password length (default: 8).
        :param require_upper: Require at least one uppercase letter (default: True).
        :param require_lower: Require at least one lowercase letter (default: True).
        :param require_numbers: Require at least one number (default: True).
        :param require_special: Require at least one special character (default: True).
        """
        self.min_length = min_length
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_numbers = require_numbers
        self.require_special = require_special

    def validate(self, password):
        """
        Validate the password against the set rules.

        :param password: Password to validate.
        :return: A tuple containing a boolean (valid/invalid) and feedback message.
        """
        if len(password) < self.min_length:
            return False, f"Password must be at least {self.min_length} characters long."

        if self.require_upper and not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter."

        if self.require_lower and not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter."

        if self.require_numbers and not re.search(r'\d', password):
            return False, "Password must contain at least one numeric digit."

        if self.require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "Password must contain at least one special character."

        if predict([password])[0] == 1:
            return False, "Password contains inappropriate language."

        return True, "Password is valid."

if __name__ == "__main__":
    # Example usage
    validator = FortiPassValidator(min_length=10)
    password = input("Enter a password to validate: ")
    is_valid, feedback = validator.validate(password)
    print(f"Valid: {is_valid}, Feedback: {feedback}")

