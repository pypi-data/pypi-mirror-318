from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name="Phone Number")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth Date")
