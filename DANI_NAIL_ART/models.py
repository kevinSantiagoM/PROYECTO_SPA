from django.db import models

class Registrar_Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=120)
    rol = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nombre
    

class registrarse(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.PositiveIntegerField(max_length=10)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=150)

#     def __str__(self) -> str:
#         return super().__str__()
    
# class Iniciar_Seccion(models.Model):
#     correo = models.EmailField(100)
#     contraseña = models.CharField(max_length=120)

# class Agendar_Cita(models.Model):
#     nombre = models.CharField(max_length=100)
#     telefono = models.CharField(max_length=20)
#     fecha = models.DateTimeField()
#     def __str__(self) -> str:
#         return self.nombre

class Agendar_Cita(models.Model):
    Servicios_Ofrecer = (
        ('manicure semipermanente', 'Manicure Semipermanente'),
        ('pedicure semipermanente', 'Pedicure Semipermanente'),
        ('uñas en polygel', 'Uñas en PolYgel')
    )
    nombre = models.CharField(max_length=100)
    tipoServicio = models.CharField(max_length=50, choices=Servicios_Ofrecer)
    fecha = models.DateTimeField()

    def __str__(self) -> str:
        return self.nombre


# Create your models here.
