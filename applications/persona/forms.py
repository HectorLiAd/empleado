from django import forms
from django.forms import fields
from django.forms import widgets
from .models import Empleado
class EmpleadoForm(forms.ModelForm):
    pass
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
            'hoja_vida',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(

            ),
        }