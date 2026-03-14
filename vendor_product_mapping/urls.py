from django.urls import path
from .views import VendorProductMappingListCreateView,VendorProductMappingDetailView
    

urlpatterns = [
    path("vendor-product-mappings/",VendorProductMappingListCreateView.as_view()),
    path("vendor-product-mappings/<uuid:pk>/",VendorProductMappingDetailView.as_view()),
]