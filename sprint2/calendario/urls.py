from django.urls import path
from . import views

# URLS de la app account

urlpatterns = [
    path('calendario/', views.calendario.as_view()),

]