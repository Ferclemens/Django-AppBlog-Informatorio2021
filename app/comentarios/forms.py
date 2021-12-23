from django import forms
from .models import Comentarios


class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('cuerpo', )
        widgets = {            
            "cuerpo": forms.Textarea(attrs={"class": "form-control"})
        }