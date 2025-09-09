from django.contrib import admin
from .models.Roles import Roles
from .models.Users import Users

# Register your models here.
admin.site.register(Roles)
admin.site.register(Users)