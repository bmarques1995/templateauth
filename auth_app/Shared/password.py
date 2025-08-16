import re

from .domain_exception import DomainException
from .crypt import gen_password

class Password():
    def __init__(self, password: str) -> None:
        self.password_value = password
        self.validate_password()
        self.hashed_password = gen_password(self.password_value, rounds=11)

    def validate_password(self) -> None:
    # Define regex patterns
        has_digit = re.search(r'\d', self.password_value)  # Checks for at least one digit
        has_special_char = re.search(r'[\W_]', self.password_value)  # Checks for at least one special character (non-word characters)
        has_letter = re.search(r'[a-zA-Z]', self.password_value)  # Checks for at least one letter (a-z or A-Z)

        # Prepare the result message
        missing_conditions = []
        if not has_digit:
            missing_conditions.append("digit")
        if not has_special_char:
            missing_conditions.append("special character")
        if not has_letter:
            missing_conditions.append("letter")
        if len(self.password_value) < 8:
            missing_conditions.append("less 8 chars")

        if missing_conditions:
            raise InvalidPasswordException(f"String is missing: {', '.join(missing_conditions)}.")
    
class InvalidPasswordException(DomainException):
    def __init__(self, message):
        self.message = f"Invalid password: {message}"
        super().__init__(self.message)
