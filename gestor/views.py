from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tarea

class TareaList(ListView):
    model = Tarea

class TareaListForDate(ListView):
    model = Tarea

class TareaView(DetailView):
    model = Tarea

class TareaCreate(CreateView):
    model = Tarea
    fields = ['fecha', 'descripcion','asignado_a']
    success_url = reverse_lazy('tarea_list')

class TareaUpdate(UpdateView):
    model = Tarea
    fields = ['fecha', 'descripcion','asignado_a']
    success_url = reverse_lazy('tarea_list')

class TareaDelete(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tarea_list')













'''from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tarea
from .models import TareaForm

# Create your views here.

def tarea_list(request):
    import time
    tareas = Tarea.objects.all().order_by('fecha')
    fecha = time.strftime("%d/%m/%y")
    
    return render(request, 'gestor/tarea_list.html', {'tareas':tareas,'fecha':fecha})

def get_tarea(request,id):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TareaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #guarda el objeto
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TareaForm()

    return render(request, 'gestor/tarea_form.html', {'form': form})
    '''

    