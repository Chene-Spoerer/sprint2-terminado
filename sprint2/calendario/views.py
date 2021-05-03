from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import *
from entrevistas.models import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class calendario(LoginRequiredMixin,ListView):
    model = Entrevista
    template_name = 'calendario/calendario.html'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(empresa=self.request.user)
        return queryset


#@login_required(login_url='/login')
#def calendario(request):
#    return render(request, 'calendario/calendario.html')