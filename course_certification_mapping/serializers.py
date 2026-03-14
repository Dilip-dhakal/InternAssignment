from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationSerializers(serializers.Serializer):
    class Meta:
        model=CourseCertificationMapping
        fields="__all__"
        
    def validate(self, data):

        course = data.get("course")
        primary = data.get("primary_mapping")

        if primary:
            if CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True
            ).exists():

                raise serializers.ValidationError(
                    "This course already has a primary certification."
                )

        return data