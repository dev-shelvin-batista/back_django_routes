from django.db import models
from cities.models.Cities import Cities

class Stops(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    city = models.ForeignKey(Cities, on_delete = models.CASCADE)

    class Meta:
        db_table = "stops"
