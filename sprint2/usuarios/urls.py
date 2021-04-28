from django.urls import path
from . import views

# URLS de la app usuarios

urlpatterns = [
    path('perfil/', views.perfil),
]