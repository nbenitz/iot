#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
"""
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import UserDispositivo
from django.urls import reverse
from django.contrib import messages  
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

#=================================== UserDispositivo ===========================================

class UserDispositivoListado(LoginRequiredMixin, ListView): 
    model = UserDispositivo 
    
class UserDispositivoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__"
    success_message = 'Lista de Dispositivos Creado Correctamente !'

    def get_success_url(self):
        return reverse('leerUserDispositivo')
    
class UserDispositivoDetalle(LoginRequiredMixin, DetailView): 
    model = UserDispositivo
    
class UserDispositivoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = UserDispositivo
    form = UserDispositivo
    fields = "__all__" 
    success_message = 'Lista de Dispositivos Actualizado Correctamente !'
 
    def get_success_url(self):
        return reverse('leerUserDispositivo')

class UserDispositivoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = UserDispositivo 
    form = UserDispositivo
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Lista de Dispositivos Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerUserDispositivo')
"""