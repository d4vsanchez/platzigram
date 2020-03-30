"""User app configuration"""

from django.apps import AppConfig

# Signals
from users import signals


class UsersConfig(AppConfig):
    """User app config."""

    name = "users"
    verbose_name = "Users"
