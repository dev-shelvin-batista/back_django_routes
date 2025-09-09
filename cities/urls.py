from django.contrib import admin
from django.urls import path
from .views.CitiesView import CitiesView

urlpatterns = [
    path('', CitiesView.as_view()),
]