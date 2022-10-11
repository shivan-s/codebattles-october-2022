"""Serializers."""

from .advocates import AdvocateDetailSerializer, AdvocateSerializer
from .companies import CompanyDetailSerializer, CompanySerializer

__all__ = [
    "AdvocateSerializer",
    "AdvocateDetailSerializer",
    "CompanyDetailSerializer",
    "CompanySerializer",
]
