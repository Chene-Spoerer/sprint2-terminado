from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# URLS de la app account

urlpatterns = [
    path('register/', views.register),
    path('login/', auth_views.LoginView.as_view(template_name='autentificacion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='autentificacion/logout.html'), name='logout'),
]