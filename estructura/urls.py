# estructura/urls.py
from django.urls import path

from .views import EmpresaListado, EmpresaCrear, EmpresaActualizar, EmpresaDetalle, EmpresaEliminar

urlpatterns = [
    path('empresa/', EmpresaListado.as_view(template_name = "empresa/index.html"), name='leerEmpresa'),
    path('empresa/detalle/<str:pk>', EmpresaDetalle.as_view(template_name = "empresa/detalles.html"), name='detallesEmpresa'),
    path('empresa/crear', EmpresaCrear.as_view(template_name = "empresa/crear.html"), name='crear'),
    path('empresa/editar/<str:pk>', EmpresaActualizar.as_view(template_name = "empresa/actualizar.html"), name='actualizarEmpresa'),
    path('empresa/eliminar/<str:pk>', EmpresaEliminar.as_view(), name='eliminarEmpresa'),

]
