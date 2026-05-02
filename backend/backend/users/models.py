from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('HR_ADMIN', 'HR Admin'),
        ('HR_USER', 'HR User'),
        ('MANAGER', 'Manager'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)