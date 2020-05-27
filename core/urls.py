from django.urls import path
#Importamos todas las vistas de nuestra App Core 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
]