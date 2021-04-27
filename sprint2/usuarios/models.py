from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_empresa = models.BooleanField(default=False)
    is_postulante = models.BooleanField(default=False)
    nombre = models.CharField(max_length=200)

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Postulante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Puesto_trabajo(models.Model):
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

class Reunion(models.Model):
    fecha_reunion = models.DateTimeField(blank=True, null=True)
    postulante = models.OneToOneField(Postulante, on_delete=models.CASCADE)
    puesto_trabajo = models.ForeignKey(Puesto_trabajo, on_delete=models.CASCADE, related_name='puesto_trabajo')
    # cv = models.FileField(upload_to='cv/') # Configurar esta wea q no entendi https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html