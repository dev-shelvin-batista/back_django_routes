from django.contrib import admin
from django.urls import path
from .views.StopsView import StopsView

urlpatterns = [
    path('', StopsView.as_view()),
]