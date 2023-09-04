from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="custom_user_groups"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="custom_user_permissions"
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    social_media_links = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username

