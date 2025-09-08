from django.db import models
from .Roles import Roles

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=250)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    rol = models.ForeignKey(Roles, on_delete = models.CASCADE)

    class Meta:
        db_table = "users"