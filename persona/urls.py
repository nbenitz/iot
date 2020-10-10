# persona/urls.py
from django.urls import path
from django.contrib.auth import get_user_model
from persona.views import register, activation_sent_view, activate, activation_complete_view, \
     ObjetoDetalle, edit_user, set_timezone


urlpatterns = [

    path('signup/', register, name="signup"),
    path('sent/', activation_sent_view, name="activation_send"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('activated/', activation_complete_view, name='activation_complete'),

    path('user/editar/<str:pk>', edit_user, name='actualizarUser'),
    path('user/detalle/<str:pk>', ObjetoDetalle.as_view(template_name="user/detalles.html",
                                                           model = get_user_model(),
                                                           extra_context={'titulo':'Cuenta'}
                                                           ), name='detallesUser'),
    path('user/set-timezone/', set_timezone, name='setTimezone'),
]

