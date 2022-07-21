from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
