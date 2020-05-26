from django.urls import path
#Importamos todas las vistas de nuestra App Core 
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),  
    path('category/<int:category_id>/', views.category, name="category"),
]