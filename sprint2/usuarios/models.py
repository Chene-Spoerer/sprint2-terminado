from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class NombreField(models.Field):

    description = "Nombre valido de empresa"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, str) or value is None:
            return value
        return str(value)
    
    def db_type(self, connection):
        return 'NombreField'
    
    def get_prep_value(self, value):
        return value

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    
    def __str__(self):
        return self.value

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

    email = models.EmailField(_('Correo electrónico'), max_length=254, unique=True)
    nombre_empresa = NombreField(_('Nombre de tu empresa'),unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'Cuentanos, en que consiste tu empresa'), max_length=500, blank=True)
    logo = models.ImageField(null=True, blank=True)

    # weas
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_empresa',]

    def __str__(self):
        return self.nombre_empresa

# Empresa debe existir?
#class Empresa(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)