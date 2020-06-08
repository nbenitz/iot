# views.py
from django.shortcuts import render, redirect
from persona.forms import SignUpForm, UserForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template.loader import render_to_string
from persona.tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


# Create your views here.

class ObjetoDetalle(LoginRequiredMixin, DetailView): 
    """model = get_user_model()"""

@login_required
def edit_user(request, pk):
    
    user = get_user_model().objects.get(id=pk)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Usuario actualizado correctmente'))
            return redirect('detallesUser', pk)
            
    else:
        user_form = UserForm(instance=user)
        
    return render(request, 'user/actualizar.html',{
        'user_form': user_form,
        'titulo': 'Actualizar Cuenta',
        })

def register(request):
    
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
            
        if user_form.is_valid():         
            user = user_form.save()

            current_site = get_current_site(request)
            subject = 'Por favor activa tu cuenta'
            email_from = settings.EMAIL_HOST_USER
            message = render_to_string('registration/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message, email_from)
        
            return redirect('activation_send')
            
    else:
        user_form = SignUpForm()
        
    return render(request, 'user/crear.html',{
        'user_form': user_form,
        'titulo': 'Registro de Cuenta',
        })

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('activation_complete')
    else:
        return render(request, 'registration/activation_invalid.html')
    
def activation_sent_view(request):
    return render(request, 'registration/registration_complete.html')

def activation_complete_view(request):
    return render(request, 'registration/activation_complete.html')