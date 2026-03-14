from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import VendorModel
from .serializers import VendorSerializers


class VendorAPIView(APIView):
    """
    Handles List (GET) and Create (POST) for Vendors
    """
    def get(self, request):
        vendors = VendorModel.objects.filter(is_active=True)
        serializer = VendorSerializers(vendors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDetailAPIView(APIView):
    """
    Handles Retrieve (GET), Update (PUT), and Delete (DELETE)
    """
    def get_object(self, id):
        return get_object_or_404(VendorModel, pk=id, is_active=True)
    
    def get(self, request, id):
        vendor = self.get_object(id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self, request, id):
        vendor = self.get_object(id)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        vendor = self.get_object(id)
        vendor.is_active = False
        vendor.save()
        return Response({"message": "Soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)