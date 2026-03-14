from django.contrib import admin
from .models import CourseCertificationMapping

@admin.register(CourseCertificationMapping)
class CourseCertificationMappingAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "certification", "primary_mapping", "created_at")
    search_fields = ("course", "certification")
    list_filter = ("primary_mapping",)