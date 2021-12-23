from django.contrib import admin

from app.categoria.forms import FormCategoria
from .models import Categoria


@admin.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "estado")
    list_filter = ("estado", )
    form = FormCategoria
    fieldsets = (
        (None, {
            'fields': (('nombre','cuerpo'), 'img', 'color')
            }),
        )