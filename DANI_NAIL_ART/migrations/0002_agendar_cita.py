# Generated by Django 4.2.5 on 2023-09-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DANI_NAIL_ART', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendar_Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipoServicio', models.CharField(choices=[('manicure semipermanente', 'Manicure Semipermanente'), ('pedicure semipermanente', 'Pedicure Semipermanente'), ('uñas en polygel', 'Uñas en Poligel')], max_length=50)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]