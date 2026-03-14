from rest_framework import serializers
from .models import CertificationModel

class CertificationSerializers(serializers.Serializer):
    class Meta:
        model=CertificationModel
        fields="__all__"