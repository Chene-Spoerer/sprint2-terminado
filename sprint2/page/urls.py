from django.urls import path
from . import views

# URLS de la app account

urlpatterns = [
    path('', views.inicio),
    path('entrevistas/', views.entrevistas),
    path('contacto/', views.contacto),
]