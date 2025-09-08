from rest_framework import serializers
from ..models.Routes import Routes
from ..models.Schedules import Schedules
from stops.models.Stops import Stops

class SchedulesRouteSerializer(serializers.Serializer):
    weekday = serializers.IntegerField()
    arrival_time = serializers.TimeField()
    departure_time = serializers.TimeField()
    stop_id = serializers.IntegerField()
    route_id = serializers.IntegerField()
    
    """ Validar existencia de la parada """
    def validate_parada_id(self, value):
        stop_data = Stops.objects.filter(id=value)
            
        if stop_data.__len__() == 0:                
            raise serializers.ValidationError("Parada no existe")
        
        return value
    
    """ Validar existencia de la ruta """
    def validate_route_id(self, value):
        route_data = Routes.objects.filter(id=value)
            
        if route_data.__len__() == 0:                
            raise serializers.ValidationError("Ruta no existe")
        
        return value
    
    def create(self, validated_data):
        schedule = Schedules.objects.create(**validated_data)        
        return schedule
    
    class Meta:
        model = Schedules
        fields = ['id', 'weekday', 'arrival_time', 'departure_time']