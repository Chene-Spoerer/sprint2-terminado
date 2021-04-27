from django.urls import path
from . import views

# URLS de la app account

urlpatterns = [
    path('', views.inicio),
    path('entrevistas/', views.entrevistas),
    path('perfil/', views.perfil),
    path('contacto/', views.contacto),
]