from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..models.Routes import Routes
from ..serializers.ListRoutesSerializer import ListRoutesSerializer
from ..serializers.RoutesSerializer import RoutesSerializer

class RoutesView(APIView):
    """ 
        API rest de listar los datos de las rutas ya creadas
        
        Retorna los datos de las rutas en base de datos
        
        Rol -> Operador logístico o Pasajero
    """
    def get(self, request):
        response = dict()    
        data = dict()    
        
        queryset = Routes.objects.all().order_by('id')
        serializer = ListRoutesSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    
    """ 
        API rest de registrar un ruta
        
        Retorna los datos de la ruta creada o un error 
        
        Rol -> Operador logístico
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}        
                
        serializer = RoutesSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            route = serializer.create(serializer.data)
            serializer_data = ListRoutesSerializer(route, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)