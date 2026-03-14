from django.urls import path
from .views import VendorAPIView,VendorDetailAPIView

urlpatterns = [
    path("vendor",VendorAPIView.as_view(),name="vendor-api-view"),
    path("vendor/<uuid:id>",VendorDetailAPIView.as_view(),name="vendor-detail-api")
]
