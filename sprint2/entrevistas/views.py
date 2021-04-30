from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage

# Create your views here.


############################################################################################################################################################################

# Para la vista general en template -> entrevistas:
# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def entrevistas(request):
    entrevistas_user = Entrevista.objects.filter(empresa=request.user)
    pendientes = Entrevista.objects.filter(
        empresa=request.user, status='Pendiente').count()
    entrevistados = Entrevista.objects.filter(
        empresa=request.user, status='Entrevistado/a').count()

    # Contexto de las variables para el template
    context = {'entrevistas_user': entrevistas_user, 'pendientes': pendientes,
               'entrevistados': entrevistados}
    return render(request, 'entrevistas/entrevistas.html', context)


############################################################################################################################################################################

# Para la vista especifica de una entrevista --> entrevista/id_de_la_entrevista (dinamica)
# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def entrevista(request, pk):
    entrevista = Entrevista.objects.get(id=pk)
    form = entrevista.cv

# Formulario para agrgar archivos al field cv de Entrevista del usuario que esta logueado actualmente
# ESTA LOGICA FUNCIONA PERO NO ES MUY EFICIENTE | REVISAR - ENCONTRAR OTRA FORMA, sino...fue xd:

    # if no tiene cv mostramos CVform en la pagina:
    if entrevista.cv == None:
        # Como Entrevista.objects.filter(empresa=request.user) retorna una queryset de 1 elemento debemos "recorrerlo", debe haber otra forma pero no me la se
        for usuario in Entrevista.objects.filter(id=pk):
            if request.method == 'POST':
                form = CVform(request.POST, request.FILES)
                if form.is_valid():
                    cv = form.save()
                    usuario.cv = cv
                    usuario.save()
                    return redirect('/entrevista/%s' % pk)
            else:
                form = CVform()
            return render(request, 'entrevistas/entrevista.html', {'entrevista': entrevista, 'form': form})
    # if tiene cv mostramos el nombre del cv:
    else:
        return render(request, 'entrevistas/entrevista.html', {'entrevista': entrevista, 'form': form})


############################################################################################################################################################################

# Para crear una entrevista:
# class crear_entrevista(FormView):
#    template_name = 'crear_entrevista.html'
#    form_class = EntrevistaForm
#    succes_url = '/entrevistas/'
#
#    def form_valid(self, form):
#        print(form.cleaned_data)
#        return super().form_valid(form)
#
#    def get_form_kwargs(self):
#        kwargs = super(crear_entrevista, self).get_form_kwargs()
#        kwargs['empresa'] = self.request.user
#        return kwargs


def crear_entrevista(request):
    if request.method == 'POST':
        form = EntrevistaForm(request.POST)
        # Como Entrevista.objects.filter(empresa=request.user) retorna una queryset de 1 elemento debemos "recorrerlo", debe haber otra forma pero no me la se
        for usuario in User.objects.filter(nombre_empresa=request.user.nombre_empresa):
            if form.is_valid():
                entrevista = form.save(commit=False)
                entrevista.empresa = usuario
                entrevista.status = 'Pendiente'
                entrevista.save()
                messages.success(request, f'Entrevista creada exitosamente')
                return redirect('/entrevistas')
    else:
        form = EntrevistaForm()
    return render(request, 'entrevistas/crear_entrevista.html', {'form': form})


############################################################################################################################################################################

# https://youtu.be/7a23TbUXfWE :
@login_required(login_url='/login')
def puestos(request):
    user = Entrevista.objects.filter(empresa=request.user)
    puestos = Puesto_trabajo.objects.filter(empresa=request.user)
    context = {'puestos': puestos}
    return render(request, 'entrevistas/puestos.html', context)
