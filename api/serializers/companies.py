"""Company serializer."""

from rest_framework import serializers

from api.models import Advocate, Company
from api.serializers import AdvocateSerializer


class CompanySerializer(serializers.ModelSerializer):
    """Company Serializer for list view."""

    url = serializers.HyperlinkedIdentityField(
        view_name="companies-detail", read_only=True
    )

    class Meta:
        """Serializer settings."""

        model = Company
        fields = [
            "id",
            "url",
            "name",
            "logo",
            "summary",
        ]


class CompanyDetailSerializer(CompanySerializer):
    """Company Serializer for detail view."""

    advocates = serializers.SerializerMethodField()

    def get_advocates(self, company):
        """Get advocates for the company."""
        advocates = Advocate.objects.filter(company=company)
        return AdvocateSerializer(
            advocates, many=True, read_only=True, context=self.context
        ).data

    class Meta(CompanySerializer.Meta):
        """Serializer settings."""

        fields = CompanySerializer.Meta.fields + ["advocates"]
