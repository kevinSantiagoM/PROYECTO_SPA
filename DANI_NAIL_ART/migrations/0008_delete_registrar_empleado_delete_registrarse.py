# Generated by Django 4.2.5 on 2023-09-21 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DANI_NAIL_ART', '0007_agendar_cita_delete_cita'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registrar_Empleado',
        ),
        migrations.DeleteModel(
            name='registrarse',
        ),
    ]
