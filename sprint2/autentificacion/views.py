from django.shortcuts import render, redirect
from .forms import RegistroEmpresaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# https://youtu.be/TBGRYkzXiTg
# https://youtu.be/q4jPR-M0TAQ


def register(request):

    if request.method == 'POST':
        form = RegistroEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Cuenta creada exitosamente, ahora puedes iniciar sesion!')
            return redirect('/login')
    else:
        form = RegistroEmpresaForm()
    return render(request, 'autentificacion/register.html', {'form': form})


def iniciar_sesion(request):
    return render(request, 'autentificacion/login.html')
