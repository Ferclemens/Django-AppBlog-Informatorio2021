from django.contrib import admin
from app.post.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha_creacion", "slug", "descripcion", "estado", "numero_comentarios", "numero_visitas")
    list_filter = ("estado", "destacado")
    search_fields = ("cuerpo", "titulo")
    