"""Testing Advocate model."""

import pytest
from pytest_lazyfixture import lazy_fixture
from rest_framework import status

from api.models import Advocate

pytestmark = pytest.mark.django_db


class TestAdvocateModel:
    """Testing Advocate custom model properties."""

    def test_advocate_years_exp(self, advocate):
        """Test if advocate years experience generates correctly from date \
                start."""
        assert isinstance(advocate.advocate_years_exp, int)

    def test_links(self, advocate):
        """Test if the social links generate correctly."""
        assert isinstance(advocate.links, dict)


class TestAdvocate:
    """Testing Advocate endpoints."""

    url = "/api/v1/advocates"

    def test_instance(self, advocate):
        """Test if the instance is correct and true."""
        assert isinstance(advocate, Advocate)

    def test_list(self, client, advocate_factory):
        """Test list view for advocates."""
        advocates = advocate_factory.create_batch(1000)
        response = client.get(f"{self.url}")
        response.status_code == status.HTTP_200_OK
        result = response.json()
        assert result["count"] == len(advocates)

    def test_retrieve(self, client, advocate):
        """Test retrieve view for an adovocate."""
        response = client.get(f"{self.url}/{advocate.id}")
        response.status_code == status.HTTP_200_OK
        result = response.json()
        assert result["name"] == advocate.name

    def test_find(self, client, advocate, advocate_factory):
        """Test search for advocates."""
        advocate_factory.create_batch(100)
        response = client.get(f"{self.url}?search={advocate.name}")
        response.status_code == status.HTTP_200_OK
        result = response.json()
        assert result["count"] < Advocate.objects.all().count()
        assert result["results"][0]["name"] == advocate.name

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
    def test_create(self, test_client, expected, advocate_factory):
        """Test creation of company as well as authority to create."""
        advocate = advocate_factory.stub()
        response = test_client.post(
            f"{self.url}",
            data=advocate,
            content_type="application/json",
        )
        response.status_code == expected
        if response.status_code == status.HTTP_201_CREATED:
            assert response["name"] == advocate.name
        else:
            assert Advocate.objects.all().count() == 0

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
    def test_update(self, test_client, expected, advocate, advocate_factory):
        """Test creation of company as well as authority to create."""
        new_advocate = advocate_factory.stub()
        response = test_client.patch(
            f"{self.url}/{advocate.pk}",
            data=new_advocate,
            content_type="application/json",
        )
        response.status_code == expected
        if response.status_code == status.HTTP_200_OK:
            assert response["name"] == new_advocate.name
        else:
            assert (
                Advocate.objects.get(pk=advocate.pk).name != new_advocate.name
            )

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
    def test_delete(self, test_client, expected, advocate):
        """Test creation of company as well as authority to create."""
        response = test_client.delete(f"{self.url}/{advocate.pk}")
        response.status_code == expected
        if response.status_code == status.HTTP_204_NO_CONTENT:
            assert Advocate.objects.filter(pk=advocate.pk).exists() is False
        else:
            assert Advocate.objects.filter(pk=advocate.pk).exists() is True
