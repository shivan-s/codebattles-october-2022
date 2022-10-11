"""Company factories."""

import factory
from faker import Faker

from api.models import Company

Faker.seed(42)
faker = Faker("en_NZ")


class CompanyFactory(factory.django.DjangoModelFactory):
    """Company Factory for test."""

    class Meta:
        """Factory settings."""

        model = Company

    name = factory.Faker("company")
    logo = factory.Faker("file_name", category="image")
    summary = factory.Faker("catch_phrase")
