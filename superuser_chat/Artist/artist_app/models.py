from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    security_answer = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username