"""Users models."""

from django.conf import settings
from django.contrib.auth import get_user_model
# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Profile model.

    Extends the information of the User model.
    """

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the username"""
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    """Create the profile automatically when creating a user."""
    Profile.objects.get_or_create(user=instance)
