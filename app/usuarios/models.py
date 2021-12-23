from django.db import models
from django.utils import timezone


# Create your models here.
"""class Usuarios(models.Model):

    nombre         = models.CharField('Nombre', max_length=100, null=False, blank=False)
    apellido       = models.CharField('Apellido', max_length=100, null=False, blank=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    correo         = models.EmailField('Correo electrónico', null=False, blank=False)
    contrasena     = models.CharField(max_length=50)

    class Meta:
        ordering = ("fecha_registro",)
    
    def __str__(self) -> str:
        return str(self.nombre)"""
