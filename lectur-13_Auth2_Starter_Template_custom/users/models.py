from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    portfolio = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)