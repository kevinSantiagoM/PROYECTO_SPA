# Generated by Django 4.2.5 on 2023-09-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrar_Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=120)),
                ('rol', models.CharField(max_length=150)),
            ],
        ),
    ]