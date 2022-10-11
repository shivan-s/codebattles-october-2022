"""Advocate Viewset."""

from rest_framework import filters, viewsets

from api.models import Advocate
from api.serializers import AdvocateDetailSerializer, AdvocateSerializer

from .pagination import StandardSetPagination


class AdvocateViewSet(viewsets.ModelViewSet):
    """List all developer advocates.

    - `/advocates/:id` - provide a detail view for a particular company.
    - `/advocates?search=` - provide search query.
    - `/advocates?limit=` - limit size of response.
    """

    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    pagination_class = StandardSetPagination

    def get_queryset(self):
        """Queryset."""
        return Advocate.objects.all()

    def get_serializer_class(self):
        """Serialize data."""
        if self.action == "retrieve":
            return AdvocateDetailSerializer
        return AdvocateSerializer
