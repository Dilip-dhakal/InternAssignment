from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CertificationModel
from .serializers import CertificationSerializers


class CertificationAPIView(APIView):
    """
    Handles List (GET) and Create (POST) for Vendors
    """
    def get(self, request):
        certification = CertificationModel.objects.filter(is_active=True)
        serializer = CertificationSerializers(certification, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CertificationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationDetailAPIView(APIView):
    """
    Handles Retrieve (GET), Update (PUT), and Delete (DELETE)
    """
    def get_object(self, id):
        return get_object_or_404(CertificationModel, pk=id, is_active=True)
    
    def get(self, request, id):
        certification = self.get_object(id)
        serializer = CertificationSerializers(certification)
        return Response(serializer.data)
    
    def put(self, request, id):
        certification = self.get_object(id)
        serializer =CertificationSerializers(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        certification = self.get_object(id)
        certification.is_active = False
        certification.save()
        return Response({"message": "Soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)