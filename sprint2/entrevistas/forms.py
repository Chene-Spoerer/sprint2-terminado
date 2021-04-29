from django.forms import ModelForm
from usuarios.models import *

class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'

class EntrevistaForm(ModelForm):
    class Meta:
        model = Entrevista
        fields = ['fecha_entrevista', 'postulante', 'puesto_trabajo']
