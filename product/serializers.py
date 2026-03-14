from rest_framework import serializers
from .models import ProductModel

class ProductSerializers(serializers.Serializer):
    class Meta:
        model=ProductModel
        fields="__all__"