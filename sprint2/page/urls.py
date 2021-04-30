from django.urls import path
from . import views

# URLS de la app account

urlpatterns = [
    path('', views.inicio),
    path('contacto/', views.contacto),
    path('calendario/', views.calendario),
]
