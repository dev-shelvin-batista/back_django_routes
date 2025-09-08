from rest_framework import serializers
from ..models.Roles import Roles

class ListRolesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=250)
    
    class Meta:
        model = Roles
        fields = ['id', 'description']