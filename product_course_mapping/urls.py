from django.urls import path
from .views import (
    ProductCourseMappingListCreateView,
    ProductCourseMappingDetailView
)

urlpatterns = [
    path("product-course-mappings/",ProductCourseMappingListCreateView.as_view()),
    path("product-course-mappings/<uuid:pk>/",ProductCourseMappingDetailView.as_view()),
]