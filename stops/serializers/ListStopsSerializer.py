from rest_framework import serializers
from ..models.Stops import Stops
from cities.serializers.ListCitiesSerializer import ListCitiesSerializer

class ListStopsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=250)
    latitude = serializers.CharField(max_length=50)
    longitude = serializers.CharField(max_length=50)
    city = ListCitiesSerializer()
    
    class Meta:
        model = Stops
        fields = ['id', 'description', 'latitude', 'longitude', 'city']