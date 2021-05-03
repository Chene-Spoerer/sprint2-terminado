from django.forms import ModelForm, DateTimeField
from django.forms.widgets import DateTimeInput
from .models import *


class EntrevistaForm(ModelForm):

    # Agregar place holder pa no olvidar el formato del input
    fecha_entrevista = DateTimeField(widget=DateTimeInput(attrs={'placeholder':"YYYY-MM-DD HH:MM:SS"}))

    class Meta:
        model = Entrevista
        fields = ['nombre_postulante', 'email',
                  'fecha_entrevista', 'puesto_trabajo']


# Limitar opciones de puesto trabajo y el input del tiempo que sea con un calendario o algo
#    def __init__(self, *args, **kwargs):
#        super(EntrevistaForm, self).__init__(*args, **kwargs)
#        self.fields['puesto_trabajo'].queryset = user.puesto_trabajo_set()
#        self.fields['fecha_entrevista'].widget = SplitHiddenDateTimeWidget()


# Para agregar cv a la entrevista ya existente
class CVform(ModelForm):
    class Meta:
        model = CVfield
        fields = ['cv']


# Para agregar un puesto de trabajo
class PuestoForm(ModelForm):

    class Meta:
        model = Puesto_trabajo
        fields = ['titulo', 'descripcion']
