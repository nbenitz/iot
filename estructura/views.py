#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Empresa, Invernadero, Sector, Cultivo, TipoCultivo
from django.urls import reverse
from django.contrib import messages  
from django.contrib.messages.views import SuccessMessageMixin 

#=================================== CLIENTE ===========================================
class EmpresaListado(ListView): 
    model = Empresa
    
class EmpresaCrear(SuccessMessageMixin, CreateView): 
    model = Empresa # Llamamos a la clase 'Empresa' que se encuentra en nuestro archivo 'models.py'
    form = Empresa # Definimos nuestro formulario con el nombre de la clase o modelo 'Empresa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cliente' de nuestra Base de Datos 
    success_message = 'Empresa Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerEmpresa') # Redireccionamos a la vista principal 'leer'

    
class EmpresaDetalle(DetailView): 
    model = Empresa # Llamamos a la clase 'Empresa' que se encuentra en nuestro archivo 'models.py'
 
class EmpresaActualizar(SuccessMessageMixin, UpdateView): 
    model = Empresa # Llamamos a la clase 'Empresa' que se encuentra en nuestro archivo 'models.py' 
    form = Empresa # Definimos nuestro formulario con el nombre de la clase o modelo 'Empresa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cliente' de nuestra Base de Datos 
    success_message = 'Empresa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerEmpresa') # Redireccionamos a la vista principal 'leer'
   
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa 
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o cliente
    def get_success_url(self): 
        success_message = 'Empresa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Empresa 
        messages.success (self.request, (success_message))       
        return reverse('leerEmpresa') # Redireccionamos a la vista principal 'leer'

#=================================== EMPLEADO ===========================================

class InvernaderoListado(ListView): 
    model = Invernadero 
    
class InvernaderoCrear(SuccessMessageMixin, CreateView): 
    model = Invernadero
    form = Invernadero
    fields = "__all__"
    success_message = 'Invernadero Creado Correctamente !'

    def get_success_url(self):
        return reverse('leer')
    
class InvernaderoDetalle(DetailView): 
    model = Invernadero
    
class InvernaderoActualizar(SuccessMessageMixin, UpdateView): 
    model = Invernadero
    form = Invernadero
    fields = "__all__" 
    success_message = 'Invernadero Actualizado Correctamente !'
 
    def get_success_url(self):
        return reverse('leer')

class InvernaderoEliminar(SuccessMessageMixin, DeleteView): 
    model = Invernadero 
    form = Invernadero
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Invernadero Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')
    