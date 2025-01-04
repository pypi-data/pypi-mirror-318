import unittest
from fortipass.validator import FortiPassValidator

class TestFortiPassValidator(unittest.TestCase):
    def setUp(self):
        self.validator = FortiPassValidator(min_length=8, require_upper=True, require_lower=True, require_numbers=True, require_special=True, avoid_common=True)

    def test_valid_password(self):
        is_valid, feedback = self.validator.validate("ValidPass123!")
        self.assertTrue(is_valid)
        self.assertEqual(feedback, "Password is valid.")

    def test_short_password(self):
        is_valid, feedback = self.validator.validate("Short1!")
        self.assertFalse(is_valid)
        self.assertIn("at least 8 characters", feedback)

    def test_no_uppercase(self):
        is_valid, feedback = self.validator.validate("lowercase123!")
        self.assertFalse(is_valid)
        self.assertIn("Consider adding uppercase letters", feedback)

    def test_no_lowercase(self):
        is_valid, feedback = self.validator.validate("UPPERCASE123!")
        self.assertFalse(is_valid)
        self.assertIn("Consider adding lowercase letters", feedback)

    def test_no_number(self):
        is_valid, feedback = self.validator.validate("NoNumber!")
        self.assertFalse(is_valid)
        self.assertIn("Consider adding numbers", feedback)

    def test_no_special_character(self):
        is_valid, feedback = self.validator.validate("NoSpecial123")
        self.assertFalse(is_valid)
        self.assertIn("Consider adding special characters", feedback)

    def test_contains_profanity(self):
        is_valid, feedback = self.validator.validate("Badword123!")
        self.assertFalse(is_valid)
        self.assertIn("Password contains inappropriate language", feedback)

    def test_common_password(self):
        is_valid, feedback = self.validator.validate("password")
        self.assertFalse(is_valid)
        self.assertIn("This password is too weak or commonly used", feedback)

    def test_custom_min_length(self):
        custom_validator = FortiPassValidator(min_length=12)
        is_valid, feedback = custom_validator.validate("Short1!")
        self.assertFalse(is_valid)
        self.assertIn("at least 12 characters", feedback)

    def test_custom_requirements(self):
        custom_validator = FortiPassValidator(require_upper=False, require_special=False)
        is_valid, feedback = custom_validator.validate("alllowercase123")
        self.assertTrue(is_valid)
        self.assertEqual(feedback, "Password is valid.")

    def test_all_requirements_disabled(self):
        custom_validator = FortiPassValidator(min_length=1, require_upper=False, require_lower=False, require_numbers=False, require_special=False)
        is_valid, feedback = custom_validator.validate("1")
        self.assertTrue(is_valid)
        self.assertEqual(feedback, "Password is valid.")

if __name__ == "__main__":
    unittest.main()