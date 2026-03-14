from rest_framework import serializers
from .models import VendorModel

class VendorSerializers(serializers.Serializer):
    class Meta:
        model=VendorModel
        fields="__all__"