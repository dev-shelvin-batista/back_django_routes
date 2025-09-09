from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..models.Schedules import Schedules
from ..serializers.ListSchedulesStopsByRouteSerializer import ListSchedulesStopsByRouteSerializer
from stops.serializers.ListStopsSerializer import ListStopsSerializer

class ListSchedulesStopsByRouteView(APIView):
    """ 
        REST API to obtain the stops on a route
        
        Returns data about stops along a route or an error. 
        
        Rol -> Operador logístico / Pasajero
    """
    def get(self, request, route_id):
        response = dict()    
        data = dict()    
        
        serializer = ListSchedulesStopsByRouteSerializer(data=data)
        stops = serializer.list_stops(route_id)
        serializer = ListStopsSerializer(stops, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)