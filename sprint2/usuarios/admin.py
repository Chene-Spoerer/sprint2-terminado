from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'nombre_empresa')
    list_filter = ('nombre_empresa',)
    ordering = ('-start_date',)
    list_display = ('email', 'nombre_empresa',
                    'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'nombre_empresa',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about','logo')}),
    )
    
# admin.site.register(User, UserAdminConfig)
admin.site.register(User)
admin.site.register(Empresa)
admin.site.register(Puesto_trabajo)
admin.site.register(Entrevista)
admin.site.register(Postulante)