from django.forms import ModelForm
from .models import Tarea

class TareaForm(ModelForm):
    model = Tarea
    fields = ['descripcion', 'fecha']
    
