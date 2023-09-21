from django import forms
from .models import Agendar_Cita

class Agendar_Citas(forms.Form):
    Servicios_Ofrecer = (
        ('manicure semipermanente', 'Manicure Semipermanente'),
        ('pedicure semipermanente', 'Pedicure Semipermanente'),
        ('uñas en polygel', 'Uñas en Polygel')
    )
    nombre = forms.CharField(max_length=100)
    tipoServicio = forms.ChoiceField(choices=Servicios_Ofrecer, widget=forms.Select)
    fecha_hora = forms.DateTimeField()
