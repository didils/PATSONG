from rest_framework import serializers
from . import models
from patsong.users import models as user_models


class CaseUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name',
            'cases'
        )

class CaseSerializer(serializers.ModelSerializer):

    owner = CaseUserSerializer()

    # 여기다가 username = 유저씨리얼라이져 추가해야 하는데, 왜 강좌가 안나오는거지
    # 추가했다!
    # 장고 버전업이 되면서, 특정 필드만 부르는 것이 금지되었음. 따라서, field에 '__all__'을 꼭 넣어야 함 -> 모든 필드 불러내는 듯

    class Meta:
        model = models.Case
        fields = (
            'trademark_title',
            'trademark_image',
            'owner',
            'request_date',
            'payment_date',
            'filed_date',
            'application_number',
            'publication_number',
            'publication_date',
            'registration_number',
            'registration_date',
            'products',
            'product_comment',
            'progress_status'
        )
