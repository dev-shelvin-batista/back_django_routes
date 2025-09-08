from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from ..serializers.ListUsersSerializer import ListUsersSerializer
import hashlib

class LoginUserView(APIView):
    """ 
        API rest de Login.
        
        Retorna los datos de la sesion del usuario o un error si el usuario y/o contraseña son incorrectos
        
        Rol -> No Aplica
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}  
        
        serializer = ListUsersSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            data["password"] = hashlib.md5(data["password"].encode()).hexdigest()
            user = serializer.login(data["username"], data["password"])
            serializer_data = ListUsersSerializer(user, many=False)
                                  
            #encoded_jwt = jwt.encode(serializer_data.data, 'secret', algorithm='HS256')
            #response["token"] = encoded_jwt.decode()
            response["token"] = ""
            response["data"] = serializer_data.data
                        
            return JsonResponse(status=status.HTTP_200_OK, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 