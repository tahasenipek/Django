from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default_profile_pic.jpg')
    language_preference = models.CharField(max_length=10, choices=settings.LANGUAGES, default='en')
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username