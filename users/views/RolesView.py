from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from ..models.Roles import Roles
from ..serializers.ListRolesSerializer import ListRolesSerializer

class RolesView(APIView):
    
    """ 
        Rest API to obtain registered roles
        
        Returns role data for users
        
        Rol -> N/A
    """
    def get(self, request):
        response = dict()

        queryset = Roles.objects.all().order_by('description')
        serializer = ListRolesSerializer(queryset, many=True)
        response["data"] = serializer.data
        return JsonResponse(status=status.HTTP_200_OK, data=response)