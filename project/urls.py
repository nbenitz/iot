"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include


from .views import about, contact, inicio, tablero
from .mqtt_to_mysql import mqtt_loop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    #path('tablero/', tablero, name='tablero'),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('registration.backends.default.urls')),

    path('estructura/', include('estructura.urls')),
    path('dispositivo/', include('dispositivo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.sites.AdminSite.site_header = 'Administracion' 
#admin.sites.AdminSite.site_title = 'My site admin title' 
#admin.sites.AdminSite.index_title = 'My site admin index'

mqtt_loop()

