from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion = models.TextField()

    fecha = models.DateField()

    asignado_a = models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion