from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

class SaveRelations(APIView):

    def post(self, request, format=None):

        products = request.data['products']
        products = products.split(",")

        n = 0
        while n < len(products):
            relation_data = models.Relation.objects.all()
            m = n+1
            
            while m < len(products):
                
                if relation_data.filter(product1=products[n], product2=products[m]):
                    asdf = relation_data.get(product1=products[n], product2=products[m])
                    asdf.count += 1
                    asdf.save()
                    print(products[n], '과', products[m], '의 카운트를', asdf.count-1, '에서', asdf.count, '로 증가!')

                elif relation_data.filter(product1=products[m], product2=products[n]):
                    asdf = relation_data.get(product1=products[m], product2=products[n])
                    asdf.count += 1
                    asdf.save()
                    print(products[n], '과', products[m], '의 카운트를', asdf.count-1, '에서', asdf.count, '로 증가!')

                elif products[m]==products[n]:
                    print('동일 제품끼리는 추가하지 않음!')
                    
                else:
                    models.Relation.objects.create(product1=products[m], product2=products[n], count=1)
                    print(products[n], '과', products[m], '관계를 새로 생성!')
                m += 1
            n += 1
        return Response(status=status.HTTP_200_OK)

class Search(APIView):

    def get(self, request, format=None):

        product = request.query_params.get('product', None)

        if product is not None:

            relations = models.Relation.objects.filter(Q(product1 = product) | Q(product2 = product)).order_by('-count')[:6]

            serializer = serializers.RelationSerializer(
                relations, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
           return Response(status=status.HTTP_200_OK)