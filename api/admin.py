"""Admin."""
from django.contrib import admin

from api.models import Advocate, Company


class AdvocateAdmin(admin.ModelAdmin):
    """Admin view for Advocate."""

    search_field = ("name",)
    readonly_fields = ("id",)
    list_display = (
        "join_date",
        "short_bio",
        "long_bio",
        "profile_pic",
        "company",
        "youtube_username",
        "twitter_username",
        "github_username",
    )


class CompanyAdmin(admin.ModelAdmin):
    """Admin view for Company."""

    search_field = ("name",)
    readonly_fields = ("id",)
    list_display = ("summary",)


admin.site.register(Advocate, AdvocateAdmin)
admin.site.register(Company, CompanyAdmin)
