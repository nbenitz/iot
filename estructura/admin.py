from django.contrib import admin

# Register your models here.
from .models import Empresa, Invernadero, Sector, Cultivo, TipoCultivo

admin.site.register(Empresa)
admin.site.register(Invernadero)
admin.site.register(Sector)
admin.site.register(Cultivo)
admin.site.register(TipoCultivo)
