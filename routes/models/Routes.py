from django.db import models

class Routes(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)

    class Meta:
        db_table = "routes"
