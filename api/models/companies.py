"""Company model.

This represents the company a developer advocate it working.
"""

from django.db import models


class Company(models.Model):
    """Company model."""

    name = models.TextField()
    logo = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    class Meta:
        """Setting for company model."""

        ...
