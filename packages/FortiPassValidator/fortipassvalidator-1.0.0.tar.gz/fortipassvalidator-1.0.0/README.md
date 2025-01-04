# FortiPassValidator

FortiPassValidator is a Python library for validating passwords against customizable rules. It helps ensure that passwords are strong, meet complexity requirements, and avoid inappropriate language.

## Features

- Validate password length, uppercase, lowercase, numbers, and special characters.
- Detect inappropriate language in passwords using the `profanity-check` library.
- Fully customizable validation settings.
- Lightweight and easy to integrate into your projects.

## Installation

Install the library using pip:

```bash
pip install FortiPassValidator
```

## Usage

### Default Settings

By default, FortiPassValidator enforces the following rules:
- Minimum length: 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one numeric digit
- At least one special character

Example:

```python
from fortipass import FortiPassValidator

validator = FortiPassValidator()

password = "ValidPass123!"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: True, Feedback: Password is valid.
```

### Customizing Validation Rules

You can adjust the validation rules to fit your requirements:

- **Custom Minimum Length**: Enforce a minimum length of 12 characters.

```python
validator = FortiPassValidator(min_length=12)
password = "Short1!"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: False, Feedback: Password must be at least 12 characters long.
```

- **Disabling Uppercase Requirement**: Allow passwords without uppercase letters.

```python
validator = FortiPassValidator(require_upper=False)
password = "lowercase123!"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: True, Feedback: Password is valid.
```

- **Disabling Special Characters Requirement**: Allow passwords without special characters.

```python
validator = FortiPassValidator(require_special=False)
password = "Password123"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: True, Feedback: Password is valid.
```

### Profanity Detection

FortiPassValidator detects inappropriate language in passwords using the `profanity-check` library. This ensures that offensive words are flagged during validation.

Example:

```python
password = "Badword123!"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: False, Feedback: Password contains inappropriate language.
```

### All Rules Disabled

If you want minimal validation (e.g., for testing purposes), you can disable all rules:

```python
validator = FortiPassValidator(min_length=1, require_upper=False, require_lower=False, require_numbers=False, require_special=False)
password = "a"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: True, Feedback: Password is valid.
```

### Comprehensive Validation

You can combine multiple rules to create a highly secure validation setup:

```python
validator = FortiPassValidator(min_length=16, require_upper=True, require_lower=True, require_numbers=True, require_special=True)
password = "SuperSecure123!"
is_valid, feedback = validator.validate(password)
print(f"Valid: {is_valid}, Feedback: {feedback}")
# Output: Valid: True, Feedback: Password is valid.
```

## Testing

To test the library, use the provided unit tests in the `tests` directory. Run the following command:

```bash
python -m unittest discover tests
```

## Project Structure

```
FortiPassValidator/
├── fortipass/
│   ├── __init__.py
│   ├── validator.py
├── tests/
│   ├── test_validator.py
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
```

## Dependencies

- `profanity-check`: Used to detect inappropriate language in passwords.

To install dependencies, run:

```bash
pip install -r requirements.txt
```

## Contribution

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

Ahmed Abdelrahman

- Email: [ahmad18189@gmail.com](mailto:ahmad18189@gmail.com)
- GitHub: [https://github.com/ahmad18189/FortiPassValidator](https://github.com/ahmad18189/FortiPassValidator)

## Example Use Cases

### Web Applications
Enforce strong password policies during user registration and account updates.

### Internal Tools
Validate passwords for employees or system administrators to ensure they follow best practices.

### Educational Projects
Demonstrate password security concepts and secure coding practices.

### Command-Line Tools
Integrate FortiPassValidator into CLI tools to check password strength in bulk or interactively.

## FAQ

**1. What happens if profanity-check doesn’t recognize a language?**
   - The `profanity-check` library works well with English. For other languages, you may need to integrate additional profanity-detection tools.

**2. Can I disable profanity detection?**
   - Yes, you can remove or replace the profanity-check logic in the `validate` method if it is not required for your use case.

**3. Is the library thread-safe?**
   - Yes, the library is designed to be thread-safe.

**4. How do I report bugs or request features?**
   - Please open an issue on the GitHub repository: [FortiPassValidator Issues](https://github.com/ahmad18189/FortiPassValidator/issues).

---

Thank you for using FortiPassValidator! Feel free to contribute or reach out with questions.

