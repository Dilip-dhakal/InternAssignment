from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductSerializers(serializers.Serializer):
    class Meta:
        model=VendorProductMapping
        fields="__all__"
        
        
    def validate(self, data):

        vendor = data.get("vendor")
        primary = data.get("primary_mapping")

        if primary:
            if VendorProductMapping.objects.filter(
                product=product,
                primary_mapping=True
            ).exists():
                raise serializers.ValidationError(
                    "This product already has a primary course mapping."
                )

        return data