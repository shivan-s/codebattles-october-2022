"""Custom pagination for views."""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from config.settings import PAGE_SIZE


class StandardSetPagination(PageNumberPagination):
    """Custom Pagination rules."""

    page_size = PAGE_SIZE
    page_size_query_param = "limit"
    max_page_size = 10_000

    def get_paginated_response(self, data):
        """Response given for paginated view."""
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "per_page": self.page.paginator.per_page,
                "results": data,
            }
        )
