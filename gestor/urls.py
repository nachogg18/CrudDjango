from django.urls import path

from . import views

urlpatterns = [
    path('', views.TareaList.as_view(), name='tarea_list'),
    path('view/<int:pk>', views.TareaView.as_view(), name='tarea_view'),
    path('new', views.TareaCreate.as_view(), name='tarea_new'),
    path('view/<int:pk>', views.TareaView.as_view(), name='tarea_view'),
    path('edit/<int:pk>', views.TareaUpdate.as_view(), name='tarea_edit'),
    path('delete/<int:pk>', views.TareaDelete.as_view(), name='tarea_delete'),
]




'''
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.tarea_list,name='/gestor/tarea_list'),
    path('/<id>/modificar',views.get_tarea,name='/gestor/tarea_form'),
]
'''