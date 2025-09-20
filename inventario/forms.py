from django import forms
from .models import Equipo, Componente

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        #fields = '__all__'
        fields = ['nombre', 'tipo', 'marca', 'modelo', 'serial', 'ubicacion', 'estado', 'fecha_adquisicion', 'descripcion']
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
        }

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['nombre', 'marca', 'modelo', 'serial', 'descripcion']
