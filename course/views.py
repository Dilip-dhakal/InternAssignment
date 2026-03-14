from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CourseModel
from .serializers import CourseSerializers


class CourseAPIView(APIView):
    """
    Handles List (GET) and Create (POST) for Vendors
    """
    def get(self, request):
        courses = CourseModel.objects.filter(is_active=True)
        serializer = CourseSerializers(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailAPIView(APIView):
    """
    Handles Retrieve (GET), Update (PUT), and Delete (DELETE)
    """
    def get_object(self, id):
        return get_object_or_404(CourseModel, pk=id, is_active=True)
    
    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializers(course)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = self.get_object(id)
        serializer =CourseSerializers(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        course.is_active = False
        course.save()
        return Response({"message": "Soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)