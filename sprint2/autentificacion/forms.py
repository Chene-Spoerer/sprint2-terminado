from django.contrib.auth.forms import UserCreationForm
from usuarios.models import User, Empresa
from django.db import transaction
from django.forms import ModelForm
from django import forms

class RegistroEmpresaForm(UserCreationForm):

    # Unica forma que se de traducir password a contraseña: (y elminar password1 y 2 de class Meta)

    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['nombre_empresa','email','password1', 'password2', 'about']
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_empresa = True
        user.save()
        empresa = Empresa.objects.create(user=user)
        empresa.save()
        return user, empresa
    

class RegistroPostulante(UserCreationForm.Meta):

    nombre = forms.CharField(label='nombre',required=True)

    class Meta:
        model = User
        fields = ['nombre']