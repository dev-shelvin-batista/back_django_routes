from ..models.Users import Users
from ..models.Roles import Roles
from rest_framework import serializers
from .ListRolesSerializer import ListRolesSerializer

class ListUsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=250)
    firstname = serializers.CharField(max_length=200, required=False)
    lastname = serializers.CharField(max_length=200, required=False)
    rol = ListRolesSerializer(required=False)
    
    """ Method that allows you to validate whether a user exists by comparing the username and password with the data sent by the user. """
    def login(self, username, password):
        user_data = Users.objects.filter(username=username, password=password)
        
        # Validate the user's existence
        if user_data.__len__() == 0:                
            raise serializers.ValidationError("User does not exist")
        
        return user_data.first()
    
    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'firstname', 'lastname', 'rol']