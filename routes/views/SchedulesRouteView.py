from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..serializers.SchedulesRouteSerializer import SchedulesRouteSerializer
from ..serializers.ListSchedulesRouteSerializer import ListSchedulesRouteSerializer

class SchedulesRouteView(APIView):
    """ 
        API rest de asignar una parada a una ruta en un horario
        
        Retorna los datos del horario establecido en la ruta o un error 
        
        Rol -> Operador logístico
    """
    def post(self, request, route_id):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}     
        
        data["route_id"] = route_id
        
        serializer = SchedulesRouteSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            schedule = serializer.create(serializer.data)
            serializer_data = ListSchedulesRouteSerializer(schedule, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)