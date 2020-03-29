"""Posts models."""

from django.contrib.auth.models import User
# Django
from django.db import models

# Models
from users.models import Profile


class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{title} by {user}".format(title=self.title, user=self.user.username)
