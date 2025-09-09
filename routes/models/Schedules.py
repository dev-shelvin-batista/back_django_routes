from django.db import models
from .Routes import Routes
from stops.models.Stops import Stops

class Schedules(models.Model):
    id = models.AutoField(primary_key=True)
    weekday = models.IntegerField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop = models.ForeignKey(Stops, on_delete = models.CASCADE)
    route = models.ForeignKey(Routes, on_delete = models.CASCADE)

    class Meta:
        db_table = "schedules"
