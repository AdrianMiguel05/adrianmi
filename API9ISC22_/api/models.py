from django.db import models

# Create your models here.

class Base(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)


