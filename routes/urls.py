from django.contrib import admin
from django.urls import path
from .views.RoutesView import RoutesView
from .views.SchedulesRouteView import SchedulesRouteView
from .views.ListSchedulesByRouteView import ListSchedulesByRouteView
from .views.ListSchedulesStopsByRouteView import ListSchedulesStopsByRouteView

urlpatterns = [
    path('', RoutesView.as_view()),
    path('schedule/<int:route_id>/add-stop/', SchedulesRouteView.as_view()),
    path('schedule/<int:route_id>/', ListSchedulesByRouteView.as_view()),
    path('schedule/<int:route_id>/stops/', ListSchedulesStopsByRouteView.as_view()),
]