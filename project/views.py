from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import HttpResponse
import json

from .forms import ContactForm
# Create your views here.


def inicio(request):
    return render(request, "inicio.html", {})


def about(request):
    return render(request, "about.html", {})


def tablero(request):
    return render(request, "tablero.html", {})


def contact(request):
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #    print(key, value)
        # for key in form.cleaned_data:
        #    print(key)
        #    print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "n.benitez.a@hotmail.com"]
        email_mensaje = "%s: %s enviado por %s" % (
            form_nombre, form_mensaje, form_email)
        send_mail(
            asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
        )
        #print(email, mensaje, nombre)

    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, "contact.html", context)


@login_required
@require_GET
def set_user_timezone(request):
    timezone = request.GET.get('timezone')
    request.session['user_timezone'] = timezone
    response_data = {}
    response_data['status'] = 'true'
    response_data['message'] = 'user timezone set successfully.'
    return HttpResponse(json.dumps(response_data))
