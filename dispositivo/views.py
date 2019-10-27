from django.views.generic import ListView, DetailView , TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Dispositivo, Sensor, TipoSensor, Actuador, TipoActuador, PublicacionSensor, PublicacionActuador
from django.urls import reverse
from django.contrib import messages  
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

#=================================== SENSOR ===========================================

class SensorListado(ListView): 
    model = Sensor
    
class SensorMonitorr(ListView): 
    model = Sensor 
    
    
class SensorMonitor(TemplateView):
    #template_name = 'agenda/index.html'

    def get_context_data(self, *args, **kwargs):
        sensores = Sensor.objects.all()
        actuadores = Actuador.objects.all()
        return {'sensores': sensores, 'actuadores': actuadores}
    
    
    
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
    
