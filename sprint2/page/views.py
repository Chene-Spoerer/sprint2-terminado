from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import *
from django.db.models import Count
# Create your views here.
# Aqui es donde se relacionan los templates con las urls


# @login_required sirve para que los usuarios no puedan ingresar a esta pagina si esque no estan logueados:
# https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page

# wea q se veia interesante por no la lei:
# https://dev.to/zachtylr21/model-inheritance-in-django-m0j


@login_required(login_url='/login')
def entrevistas(request):
    reuniones_user = Reunion.objects.filter(empresa=request.user)
    pendientes = Reunion.objects.filter(empresa=request.user, status='Pendiente').count()
    entrevistados = Reunion.objects.filter(empresa=request.user, status='Entrevistado/a').count()
    evaluados = Reunion.objects.filter(empresa=request.user, status='Evaluado/a')    
    context = { 'reuniones_user':reuniones_user, 'pendientes': pendientes, 
    'entrevistados':entrevistados}
    return render(request, 'page/entrevistas.html', context)

@login_required(login_url='/login')
def puestos(request):
    user = Reunion.objects.filter(empresa=request.user)
    puestos = Puesto_trabajo.objects.filter(empresa=request.user)
    context = { 'puestos':puestos}
    return render(request, 'page/puestos.html', context)
    
@login_required(login_url='/login')
def calendario(request):
    return render(request, 'page/calendario.html')

def contacto(request):  
    return render(request, 'page/contacto.html')

def inicio(request):
    return render(request, 'page/inicio.html')