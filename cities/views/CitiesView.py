from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..models.Cities import Cities
from ..serializers.ListCitiesSerializer import ListCitiesSerializer
from ..serializers.CitiesSerializer import CitiesSerializer

class CitiesView(APIView):
    
    """ 
        Rest API to obtain registered cities
        
        Returns data about cities.
        
        Rol -> Operador logístico / Pasajero
    """
    def get(self, request):
        response = dict()

        queryset = Cities.objects.all().order_by('description')
        serializer = ListCitiesSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    
    """ 
        Rest API to register a city. 
        
        Returns the data for the registered city or an error.  
              
        Rol -> Operador logístico.
    """
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}        
                
        serializer = CitiesSerializer(data=data)
        """ The creation operation is validated if there are no errors. If there are errors, it returns """
        if serializer.is_valid(raise_exception=False):
            city = serializer.create(serializer.data)
            serializer_data = ListCitiesSerializer(city, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)