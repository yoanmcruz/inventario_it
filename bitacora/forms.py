from django import forms
from .models import RegistroBitacora

class RegistroBitacoraForm(forms.ModelForm):
    class Meta:
        model = RegistroBitacora
        fields = ['descripcion']