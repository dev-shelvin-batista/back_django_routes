from rest_framework import serializers
from ..models.Routes import Routes

class RoutesSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=250)
    origin = serializers.CharField(max_length=150)
    destination = serializers.CharField(max_length=150)
    
    def create(self, validated_data):
        route = Routes.objects.create(**validated_data)
        
        return route
    
    class Meta:
        model = Routes
        fields = ['id', 'description', 'origin', 'destination']