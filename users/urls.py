from django.contrib import admin
from django.urls import path
from .views.RolesView import RolesView
from .views.RegisterUserView import RegisterUserView
from .views.LoginUserView import LoginUserView

urlpatterns = [
    path('roles', RolesView.as_view()),
    path('register', RegisterUserView.as_view()),
    path('login', LoginUserView.as_view()),
]