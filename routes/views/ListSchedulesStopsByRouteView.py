from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..models.Schedules import Schedules
from ..serializers.ListSchedulesStopsByRouteSerializer import ListSchedulesStopsByRouteSerializer
from stops.serializers.ListStopsSerializer import ListStopsSerializer

class ListSchedulesStopsByRouteView(APIView):
    """ 
        API rest de obtener las paradas de una ruta
        
        Retorna los datos de las paradas de una ruta o un error 
        
        Rol -> Operador logístico o Pasajero
    """
    def get(self, request, route_id):
        response = dict()    
        data = dict()    
        
        serializer = ListSchedulesStopsByRouteSerializer(data=data)
        stops = serializer.list_stops(route_id)
        serializer = ListStopsSerializer(stops, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)