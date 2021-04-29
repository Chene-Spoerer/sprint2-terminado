from django.forms import ModelForm
from .models import *

class EntrevistaForm(ModelForm):
    class Meta:
        model = Entrevista
        fields = '__all__'
