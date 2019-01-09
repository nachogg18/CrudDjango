from django.db import models
'''from django.forms import ModelForm'''

# Create your models here.

class Tarea(models.Model):
    descripcion = models.TextField()

    fecha = models.DateField()

    asignado_a = models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse('/gestor/Tarea_edit', kwargs={'pk': self.pk})


'''class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'fecha']
'''