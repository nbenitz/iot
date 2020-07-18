from .models import Dispositivo
from django.forms.models import ModelForm

class DispositivoForm(ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'