from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from inventario.models import Equipo
from .models import RegistroBitacora, Auditoria
from .forms import RegistroBitacoraForm
from django.contrib import messages

@login_required
def agregar_registro_bitacora(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        form = RegistroBitacoraForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.equipo = equipo
            registro.usuario = request.user
            registro.save()
            Auditoria.objects.create(usuario=request.user, accion=f"Se agregó un registro a la bitácora del equipo: {equipo.nombre}")
            messages.success(request, "Registro de bitácora añadido exitosamente.")
            return redirect('detalle_equipo', pk=equipo.pk)
    else:
        form = RegistroBitacoraForm()
    return render(request, 'bitacora/form_registro_bitacora.html', {'form': form, 'equipo': equipo})

@login_required
def lista_auditoria(request):
    registros_auditoria = Auditoria.objects.all().order_by('-fecha')
    return render(request, 'bitacora/lista_auditoria.html', {'registros': registros_auditoria})