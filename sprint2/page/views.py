from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# Aqui es donde se relacionan los templates con las urls


# @login_required sirve para que los usuarios no puedan ingresar a esta pagina si esque no estan logueados:
# https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page

# wea q se veia interesante por no la lei:
# https://dev.to/zachtylr21/model-inheritance-in-django-m0j

def inicio(request):
    return render(request, 'page/inicio.html')


# Mostrar las reuniones de la empresa (no me funciono xd)
@login_required(login_url='/login')
def entrevistas(request):
    return render(request, 'page/entrevistas.html')

@login_required(login_url='/login')
def perfil(request):
    return render(request, 'page/perfil.html')

def contacto(request):  
    return render(request, 'page/contacto.html')