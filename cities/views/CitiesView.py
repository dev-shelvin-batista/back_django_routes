from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status
from ..models.Cities import Cities
from ..serializers.ListCitiesSerializer import ListCitiesSerializer
from ..serializers.CitiesSerializer import CitiesSerializer

class CitiesView(APIView):
    
    def get(self, request):
        response = dict()

        queryset = Cities.objects.all().order_by('description')
        serializer = ListCitiesSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)
    
    def post(self, request):
        response = dict()
        
        if request.body:            
            data = json.loads(request.body)
        else:
            data = {}        
                
        serializer = CitiesSerializer(data=data)
        """ Se valida si no hay errores la operacion de crear. Si hay errores, se retorna """
        if serializer.is_valid(raise_exception=False):
            city = serializer.create(serializer.data)
            serializer_data = ListCitiesSerializer(city, many=False)
            
            response["data"] = serializer_data.data
            return JsonResponse(status=status.HTTP_201_CREATED, data=response)
        else:
            response["errors"] = serializer.errors
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data=response)