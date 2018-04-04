# from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

# creating new manager for user


class CustomUserManager(UserManager):
    pass

# declaring new formed manager to be user manager


class CustomUser(AbstractUser):
    objects = CustomUserManager()

