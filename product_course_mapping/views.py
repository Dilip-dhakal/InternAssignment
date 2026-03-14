from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ProductCourseMapping
from .serializers import ProductCourseSerializers


class ProductCourseMappingListCreateView(APIView):

    def get(self, request):

        queryset = ProductCourseMapping.objects.all()

        product_id = request.query_params.get("product_id")

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        serializer = ProductCourseSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ProductCourseSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
class ProductCourseMappingDetailView(APIView):

    def get(self, request, id):

        mapping = get_object_or_404(ProductCourseMapping, pk=id)
        serializer = ProductCourseMappingSerializer(mapping)

        return Response(serializer.data)

    def put(self, request, id):

        mapping = get_object_or_404(ProductCourseMapping, pk=id)

        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, id):

        mapping = get_object_or_404(ProductCourseMapping, pk=id)

        serializer = ProductCourseMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):

        mapping = get_object_or_404(ProductCourseMapping, pk=id)
        mapping.is_active=False
        mapping.save()
        return Response(status=status.HTTP_204_NO_CONTENT)