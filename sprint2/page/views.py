from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import *
from django.db.models import Count
# Create your views here.
# Aqui es donde se relacionan los templates con las urls


# @login_required sirve para que los usuarios no puedan ingresar a esta pagina si esque no estan logueados:
# https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page

# revisar ? https://dev.to/zachtylr21/model-inheritance-in-django-m0j

    
@login_required(login_url='/login')
def calendario(request):
    return render(request, 'page/calendario.html')

def contacto(request):  
    return render(request, 'page/contacto.html')

def inicio(request):
    return render(request, 'page/inicio.html')