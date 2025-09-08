from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from ..serializers.UserSerializer import UserSerializer
from ..serializers.ListUsersSerializer import ListUsersSerializer

class RegisterUserView(APIView):
    """ 
        API rest de registro del usuario.
        
        Retorna los datos del usuario creado o un error 
        
        Rol -> No Aplica
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}
        
        serializer = UserSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            
            usuario = serializer.create(serializer.data)
            serializer_data = ListUsersSerializer(usuario, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)  