# Generated by Django 3.2 on 2021-04-28 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usuarios.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('nombre_empresa', usuarios.models.NombreField(max_length=100, unique=True, verbose_name='Nombre de tu empresa')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='Cuentanos, en que consiste tu empresa')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_postulante', usuarios.models.NombreField(blank=True, max_length=100, null=True, verbose_name='Nombre del postulante')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('fecha_ingresado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto_trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reunion', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Entrevistado/a', 'Entrevistado/a'), ('Evaluado/a', 'Evaluado/a')], max_length=200, null=True)),
                ('postulante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.postulante')),
                ('puesto_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puesto_trabajoReu', to='usuarios.puesto_trabajo')),
            ],
        ),
        migrations.AddField(
            model_name='postulante',
            name='puesto_trabajo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='puesto_trabajoPost', to='usuarios.puesto_trabajo'),
        ),
    ]
