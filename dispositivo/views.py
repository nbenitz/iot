from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms.models import ModelForm

from dispositivo.models import Dispositivo, Sensor, TipoSensor, Actuador, TipoActuador, PublicacionSensor, PublicacionActuador
from dispositivo.forms import DispositivoForm
from persona.models import User
from estructura.models import UserDispositivo

# Create your views here.

# =================================== SENSOR ===========================================


class SensorListado(LoginRequiredMixin, ListView):
    model = Sensor
    extra_context = {'titulo': 'Sensor',
                     'plural': 'Sensores'}


class SensorMonitorr(LoginRequiredMixin, ListView):
    model = Sensor


class SensorMonitor(LoginRequiredMixin, TemplateView):

    def get_context_data(self, *args, **kwargs):
        sensores = Sensor.objects.all()
        actuadores = Actuador.objects.all()
        return {'sensores': sensores,
                'actuadores': actuadores}


class SensorMonitor2(TemplateView):

    def get_context_data(self, *args, **kwargs):
        sensores = Sensor.objects.all()
        actuadores = Actuador.objects.all()
        return {'sensores': sensores,
                'actuadores': actuadores}


class SensorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sensor
    form = Sensor
    fields = "__all__"
    success_message = 'Sensor Creado Correctamente !'
    extra_context = {'titulo': 'Crear Sensor'}
    

    def get_success_url(self):
        return reverse('leerSensor')


class SensorDetalle(LoginRequiredMixin, DetailView):
    model = Sensor
    extra_context = {'titulo': 'Detalles del Sensor'}


class SensorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Sensor
    form = Sensor
    fields = "__all__"
    success_message = 'Sensor Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Sensor'}

    def get_success_url(self):
        return reverse('leerSensor')


class SensorEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Sensor
    form = Sensor
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Sensor Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerSensor')

# =================================== ACTUADOR ===========================================

class ActuadorListado(LoginRequiredMixin, ListView):
    model = Actuador
    extra_context = {'titulo': 'Actuador',
                     'plural': 'Actuadores'}


class ActuadorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Actuador
    form = Actuador
    fields = "__all__"
    success_message = 'Actuador Creado Correctamente !'
    extra_context = {'titulo': 'Crear Actuador'}

    def get_success_url(self):
        return reverse('leerActuador')


class ActuadorDetalle(LoginRequiredMixin, DetailView):
    model = Actuador
    extra_context = {'titulo': 'Detalles del Actuador'}


class ActuadorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Actuador
    form = Actuador
    fields = "__all__"
    success_message = 'Actuador Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Actuador'}

    def get_success_url(self):
        return reverse('leerActuador')


class ActuadorEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Actuador
    form = Actuador
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Actuador Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerActuador')

# =================================== CONTROLADOR ===========================================

class DispositivoListado(LoginRequiredMixin, ListView):
    model = Dispositivo
    extra_context = {'titulo': 'Controlador',
                     'plural': 'Controladores'}


class DispositivoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Dispositivo
    form = Dispositivo
    fields = "__all__"
    success_message = 'Controlador Creado Correctamente !'
    extra_context = {'titulo': 'Agregar Controlador'}

    def get_success_url(self):
        return reverse('leerDispositivo')


class DispositivoDetalle(LoginRequiredMixin, DetailView):
    model = Dispositivo
    extra_context = {'titulo': 'Detalles del Controlador'}


class DispositivoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Dispositivo
    form = Dispositivo
    fields = "__all__"
    success_message = 'Controlador Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Controlador'}

    def get_success_url(self):
        return reverse('leerUserDispositivo')


class DispositivoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Dispositivo
    form = Dispositivo
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Controlador Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerDispositivo')


# =================================== TIPO SENSOR ===========================================

class TipoSensorListado(LoginRequiredMixin, ListView):
    model = TipoSensor
    extra_context = {'titulo': 'Tipo de Sensor',
                     'plural': 'Tipos de Sensores'}


class TipoSensorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TipoSensor
    form = TipoSensor
    fields = "__all__"
    success_message = 'Tipo de Sensor Creado Correctamente !'
    extra_context = {'titulo': 'Crear Tipo de Sensor'}

    def get_success_url(self):
        return reverse('leerTipoSensor')


class TipoSensorDetalle(LoginRequiredMixin, DetailView):
    model = TipoSensor
    extra_context = {'titulo': 'Detalles del Tipo de Sensor'}


class TipoSensorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TipoSensor
    form = TipoSensor
    fields = "__all__"
    success_message = 'Tipo de Sensor Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Tipo de Sensor'}

    def get_success_url(self):
        return reverse('leerTipoSensor')


class TipoSensorEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TipoSensor
    form = TipoSensor
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Tipo de Sensor Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerTipoSensor')


# =================================== TIPO ACTUADOR ===========================================

class TipoActuadorListado(LoginRequiredMixin, ListView):
    model = TipoActuador
    extra_context = {'titulo': 'Tipo de Actuador',
                     'plural': 'Tipos de Actuadores'}


class TipoActuadorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TipoActuador
    form = TipoActuador
    fields = "__all__"
    success_message = 'Tipo de Actuador Creado Correctamente !'
    extra_context = {'titulo': 'Crear Tipo de Actuador'}

    def get_success_url(self):
        return reverse('leerTipoActuador')


class TipoActuadorDetalle(LoginRequiredMixin, DetailView):
    model = TipoActuador
    extra_context = {'titulo': 'Detalles del Tipo de Actuador'}


class TipoActuadorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TipoActuador
    form = TipoActuador
    fields = "__all__"
    success_message = 'Tipo de Actuador Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Tipo de Actuador'}

    def get_success_url(self):
        return reverse('leerTipoActuador')


class TipoActuadorEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TipoActuador
    form = TipoActuador
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Tipo de Actuador Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerTipoActuador')

#===========================================================================================        

def ajax_controlador_detalle(request, pk):
    controlador = get_object_or_404(Dispositivo, id=pk)
    data = dict()
    data['result'] = render_to_string(template_name='include/detalles_controlador_container.html',
                                      request=request,
                                      context={'controlador': controlador})
    return JsonResponse(data)


def ajax_controlador_actualizar(request, pk):

    controlador = get_object_or_404(Dispositivo, id=pk)
    form = DispositivoForm(request.POST or None, instance=controlador)
    if form.is_valid():
        form.save()
        return redirect('leerUserDispositivo')

    data = dict()
    data['result'] = render_to_string(template_name='include/editar_controlador_container.html',
                                      request=request,
                                      context={'form': form})
    return JsonResponse(data)