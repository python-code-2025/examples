from abc import ABC, abstractmethod
import re

class Validator(ABC):
    @abstractmethod
    def validate(self, data: str) -> bool:
        pass

class EmailValidator(Validator):
    def validate(self, data: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, data))

class PhoneValidator(Validator):
    def validate(self, data: str) -> bool:
        pattern = r'^\+?[1-9]\d{1,14}$'  # Supports international phone numbers
        return bool(re.match(pattern, data))

# Example usage
email_validator = EmailValidator()
phone_validator = PhoneValidator()

print(email_validator.validate("test@example.com"))  # True
print(email_validator.validate("invalid-email"))      # False
print(phone_validator.validate("+1234567890"))       # True
print(phone_validator.validate("12345"))            # False
