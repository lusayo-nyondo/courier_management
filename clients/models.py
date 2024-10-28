from django.db import models
from .validators import (
    phone_number_country_code_validator,
    phone_number_number_validator
)


class Client(models.Model):
    full_name: models.CharField = models.CharField(
        max_length=255
    )
    
    def __str__(self):
        pass


class PhoneNumber(models.Model):
    client: models.ForeignKey = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    country_code: models.CharField = models.CharField(
        max_length=4,
        validators=[
            phone_number_country_code_validator
        ]
    )
    number: models.CharField = models.CharField(
        max_length=12,
        validators=[
            phone_number_number_validator
        ]
    )
    
    def __str__(self):
        return f"{ self.country_code } { self.number }"


class Email(models.Model):
    client: models.ForeignKey = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    address: models.EmailField = models.EmailField()
    
    def __str__(self):
        return self.address
