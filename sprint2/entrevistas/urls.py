from django.urls import path
from . import views

# URLS de la app account

urlpatterns = [
    path('entrevistas/', views.entrevistas), # vista general
    path('entrevista/<str:pk>/', views.entrevista, name='entrevista'), # vista especifica
    path('puestos/', views.puestos),
    path('crear_entrevista/', views.crear_entrevista, name='crear_entrevista'),

]