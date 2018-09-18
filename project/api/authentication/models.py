from django.contrib.auth.models import AbstractUser
from django.db import models
from project.api.models import TimestampedModel

class User(AbstractUser, TimestampedModel):
    date_joined = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
