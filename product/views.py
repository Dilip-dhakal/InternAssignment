from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ProductModel
from .serializers import ProductSerializers


class ProductAPIView(APIView):
    """
    Handles List (GET) and Create (POST) for Vendors
    """
    def get(self, request):
        products = ProductModel.objects.filter(is_active=True)
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = productSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    """
    Handles Retrieve (GET), Update (PUT), and Delete (DELETE)
    """
    def get_object(self, id):
        return get_object_or_404(ProductModel, pk=id, is_active=True)
    
    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = self.get_object(id)
        serializer =ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        product.is_active = False
        product.save()
        return Response({"message": "Soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)