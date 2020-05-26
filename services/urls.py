from django.urls import path
#Importamos todas las vistas de nuestra App Core 
from . import views

urlpatterns = [
    path('', views.services, name="services"), 
]