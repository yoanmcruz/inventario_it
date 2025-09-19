from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventario.models import Equipo
from bitacora.models import RegistroBitacora

@login_required
def dashboard_view(request):
    total_equipos = Equipo.objects.count()
    equipos_activos = Equipo.objects.filter(estado='activo').count()
    equipos_mantenimiento = Equipo.objects.filter(estado='mantenimiento').count()
    ultimas_reparaciones = RegistroBitacora.objects.all().order_by('-fecha')[:5]
    
    estadisticas = {
        'total_equipos': total_equipos,
        'equipos_activos': equipos_activos,
        'equipos_mantenimiento': equipos_mantenimiento,
    }
    
    return render(request, 'core/dashboard.html', {
        'estadisticas': estadisticas,
        'ultimas_reparaciones': ultimas_reparaciones
})