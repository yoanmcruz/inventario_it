from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib import messages

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            domain = email.split('@')[-1]
            if domain not in settings.ALLOWED_DOMAINS_FOR_REGISTRATION:
                messages.error(request, 'Solo se permite el registro con dominios de la empresa.')
            else:
                user = form.save()
                messages.success(request, '¡Tu cuenta ha sido creada exitosamente! Por favor, inicia sesión.')
                # Aquí puedes enviar un correo de bienvenida si lo deseas.
                return redirect('login')
        else:
            messages.error(request, 'Hubo un error en el registro. Por favor, revisa los datos.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')