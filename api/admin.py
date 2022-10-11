"""Admin."""
from django.contrib import admin

from api.models import Advocate, Company


class AdvocateAdmin(admin.ModelAdmin):
    """Admin view for Advocate."""

    search_fields = ("name",)
    readonly_fields = ("id",)
    list_display = ("name",)


class CompanyAdmin(admin.ModelAdmin):
    """Admin view for Company."""

    search_fields = ("name",)
    readonly_fields = ("id",)
    list_display = ("name",)


admin.site.register(Advocate, AdvocateAdmin)
admin.site.register(Company, CompanyAdmin)
