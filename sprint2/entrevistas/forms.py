from django.forms import ModelForm, DateTimeField
from .models import *

class EntrevistaForm(ModelForm):
    Entrevista.fecha_entrevista = DateTimeField()
    class Meta:
        model = Entrevista
        fields = ['nombre_postulante', 'email', 'fecha_entrevista', 'puesto_trabajo']
    
#    def __init__(self, *args, **kwargs):
#        super(EntrevistaForm, self).__init__(*args, **kwargs)
#        self.fields['puesto_trabajo'].queryset = user.puesto_trabajo_set()



class CVform(ModelForm):
    class Meta:
        model = Cv
        fields = ['cv']
