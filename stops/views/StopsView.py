from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from django.http import HttpResponse
from ..models.Stops import Stops
from ..serializers.StopsSerializer import StopsSerializer
from ..serializers.ListStopsSerializer import ListStopsSerializer

class StopsView(APIView):
    """ 
        Rest API to obtain registered stops
        
        Returns the stop data
        
        Rol -> Operador logístico / Pasajero
    """
    def get(self, request):
        response = dict()    
        data = dict()    
        
        queryset = Stops.objects.all().order_by('id')
        serializer = ListStopsSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    
    """ 
        Rest API for registering a stop
        
        Returns the data for the recorded stop or an error.
        
        Rol -> Operador logístico
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}        
                
        serializer = StopsSerializer(data=data)
        """ The creation operation is validated if there are no errors. If there are errors, it returns """
        if serializer.is_valid(raise_exception=False):
            stop = serializer.create(serializer.data)
            serializer_data = ListStopsSerializer(stop, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)