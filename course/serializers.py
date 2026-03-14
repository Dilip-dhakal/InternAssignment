from rest_framework import serializers
from .models import CourseModel

class CourseSerializers(serializers.Serializer):
    class Meta:
        model=CourseModel
        fields="__all__"