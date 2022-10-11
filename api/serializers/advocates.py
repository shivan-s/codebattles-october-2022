"""Advocate serializers."""

from rest_framework import serializers

from api.models import Advocate


class AdvocateSerializer(serializers.ModelSerializer):
    """Advocate Serializer for the list view."""

    url = serializers.HyperlinkedIdentityField(
        view_name="advocates-detail", read_only=True
    )

    class Meta:
        """Serializer settings."""

        model = Advocate
        fields = [
            "id",
            "url",
            "name",
            "advocate_years_exp",
            "join_date",
            "short_bio",
            "profile_pic",
            "company",
        ]


class AdvocateDetailSerializer(AdvocateSerializer):
    """Advocate Serializer for the detail view."""

    class Meta(AdvocateSerializer.Meta):
        """Serializer settings."""

        fields = AdvocateSerializer.Meta.fields + ["long_bio", "links"]
