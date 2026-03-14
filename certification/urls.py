from django.urls import path
from .views import CertificationDetailAPIView,CertificationAPIView


urlpatterns = [
    path("certification",CertificationAPIView.as_view(),name="certification"),
    path("certifiaction/<uuid:id>",CertificationDetailAPIView.as_view(),name="certification-detail")
]

