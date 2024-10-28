from django.core.validators import (
    RegexValidator
)

phone_number_country_code_validator = RegexValidator(
    regex=r'^\+\d{1,3}',
    message="Phone number must have a valid country code."
)

phone_number_number_validator = RegexValidator(
    regex=r'\d{8,}',
    message="Phone number must have at least 8 digits."
)

