from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, nombre_empresa, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True')
            
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_staff=True')

        return self.create_user(email, nombre_empresa, password, **other_fields)    


    def create_user(self, email, nombre_empresa, password, **other_fields):

        # validacion
        if not email:
            raise ValueError(_('Debe ingresar correo electrónico'))

        # asignacion
        email = self.normalize_email(email)
        user = self.model(email=email, nombre_empresa=nombre_empresa, **other_fields)
        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Correo electrónico'), unique=True)
    nombre_empresa = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    logo = models.ImageField(null=True, blank=True)

    # weas
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_empresa',]

    def __str__(self):
        return self.nombre_empresa

# class User(AbstractUser):
#    is_empresa = models.BooleanField(default=False)
#    is_postulante = models.BooleanField(default=False)
#    nombre = models.CharField(max_length=200)


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