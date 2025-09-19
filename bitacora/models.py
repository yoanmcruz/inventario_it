from django.db import models
from django.contrib.auth import get_user_model
from inventario.models import Equipo

User = get_user_model()

class RegistroBitacora(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='registros_bitacora')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(help_text="Descripción del movimiento, reparación o incidencia.")
    
    def __str__(self):
        return f"Registro para {self.equipo.nombre} el {self.fecha.strftime('%Y-%m-%d')}"

class Auditoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=255, help_text="Descripción de la acción realizada (ej. 'Creación de equipo', 'Modificación de bitácora').")
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.accion} ({self.fecha})"