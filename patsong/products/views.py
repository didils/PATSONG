from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers, jsons
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

class UploadProducts(APIView):

    def get(self, request, format=None):

        jsons_data = jsons.jsons


        for json in jsons_data:
            models.Product.objects.create(**json)

        return Response(status=status.HTTP_200_OK)

class Search(APIView):

    def get(self, request, format=None):

        keyword = request.query_params.get('keyword', None)

        result = models.Product.objects.filter(Q(product__contains=keyword) | Q(product_en__icontains=keyword))
        
        if result is not None:
            serializer = serializers.ProductSerializer(result, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)