from django import forms
from .models import UserDispositivo
from django.forms.models import ModelForm
from django.forms.widgets import TextInput


class ControllerAddForm(ModelForm):
    class Meta:
        model = UserDispositivo
        fields = ['id_dispositivo_fk']

        widgets = {'id_dispositivo_fk': TextInput()}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ControllerAddForm, self).__init__(*args, **kwargs)

    def clean_id_dispositivo_fk(self):
        dispositivo = self.cleaned_data['id_dispositivo_fk']
        
        if UserDispositivo.objects.filter(id_user_fk=self.user, id_dispositivo_fk=dispositivo).exists():
            raise forms.ValidationError("El Dispositivo ya existe en tu Lista de Dispositivos")

        return dispositivo 