# estructura/urls.py
from django.urls import path

from .views import TopicListado, TopicCrear, TopicActualizar, TopicDetalle, TopicEliminar

urlpatterns = [
    path('topic/', TopicListado.as_view(template_name = "topic/index.html"), name='leerTopic'),
    path('topic/detalle/<str:pk>', TopicDetalle.as_view(template_name = "topic/detalles.html"), name='detallesTopic'),
    path('topic/crear', TopicCrear.as_view(template_name = "topic/crear.html"), name='crear'),
    path('topic/editar/<str:pk>', TopicActualizar.as_view(template_name = "topic/actualizar.html"), name='actualizarTopic'),
    path('topic/eliminar/<str:pk>', TopicEliminar.as_view(), name='eliminarTopic'),

]
