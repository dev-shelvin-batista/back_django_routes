from rest_framework import serializers
from ..models.Routes import Routes
from stops.serializers.ListStopsSerializer import ListStopsSerializer
from .ListRoutesSerializer import ListRoutesSerializer

class ListSchedulesRouteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    weekday = serializers.IntegerField()
    arrival_time = serializers.TimeField()
    departure_time = serializers.TimeField()
    stop = ListStopsSerializer()
    route = ListRoutesSerializer()
    
    class Meta:
        model = Routes
        fields = ['id', 'weekday', 'arrival_time', 'departure_time', 'stop', 'route']