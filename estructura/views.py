#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from estructura.models import UserDispositivo, Tablero
from django.db.models import Avg
from estructura.forms import ControllerAddForm, TableroForm
from dispositivo.models import Sensor, Actuador, Dispositivo, PublicacionSensor, PublicacionActuador, PublicacionControlador
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils import timezone
import pytz
from datetime import datetime
# from django.db.models import Max

# =================================== UserDispositivo ===========================================


class UserDispositivoListado(LoginRequiredMixin, TemplateView):
    # model = UserDispositivo
    # extra_context={'titulo':'Dispositivos',
    #                'plural':'Dispositivos'}

    def get_context_data(self, *args, **kwargs):
        controladores = UserDispositivo.objects.filter(
            id_user_fk=self.request.user.id)
        return {'object_list': controladores}

    # def get_queryset(self, **kwargs):
    #     qs = self.model.objects.filter(id_user_fk=self.request.user.id)
    #     return qs


class UserDispositivoCrear2(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__"
    success_message = 'Lista de Dispositivos Creado Correctamente !'
    extra_context = {'titulo': 'Agregar Controlador'}

    def get_success_url(self):
        return reverse('leerUserDispositivo')


class UserDispositivoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ControllerAddForm
    success_message = 'Dispositivo Agregado Correctamente !'
    extra_context = {'titulo': 'Agregar Controlador'}

    # Sending user object to the form, to verify which fields to display/remove
    # def get_form_kwargs(self):
    #     kwargs = super(UserDispositivoCrear, self).get_form_kwargs()
    #     kwargs.update({'user': self.request.user})
    #     return kwargs
    # Sending user object to the form, to verify which fields to display/remove
    def get_form_kwargs(self):
        kwargs = super(UserDispositivoCrear, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        #cliente = Cliente.objects.get(user_id=self.request.user.id)
        form.instance.id_user_fk = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('leerUserDispositivo')



class UserDispositivoDetalle(LoginRequiredMixin, DetailView):
    model = UserDispositivo
    extra_context = {'titulo': 'Detalles del Controlador'}



class UserDispositivoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__"
    success_message = 'Lista de Dispositivos Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Controlador'}

    def get_success_url(self):
        return reverse('leerUserDispositivo')



class UserDispositivoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Dispositivo Removido Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerUserDispositivo')


# =================================== Tablero ===========================================

class TableroListado(LoginRequiredMixin, ListView):
    model = Tablero
    extra_context = {'titulo': 'Tablero',
                     'plural': 'Tableros'}

    def get_queryset(self, **kwargs):
        qs = self.model.objects.filter(id_user_fk=self.request.user.id)
        return qs


class TableroCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tablero
    form_class = TableroForm
    success_message = 'Tablero Creado Correctamente !'
    extra_context = {'titulo': 'Crear Tablero'}
    success_url = reverse_lazy('leerTablero')

    def form_valid(self, form):
        form.instance.id_user_fk = self.request.user
        return super().form_valid(form)


class TableroDetalle(LoginRequiredMixin, DetailView):
    model = Tablero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tablero = self.model.objects.get(id=self.kwargs['pk'])
        context.update(locals())
        return context


class TableroStats(LoginRequiredMixin, DetailView):
    model = Tablero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tablero = self.model.objects.get(id=self.kwargs['pk'])

        timezone_name = self.request.session.get('user_timezone')
        if not timezone_name:
            timezone_name = 'America/Asuncion'
        lz = pytz.timezone(timezone_name)
        utc = pytz.timezone('UTC')

        now = datetime.strptime(
            timezone.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
        now = lz.localize(now).astimezone(utc)

        sensor_list = tablero.sensor.all()
        # pub = PublicacionSensor.objects.none
        # for i, sensor in enumerate(sensor_list):
        # sensor = self.sensor.get(id=id_sensor)
        # sensor = get_object_or_404(Sensor, id=id_sensor)
        pub = PublicacionSensor.objects.filter(id_sensor_fk__in=sensor_list,
                                               fecha__gte=now,
                                               ).aggregate(Avg('valor'))
        # print(pub)

        context.update(locals())
        return context


class TableroActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tablero
    form_class = TableroForm
    success_message = 'Tablero Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Tablero'}
    #success_url = reverse_lazy('leerTablero')

    def get_success_url(self):
        return reverse('leerTablero')


class TableroEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tablero
    form = Tablero
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Tablero Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerTablero')


# ===================================== AJAX CALLS ===================================

def ajax_tablero_buttons(request):
    tableros = Tablero.objects.filter(id_user_fk=request.user.id)
    data = dict()
    data['result'] = render_to_string(template_name='include/tablero_buttons_container.html',
                                      request=request,
                                      context={'tableros': tableros})
    return JsonResponse(data)
