from rest_framework import serializers
from ..models.Cities import Cities

class CitiesSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=250)
    
    """ Method for creating a city after the data has passed validation and is correct. """
    def create(self, validated_data):
        city = Cities.objects.create(**validated_data)
        
        return city
    
    class Meta:
        model = Cities
        fields = ['id', 'description']