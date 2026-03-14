from django.urls import path
from .views import (
    CourseCertificationMappingListCreateView,
    CourseCertificationMappingDetailView
)

urlpatterns = [
    path("course-certification-mappings/",CourseCertificationMappingListCreateView.as_view()),
    path("course-certification-mappings/<uuid:id>/",CourseCertificationMappingDetailView.as_view()),
]