from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..models.Schedules import Schedules
from ..serializers.ListSchedulesRouteSerializer import ListSchedulesRouteSerializer

class ListSchedulesByRouteView(APIView):
    """ 
        API rest de obtener los detalles de un ruta
        
        Retorna los datos de una ruta creada o un error 
        
        Rol -> Operador logístico o Pasajero
    """
    def get(self, request, route_id):
        response = dict()    
        data = dict()    
        
        data["route_id"] = route_id
        
        queryset = Schedules.objects.filter(**data).order_by('id')
        serializer = ListSchedulesRouteSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)