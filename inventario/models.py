from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Equipo(models.Model):
    TIPO_CHOICES = [
        ('servidor', 'Servidor'),
        ('pc', 'PC de escritorio'),
        ('portatil', 'Laptop'),
        ('monitor', 'Monitor'),
        ('impresora', 'Impresora'),
        ('otro', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('mantenimiento', 'En Mantenimiento'),
        ('baja', 'Dado de Baja'),
    ]
    
    nombre = models.CharField(max_length=200, help_text="Nombre descriptivo del equipo")
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=150, unique=True, help_text="Número de serie único")
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='activo')
    fecha_adquisicion = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.serial}"

class Componente(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='componentes')
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    serial = models.CharField(max_length=150, unique=True, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
