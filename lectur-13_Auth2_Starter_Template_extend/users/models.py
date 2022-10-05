from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    portfolio =  models.CharField(max_length=100, blank=True)
    proile_pic = models.ImageField(upload_to="profile_pic", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

