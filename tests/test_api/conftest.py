"""Test fixture setup."""

import pytest
from pytest_factoryboy import register

from .factories import AdvocateFactory, CompanyFactory

register(AdvocateFactory)
register(CompanyFactory)


@pytest.fixture
def company_with_advocates():
    """Create company with advocates."""
    company = CompanyFactory()
    (AdvocateFactory(company=company) for _ in range(50))
    return company
