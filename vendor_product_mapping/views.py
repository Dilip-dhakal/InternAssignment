from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import VendorProductMapping
from .serializers import VendorProductSerializers

class VendorProductMappingListCreateView(APIView):

    def get(self, request):
        queryset = VendorProductMapping.objects.all()

        vendor_id = request.query_params.get("vendor_id")

        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)

        serializer = VendorProductSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorProductSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VendorProductMappingDetailView(APIView):

    def get(self, request, id):
        mapping = get_object_or_404(VendorProductMapping, pk=id)
        serializer = VendorProductMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, id):
        mapping = get_object_or_404(VendorProductMapping, pk=id)
        serializer = VendorProductMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, id):
        mapping = get_object_or_404(VendorProductMapping, pk=id)
        serializer = VendorProductMappingSerializer(
            mapping, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        mapping = get_object_or_404(VendorProductMapping, pk=id)
        mapping.is_active=False
        mapping.save()
        return Response(status=status.HTTP_204_NO_CONTENT)