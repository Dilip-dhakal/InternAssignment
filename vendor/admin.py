from django.contrib import admin
from .models import VendorModel

@admin.register(VendorModel)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "is_active", "created_at")
    search_fields = ("name", "code")
    list_filter = ("is_active",)