from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Dispositivo, Sensor, TipoSensor, Actuador, TipoActuador, PublicacionSensor, PublicacionActuador
from django.urls import reverse
from django.contrib import messages  
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

#=================================== SENSOR ===========================================

class SensorListado(ListView): 
    model = Sensor 
    
class SensorCrear(SuccessMessageMixin, CreateView): 
    model = Sensor
    form = Sensor
    fields = "__all__"
    success_message = 'Sensor Creado Correctamente !'

    def get_success_url(self):
        return reverse('leerSensor')
    
class SensorDetalle(DetailView): 
    model = Sensor
    
class SensorActualizar(SuccessMessageMixin, UpdateView): 
    model = Sensor
    form = Sensor
    fields = "__all__" 
    success_message = 'Sensor Actualizado Correctamente !'
 
    def get_success_url(self):
        return reverse('leerSensor')

class SensorEliminar(SuccessMessageMixin, DeleteView): 
    model = Sensor 
    form = Sensor
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Sensor Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerSensor')
    
