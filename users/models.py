"""User model."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """The User model."""

    username = models.CharField(_("username"), unique=True, max_length=25)
    name = models.CharField(_("name"), max_length=155, blank=True)
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        """Represent as string."""
        return self.username
