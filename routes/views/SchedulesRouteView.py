from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..serializers.SchedulesRouteSerializer import SchedulesRouteSerializer
from ..serializers.ListSchedulesRouteSerializer import ListSchedulesRouteSerializer

class SchedulesRouteView(APIView):
    """ 
        Rest API to assign a stop to a route in a schedule
        
        Returns the schedule data established on the route or an error. 
        
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
        """ The creation operation is validated if there are no errors. If there are errors, it returns """
        if serializer.is_valid(raise_exception=False):
            schedule = serializer.create(serializer.data)
            serializer_data = ListSchedulesRouteSerializer(schedule, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)