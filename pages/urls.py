from django.urls import path
#Importamos todas las vistas de nuestra App Core 
from . import views

urlpatterns = [ 
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]