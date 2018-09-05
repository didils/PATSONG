from rest_framework import serializers
from . import models
from patsong.relations import models as relation_models
    
class RelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = relation_models.Relation
        fields = (
            'product1',
            'product2',
            'count'
        )