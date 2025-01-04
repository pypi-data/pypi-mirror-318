import re
from profanity_check import predict
from zxcvbn import zxcvbn

class FortiPassValidator:
    """
    A class to validate password strength based on user-defined settings.
    """
    def __init__(self, min_length=8, require_upper=True, require_lower=True, require_numbers=True, require_special=True,
                 avoid_common=True, log_attempts=False):
        """
        Initialize the FortiPassValidator with specific settings.

        :param min_length: Minimum password length (default: 8).
        :param require_upper: Require at least one uppercase letter (default: True).
        :param require_lower: Require at least one lowercase letter (default: True).
        :param require_numbers: Require at least one number (default: True).
        :param require_special: Require at least one special character (default: True).
        :param avoid_common: Check against common passwords using zxcvbn (default: True).
        :param log_attempts: Log password validation attempts (default: False).
        """
        self.min_length = min_length
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_numbers = require_numbers
        self.require_special = require_special
        self.avoid_common = avoid_common
        self.log_attempts = log_attempts

    def validate(self, password):
        """
        Validate the password against the set rules.

        :param password: Password to validate.
        :return: A tuple containing a boolean (valid/invalid) and feedback message.
        """
        feedback = []

        # Check minimum length
        if len(password) < self.min_length:
            feedback.append(f"Password must be at least {self.min_length} characters long.")

        # Check uppercase letters
        if self.require_upper and not re.search(r'[A-Z]', password):
            feedback.append("Consider adding uppercase letters (e.g., A, B, C).")

        # Check lowercase letters
        if self.require_lower and not re.search(r'[a-z]', password):
            feedback.append("Consider adding lowercase letters (e.g., a, b, c).")

        # Check numeric digits
        if self.require_numbers and not re.search(r'\d', password):
            feedback.append("Consider adding numbers (e.g., 1, 2, 3).")

        # Check special characters
        if self.require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            feedback.append("Consider adding special characters (e.g., @, #, $).")

        # Check common passwords using zxcvbn
        if self.avoid_common:
            zxcvbn_result = zxcvbn(password)
            if zxcvbn_result['score'] < 3:  # Score ranges from 0 (weak) to 4 (strong)
                feedback.append("This password is too weak or commonly used. Please choose a more unique password.")

        # Check inappropriate language
        if predict([password])[0] == 1:
            feedback.append("Password contains inappropriate language.")

        # Log validation attempts if enabled
        if self.log_attempts:
            with open("password_validation_log.txt", "a") as log_file:
                log_file.write(f"Password validation attempted: {password}\n")

        # Provide suggestions if invalid
        if feedback:
            feedback.append("Consider using a password manager to create and store complex passwords securely.")
            return False, " ".join(feedback)

        return True, "Password is valid."

if __name__ == "__main__":
    # Example usage
    validator = FortiPassValidator(min_length=10, avoid_common=True, log_attempts=True)
    password = input("Enter a password to validate: ")
    is_valid, feedback = validator.validate(password)
    print(f"Valid: {is_valid}, Feedback: {feedback}")
