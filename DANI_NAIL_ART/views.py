from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Agendar_Cita
from .forms import Agendar_Citas

def InicioSeccion( request ):
    return render( request, 'Login/iniciar_seccion.html')

def registrar( request ):
    return render(request, 'Register/registrarse.html')

def servicios(request):
    return render(request, 'Servicios/servicios.html')

def Citas(request):
    Citas_Agendadas = 'citas'
    citas = Agendar_Cita.objects.all()
    return render(request, 'Agendar_Cita/Citas_Agendadas.html',{
        'title':Citas_Agendadas,
        'citas':citas,
    })

# def Agendar_Citas(request):
#     if request.method == 'GET':
#         return render(request, 'Agendar_Cita/agendar.html', {
#             'form': Agendar_Cita(),
#         })
#     else:
#         form = Agendar_Citas(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data['nombre']
#             tipoServicio = form.cleaned_data['tipoServicio']
#             fecha_hora = form.cleaned_data['fecha_hora']
#             Agendar_Cita.objects.create()

def Agendar_Citas(request):
    if request.method == 'POST':
        form = Agendar_Cita(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            tipoServicio = form.cleaned_data['tipoServicio']
            fecha_hora = form.cleaned_data['fecha_hora']
            # Crea una instancia del modelo Cita y guárdala en la base de datos
            cita = Citas(nombre=nombre, tipoServicio=tipoServicio, fecha_hora=fecha_hora)
            cita.save()
            return redirect('listar_citas')  # Redirige a la página de listado de citas o la que desees
    else:
        form = Agendar_Cita()

    return render(request, 'Agendar_Cita/agendar.html', {'form': form})


# Create your views here.