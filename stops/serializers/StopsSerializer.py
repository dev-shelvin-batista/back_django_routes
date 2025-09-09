from rest_framework import serializers
from cities.models.Cities import Cities
from ..models.Stops import Stops

class StopsSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=250)
    latitude = serializers.CharField(max_length=50)
    longitude = serializers.CharField(max_length=50)
    city_id = serializers.IntegerField()
    
    """ Validate the existence of the city """
    def validate_city_id(self, value):
        city_data = Cities.objects.filter(id=value)
            
        if city_data.__len__() == 0:                
            raise serializers.ValidationError("City does not exist")
        
        return value
    
    """ Method for creating a stop after the data has passed validation and is correct. """
    def create(self, validated_data):
        stop = Stops.objects.create(**validated_data)        
        return stop
    
    class Meta:
        model = Stops
        fields = ['id', 'description', 'latitude', 'longitude']