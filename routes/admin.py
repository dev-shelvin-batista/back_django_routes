from django.contrib import admin
from .models.Routes import Routes
from .models.Schedules import Schedules

# Register your models here.
admin.site.register(Routes)
admin.site.register(Schedules)