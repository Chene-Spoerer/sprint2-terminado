from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import *
from .forms import *

# Create your views here.

# Para la vista general en template entrevistas:
# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def entrevistas(request):
    entrevistas_user = Entrevista.objects.filter(empresa=request.user)
    pendientes = Entrevista.objects.filter(empresa=request.user, status='Pendiente').count()
    entrevistados = Entrevista.objects.filter(empresa=request.user, status='Entrevistado/a').count()

    # Contexto de las variables para el template
    context = { 'entrevistas_user':entrevistas_user, 'pendientes': pendientes, 
    'entrevistados':entrevistados}
    return render(request, 'entrevistas/entrevistas.html', context)


# Para la vista especifica de una entrevista
# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def entrevista(request, pk):
    entrevista  = Entrevista.objects.get(id=pk)

    # Contexto de las variables para el template
    context = { 'entrevista':entrevista, }
    return render(request, 'entrevistas/entrevista.html', context)

def crear_postulante(request):
    if request.method == 'POST':
        form = PostulanteForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = request.POST.get('nombre_postulante')
            messages.success(request, f'Postulante creado exitosamente')
            return redirect('/crear_entrevista')
    else:
        form = PostulanteForm()
    return render(request, 'entrevistas/crear_entrevista.html', {'form': form})

def crear_entrevista(request):
    form = EntrevistaForm
    context = {'form':form,}
    return render(request, 'entrevistas/crear_entrevista.html', context=context)

# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def puestos(request):
    user = Entrevista.objects.filter(empresa=request.user)
    puestos = Puesto_trabajo.objects.filter(empresa=request.user)
    context = { 'puestos':puestos}
    return render(request, 'entrevistas/puestos.html', context)