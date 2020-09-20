#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from estructura.models import UserDispositivo, Tablero
from estructura.forms import ControllerAddForm
from dispositivo.models import Sensor, Actuador, Dispositivo
from django.urls import reverse
from django.contrib import messages  
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

#=================================== UserDispositivo ===========================================

class UserDispositivoListado(LoginRequiredMixin, TemplateView): 
    # model = UserDispositivo
    # extra_context={'titulo':'Dispositivos',
    #                'plural':'Dispositivos'}

    def get_context_data(self, *args, **kwargs):
        controladores = UserDispositivo.objects.filter(id_user_fk=self.request.user.id)
        return {'object_list': controladores}

    # def get_queryset(self, **kwargs):
    #     qs = self.model.objects.filter(id_user_fk=self.request.user.id)        
    #     return qs

    
class UserDispositivoCrear2(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__"
    success_message = 'Lista de Dispositivos Creado Correctamente !'
    extra_context={'titulo':'Agregar Controlador'}

    def get_success_url(self):
        return reverse('leerUserDispositivo')




class UserDispositivoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    form_class = ControllerAddForm
    success_message = 'Dispositivo Agregado Correctamente !'
    extra_context={'titulo':'Agregar Controlador'}
    
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
    extra_context={'titulo':'Detalles del Controlador'}
    
class UserDispositivoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__" 
    success_message = 'Lista de Dispositivos Actualizado Correctamente !'
    extra_context={'titulo':'Editar Controlador'}
 
    def get_success_url(self):
        return reverse('leerUserDispositivo')

class UserDispositivoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = UserDispositivo 
    form = UserDispositivo
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Dispositivo Removido Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerUserDispositivo')


#=================================== Tablero ===========================================

class TableroListado(LoginRequiredMixin, ListView): 
    model = Tablero
    extra_context={'titulo':'Tablero',
                   'plural':'Tableros'}

    def get_queryset(self, **kwargs):
        qs = self.model.objects.filter(id_user_fk=self.request.user.id)        
        return qs
    
class TableroCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tablero
    form = Tablero
    fields = "__all__"
    success_message = 'Tablero Creado Correctamente !'
    extra_context={'titulo':'Crear Tablero'}

    def get_success_url(self):
        return reverse('leerTablero')
    
class TableroDetalle(LoginRequiredMixin, DetailView): 
    model = Tablero
    extra_context={'titulo':'Detalles del Tablero'}

    
class TableroActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Tablero
    form = Tablero
    fields = "__all__" 
    success_message = 'Tablero Actualizado Correctamente !'
    extra_context={'titulo':'Editar Tablero'}
 
    def get_success_url(self):
        return reverse('leerTablero')

class TableroEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Tablero 
    form = Tablero
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Tablero Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerTablero')


# ===================================== AJAX CALLS ===================================

def ajax_tablero_buttons(request):
    tableros = Tablero.objects.filter(id_user_fk=request.user.id)
    data = dict()
    data['result'] = render_to_string(template_name='include/tablero_buttons_container.html',
                                      request=request,
                                      context={'tableros': tableros})
    return JsonResponse(data)