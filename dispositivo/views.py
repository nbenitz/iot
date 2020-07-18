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

from .models import Dispositivo, Sensor, TipoSensor, Actuador, TipoActuador, PublicacionSensor, PublicacionActuador
from .forms import DispositivoForm
from persona.models import User
from estructura.models import UserDispositivo

# Create your views here.

# =================================== SENSOR ===========================================


class SensorListado(LoginRequiredMixin, ListView):
    model = Sensor


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

    def get_success_url(self):
        return reverse('leerSensor')


class SensorDetalle(LoginRequiredMixin, DetailView):
    model = Sensor


class SensorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Sensor
    form = Sensor
    fields = "__all__"
    success_message = 'Sensor Actualizado Correctamente !'

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


# =================================== CONTROLADOR ===========================================

class DispositivoListado(LoginRequiredMixin, ListView):
    model = UserDispositivo
    extra_context = {'titulo': 'Controlador',
                     'plural': 'Controladores'}

    def get_queryset(self, **kwargs):
        qs = self.model.objects.filter(id_user_fk=self.request.user.id)
        return qs


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