from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'descripcion',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese texto aqui'
                }
            )
        }

    def clean_cantidad(self):
        data = self.cleaned_data["cantidad"]
        if data < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        return data
    