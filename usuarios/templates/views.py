from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            domain = email.split('@')[-1]
            if domain not in settings.ALLOWED_DOMAINS_FOR_REGISTRATION:
                form.add_error('email', 'Solo se permite el registro con dominios de la empresa.')
            else:
                user = form.save()
                login(request, user)
                send_mail(
                    'Bienvenido a Inventario IT',
                    f'Hola {user.username}, tu cuenta ha sido creada exitosamente.',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
                return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
