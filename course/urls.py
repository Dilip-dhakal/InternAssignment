from django.urls import path
from .views import CourseAPIView,CourseDetailAPIView

urlpatterns = [
    path("course",CourseAPIView.as_view(),name="courses"),
    path("course:<uuid:id>",CourseDetailAPIView.as_view(),name="course-details")
]
