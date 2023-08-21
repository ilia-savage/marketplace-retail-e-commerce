from django.db import models


from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.EmailField(null=True, default=None, max_length=255, unique=True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=255, null=True, blank=True)
    auth_code = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []