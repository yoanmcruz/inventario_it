from import_export import resources
from .models import Equipo

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
        fields = ('nombre', 'tipo', 'marca', 'modelo', 'serial', 'ubicacion', 'estado', 'fecha_adquisicion')