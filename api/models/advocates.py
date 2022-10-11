"""Advocate model.

This represents the developer advocate.
"""
from datetime import datetime

from django.db import models


class Advocate(models.Model):
    """Developer Advocate model."""

    name = models.TextField()
    join_date = models.DateField(default=datetime.now)
    short_bio = models.TextField(null=True, blank=True)
    long_bio = models.TextField(null=True, blank=True)
    profile_pic = models.TextField(null=True, blank=True)
    company = models.ForeignKey(
        "api.Company", on_delete=models.SET_NULL, null=True
    )
    youtube_username = models.TextField(null=True, blank=True)
    twitter_username = models.TextField(null=True, blank=True)
    github_username = models.TextField(null=True, blank=True)

    class Meta:
        """Option for Advocate model."""

        ordering = ["name"]

    @property
    def advocate_years_exp(self) -> int:
        """Give number of years of experience."""
        return datetime.now().year - self.join_date.year

    @property
    def links(self) -> dict[str, str]:
        """Provide social links."""
        return {
            "youtube": f"youtube.com/channel/{self.youtube_username}",
            "twitter": f"twitter.com/{self.twitter_username}",
            "github": f"github.com/{self.github_username}",
        }

    def __str__(self):
        """Represent string."""
        return f"{self.name}"
