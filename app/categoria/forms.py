from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Categoria

class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }