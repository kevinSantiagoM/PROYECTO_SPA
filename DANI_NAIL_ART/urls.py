from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioSeccion, name='InicioSeccion'),
    path('registrar', views.registrar, name='registrar'),
    path('Servicios', views.servicios, name='Servicios'),
    path('Agendar_Cita', views.Agendar_Citas, name='Agendar'),
    path('citas/', views.Citas, name='citas'),
]