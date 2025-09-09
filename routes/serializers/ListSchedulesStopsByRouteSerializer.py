from rest_framework import serializers
from stops.models.Stops import Stops

class ListSchedulesStopsByRouteSerializer(serializers.Serializer):

    """ Method for listing all stops assigned to a route """
    def list_stops(self, route_id):
        list_data = Stops.objects.raw(f'''select 
            st.*
            from schedules s 
            inner join stops st on st.id = s.stop_id 
            inner join routes r on r.id = s.route_id
            where s.route_id = {route_id}
            group by s.route_id, st.id''')
        return list_data