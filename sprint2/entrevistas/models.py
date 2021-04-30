from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from usuarios.models import User, NombreField

# Create your models here.

############################################################################################################################################################################


class Puesto_trabajo(models.Model):
    empresa = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.titulo

############################################################################################################################################################################


class CVfield(models.Model):
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

############################################################################################################################################################################


class Entrevista(models.Model):
    STATUS = (
        ('Pendiente', 'Pendiente'),
        ('Entrevistado/a', 'Entrevistado/a'),
        ('Evaluado/a', 'Evaluado/a')
    )
    # DATOS DEL POSTULANTE:
    nombre_postulante = NombreField(
        _('Nombre del postulante'), blank=True, null=True)
    email = models.EmailField(_('Correo electrónico'), max_length=254)
    fecha_ingresado = models.DateTimeField(auto_now_add=True)
    # Configurar esta wea q no entendi https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
    cv = models.OneToOneField(
        CVfield, on_delete=models.CASCADE, blank=True, null=True)

    # DATOS DE LA ENTREVISTA
    empresa = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fecha_entrevista = models.DateTimeField(blank=True, null=True)
    puesto_trabajo = models.ForeignKey(
        Puesto_trabajo, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default='Pendiente')

    def __str__(self):
        return 'Entrevista con {} por el puesto {}'.format(self.nombre_postulante, self.puesto_trabajo)

# Postulante debe ser un usuario?
# class Postulante(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
