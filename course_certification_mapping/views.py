from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CourseCertificationMapping
from .serializers import CourseCertificationSerializers

class CourseCertificationMappingListCreateView(APIView):

    def get(self, request):

        queryset = CourseCertificationMapping.objects.all()
        course_id = request.query_params.get("course_id")
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        serializer = CourseCertificationSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseCertificationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class CourseCertificationMappingDetailView(APIView):
    def get(self, request, pk):

        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        serializer = CourseCertificationSerializers(mapping)
        return Response(serializer.data)

    def put(self, request, pk):
        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        serializer = CourseCertificationSerializers(mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk):

        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        serializer = CourseCertificationSerializers(mapping,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        mapping.is_active=False
        mapping.save()
        return Response(status=status.HTTP_204_NO_CONTENT)