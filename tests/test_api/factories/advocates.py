"""Advocate factories."""

import factory
from faker import Faker

from api.models import Advocate

from .companies import CompanyFactory

Faker.seed(42)
faker = Faker("en_NZ")


class AdvocateFactory(factory.django.DjangoModelFactory):
    """Advocate Factory for test."""

    class Meta:
        """Factory settings."""

        model = Advocate

    name = factory.Faker("name")
    join_date = factory.Faker("date_this_decade")
    short_bio = factory.Faker("sentence")
    long_bio = factory.Faker("paragraph")
    profile_pic = factory.Faker("file_name", category="image")
    company = factory.SubFactory(CompanyFactory)
    twitter_username = factory.Faker("user_name")
    youtube_username = factory.Faker("user_name")
    github_username = factory.Faker("user_name")
