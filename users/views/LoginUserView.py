from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from ..serializers.ListUsersSerializer import ListUsersSerializer
import hashlib
import jwt

class LoginUserView(APIView):
    """ 
        REST API for login.
        
        Returns the user's session data or an error if the username and/or password are incorrect.
        
        Rol -> N/A
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}  
        
        serializer = ListUsersSerializer(data=data)
        """ The creation operation is validated if there are no errors. If there are errors, it returns """
        if serializer.is_valid(raise_exception=False):
            data["password"] = hashlib.md5(data["password"].encode()).hexdigest()
            user = serializer.login(data["username"], data["password"])
            serializer_data = ListUsersSerializer(user, many=False)
                                  
            encoded_jwt = jwt.encode(serializer_data.data, 'secret', algorithm='HS256')
            response["token"] = encoded_jwt.decode()
            response["data"] = serializer_data.data
                        
            return JsonResponse(status=status.HTTP_200_OK, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response) 