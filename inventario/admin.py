from django.contrib import admin
from .models import Equipo, Componente

# Define la clase Inline para el modelo Componente
class ComponenteInline(admin.TabularInline):
    model = Componente
    extra = 1  # Proporciona un campo extra para añadir un nuevo componente
    verbose_name = "Componente"
    verbose_name_plural = "Componentes"

# Define la clase ModelAdmin para el modelo Equipo
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'marca', 'modelo', 'serial', 'ubicacion', 'estado', 'fecha_adquisicion')
    list_filter = ('estado', 'tipo', 'ubicacion', 'marca')
    search_fields = ('nombre', 'serial', 'marca', 'modelo')
    list_per_page = 25  # Paginación de 25 equipos por página
    ordering = ('nombre',)
    
    inlines = [ComponenteInline]

# Define la clase ModelAdmin para el modelo Componente
@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'serial', 'equipo')
    list_filter = ('equipo',)
    search_fields = ('nombre', 'serial')