from django.urls import path
from .views import dashboard_view, overview_view, water_view, soil_view

urlpatterns = [
    path('', dashboard_view, name='air'),
    path('overview/', overview_view, name='overview'),
    path('water/', water_view, name='water'),
    path('soil/', soil_view, name='soil'),
]