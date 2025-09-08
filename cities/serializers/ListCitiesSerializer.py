from rest_framework import serializers
from ..models.Cities import Cities

class ListCitiesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=250)
    
    class Meta:
        model = Cities
        fields = ['id', 'description']