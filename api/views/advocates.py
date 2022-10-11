"""Advocate Viewset."""

from rest_framework import filters, viewsets

from api.models import Advocate
from api.serializers import AdvocateDetailSerializer, AdvocateSerializer


class AdvocateViewSet(viewsets.ModelViewSet):
    """List all developer advocates.

    - `/advocates/:id` - provide a detail view for a particular company.
    - `/advocates?search=` - provide search query.
    """

    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    def get_queryset(self):
        """Queryset."""
        return Advocate.objects.all()

    def get_serializer_class(self):
        """Serialize data."""
        if self.action == "retrieve":
            return AdvocateDetailSerializer
        return AdvocateSerializer
