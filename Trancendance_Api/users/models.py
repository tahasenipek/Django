from django.db import models

# Create your models here.




class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(blank=True, null=True)
    language = models.CharField(max_length=255, default="tr")
    tournament_nickname = models.CharField(max_length=255, blank=True, null=True)
    is_online = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username




