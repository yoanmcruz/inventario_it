from django.contrib import admin
from .models import RegistroBitacora, Auditoria

@admin.register(RegistroBitacora)
class RegistroBitacoraAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'usuario', 'fecha', 'descripcion')
    list_filter = ('fecha', 'usuario')
    search_fields = ('equipo__nombre', 'equipo__serial', 'descripcion')
    date_hierarchy = 'fecha'
    list_per_page = 25

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'accion', 'fecha')
    list_filter = ('fecha', 'usuario')
    search_fields = ('usuario__username', 'accion')
    date_hierarchy = 'fecha'
    list_per_page = 25