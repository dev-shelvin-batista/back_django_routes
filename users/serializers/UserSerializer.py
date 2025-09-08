from ..models.Users import Users
from ..models.Roles import Roles
from rest_framework import serializers
import hashlib

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=250)
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    rol_id = serializers.IntegerField()
    
    """ Validar existencia del usuario """
    def validate_username(self, value):
        user_data = Users.objects.filter(username=value)
            
        if user_data.__len__() > 0:                
            raise serializers.ValidationError("Usuaio ya existe")
        
        return value
    
    """ Validar existencia del rol """
    def validate_rol_id(self, value):
        rol_data = Roles.objects.filter(id=value)
            
        if rol_data.__len__() == 0:                
            raise serializers.ValidationError("Rol no existe")
        
        return value
    
    def create(self, validated_data):
        validated_data["password"] = hashlib.md5(validated_data["password"].encode()).hexdigest()
        user = Users.objects.create(**validated_data)
        
        return user
    
    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'firstname', 'lastname']