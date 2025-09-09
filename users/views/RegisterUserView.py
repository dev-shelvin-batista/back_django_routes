from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from ..serializers.UserSerializer import UserSerializer
from ..serializers.ListUsersSerializer import ListUsersSerializer

class RegisterUserView(APIView):
    """ 
        REST API for user registration.
        
        Returns the data of the created user or an error 
        
        Rol -> N/A
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
        
        serializer = UserSerializer(data=data)
        """ The creation operation is validated if there are no errors. If there are errors, it returns """
        if serializer.is_valid(raise_exception=False):
            
            usuario = serializer.create(serializer.data)
            serializer_data = ListUsersSerializer(usuario, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)  