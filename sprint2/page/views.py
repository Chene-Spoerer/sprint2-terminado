from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import *
from django.db.models import Count
# Create your views here.
# Aqui es donde se relacionan los templates con las urls


# @login_required sirve para que los usuarios no puedan ingresar a esta pagina si esque no estan logueados:
# https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page

# revisar ? https://dev.to/zachtylr21/model-inheritance-in-django-m0j



# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def entrevistas(request):
    entrevistas_user = Entrevista.objects.filter(empresa=request.user)
    pendientes = Entrevista.objects.filter(empresa=request.user, status='Pendiente').count()
    entrevistados = Entrevista.objects.filter(empresa=request.user, status='Entrevistado/a').count()   
    context = { 'entrevistas_user':entrevistas_user, 'pendientes': pendientes, 
    'entrevistados':entrevistados}
    return render(request, 'page/entrevistas.html', context)

# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def puestos(request):
    user = Entrevista.objects.filter(empresa=request.user)
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