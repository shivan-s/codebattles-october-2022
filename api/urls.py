"""API Router endpoints."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import AdvocateViewSet, CompanyViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"advocates", AdvocateViewSet, "advocates")
router.register(r"companies", CompanyViewSet, "companies")

urlpatterns = (path("", include(router.urls)),)
