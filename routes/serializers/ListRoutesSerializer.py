from rest_framework import serializers
from ..models.Routes import Routes
from django.db import connection
import json

class ListRoutesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=250)
    origin = serializers.CharField(max_length=150)
    destination = serializers.CharField(max_length=150)
    
    class Meta:
        model = Routes
        fields = ['id', 'description', 'origin', 'destination']