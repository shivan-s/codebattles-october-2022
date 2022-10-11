"""Testing Company model."""

import pytest
from pytest_lazyfixture import lazy_fixture
from rest_framework import status

from api.models import Advocate, Company

pytestmark = pytest.mark.django_db


class TestCompany:
    """Testing Advocate endpoints."""

    url = "/api/v1/companies"

    def test_instance(self, company):
        """Test if the instance is correct and true."""
        assert isinstance(company, Company)

    def test_list(self, client, company_factory):
        """Test list view for companies."""
        companies = company_factory.create_batch(1000)
        response = client.get(f"{self.url}")
        assert response.status_code == status.HTTP_200_OK
        result = response.json()
        assert result["count"] == len(companies)

    def test_retrieve(self, client, company_with_advocates):
        """Test retrieve view for companies with advocates."""
        response = client.get(f"{self.url}/{company_with_advocates.pk}")
        assert response.status_code == status.HTTP_200_OK
        result = response.json()
        assert result["name"] == company_with_advocates.name
        assert (
            len(result["advocates"])
            == Advocate.objects.filter(company=company_with_advocates).count()
        )

    def test_find(self, client, company, company_factory):
        """Test search for companies."""
        company_factory.create_batch(100)
        response = client.get(f"{self.url}?search={company.name}")
        assert response.status_code == status.HTTP_200_OK
        result = response.json()
        assert result["count"] < Company.objects.all().count()
        assert result["results"][0]["name"] == company.name

    @pytest.mark.parametrize(
        "test_client,expected",
        [
            pytest.param(
                lazy_fixture("client"),
                status.HTTP_401_UNAUTHORIZED,
                id="client-create",
            ),
            pytest.param(
                lazy_fixture("admin_client"),
                status.HTTP_201_CREATED,
                id="admin-client-create",
            ),
        ],
    )
    def test_create(self, test_client, expected, company_factory):
        """Test creation of company as well as authority to create."""
        company = company_factory.stub()
        response = test_client.post(
            f"{self.url}/",
            data=company,
            content_type="application/json",
        )
        assert response.status_code == expected
        if response.status_code == status.HTTP_201_CREATED:
            assert response["name"] == company.name
        else:
            assert Company.objects.all().count() == 0

    @pytest.mark.parametrize(
        "test_client,expected",
        [
            pytest.param(
                lazy_fixture("client"),
                status.HTTP_401_UNAUTHORIZED,
                id="client-update",
            ),
            pytest.param(
                lazy_fixture("admin_client"),
                status.HTTP_200_OK,
                id="admin-client-update",
            ),
        ],
    )
    def test_update(self, test_client, expected, company, company_factory):
        """Test update of company as well as authority to update."""
        new_company = company_factory.stub()
        response = test_client.post(
            f"{self.url}/{company.pk}",
            data=new_company,
            content_type="application/json",
        )
        assert response.status_code == expected
        if response.status_code == status.HTTP_200_OK:
            assert response["name"] == new_company.name
        else:
            assert Company.objects.get(pk=company.pk).name != new_company.name

    @pytest.mark.parametrize(
        "test_client,expected",
        [
            pytest.param(
                lazy_fixture("client"),
                status.HTTP_401_UNAUTHORIZED,
                id="client-delete",
            ),
            pytest.param(
                lazy_fixture("admin_client"),
                status.HTTP_204_NO_CONTENT,
                id="admin-client-delete",
            ),
        ],
    )
    def test_delete(self, test_client, expected, company):
        """Test deletion of company as well as authority to delete."""
        response = test_client.post(f"{self.url}/{company.pk}")
        assert response.status_code == expected
        if response.status_code == status.HTTP_204_NO_CONTENT:
            assert Company.objects.filter(pk=company.pk).exists() is False
        else:
            assert Company.objects.filter(pk=company.pk).exists() is True
