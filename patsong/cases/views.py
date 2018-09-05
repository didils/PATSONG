from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllCases(APIView):

    def get(self, request, format=None):

        all_cases = models.Case.objects.filter(owner__username=request.user)

        serializer = serializers.CaseSerializer(all_cases, many=True)

        """
        Serializer로 serialize할 때, 동일한 모델을 serialize하는 serializer를 사용해야만 함.
        
        여기서, all_cases는 models.Case이고,
        CaseSerialize 역시 models.Case를 씨리얼라이즈하고 있으(serializer.py참조)므로 가능
        """

        return Response(data=serializer.data)