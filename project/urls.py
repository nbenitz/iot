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
from django.conf import settings
from django.conf.urls.static import static


from .views import about, contact, inicio, tablero, set_user_timezone
# from .mqtt_to_pg import mqtt_loop
# from concurrent.futures import ThreadPoolExecutor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    #path('tablero/', tablero, name='tablero'),
    #path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('set-user-timezone/', set_user_timezone, name='set_user_timezone'),

    path('', include('estructura.urls')),
    path('', include('dispositivo.urls')),
    path('', include('persona.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.sites.AdminSite.site_header = 'Administración'
#admin.sites.AdminSite.site_title = 'My site admin title'
#admin.sites.AdminSite.index_title = 'My site admin index'

# with ThreadPoolExecutor(max_workers=1) as executor:
#    executor.submit(mqtt_loop())
# mqtt_loop()
