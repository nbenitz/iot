#from django.shortcuts import render

# Instanciamos las vistas gen�ricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Topic
from django.urls import reverse
from django.contrib import messages  
from django.contrib.messages.views import SuccessMessageMixin 

#=================================== Topic ===========================================

class TopicListado(ListView): 
    model = Topic 
    
class TopicCrear(SuccessMessageMixin, CreateView): 
    model = Topic
    form = Topic
    fields = "__all__"
    success_message = 'Topic Creado Correctamente !'

    def get_success_url(self):
        return reverse('leerTopic')
    
class TopicDetalle(DetailView): 
    model = Topic
    
class TopicActualizar(SuccessMessageMixin, UpdateView): 
    model = Topic
    form = Topic
    fields = "__all__" 
    success_message = 'Topic Actualizado Correctamente !'
 
    def get_success_url(self):
        return reverse('leerTopic')

class TopicEliminar(SuccessMessageMixin, DeleteView): 
    model = Topic 
    form = Topic
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Topic Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerTopic')
    