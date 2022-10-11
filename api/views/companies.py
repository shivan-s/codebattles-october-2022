"""Company Viewset."""

from rest_framework import filters, viewsets

from api.models import Company
from api.serializers import CompanyDetailSerializer, CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """List all companies.

    - `/companies/:id` - provide a detail view for a particular company.
    - `/companies?search=` - provide search query.
    """

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        """Queryset."""
        return Company.objects.all()

    def get_serializer_class(self):
        """Serialize data."""
        if self.action == "retrieve":
            return CompanyDetailSerializer
        return CompanySerializer
