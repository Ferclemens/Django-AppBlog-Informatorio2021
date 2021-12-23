from django.db import models
from app.categoria.models import Categoria
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):

    def user_directory_path(instance, filename: str):
        '''Toma: Una instancia del Post y el nombre de la imagen que se asigna al post.
        Devuelve: Un string con el directorio donde va a ser guardada la imagen.
        Usada en: El kwarg "upload_to" del atributo "img" del post.
        El kwarg "upload_to" le indica a Django dónde será guardada la imagen que le asignemos al post,
        así puede crear automáticamente esta carpeta y mover ahí el archivo en cuestión.'''
        
        return f"post/{instance.id}/{filename}"

    def obtener_url_absoluta(self):
        '''Toma: self.
           Devuelve: La URL del post en cuestión usando el atributo slug del post.
           Usada en: index.html como href de la tag <a> en la línea de la imagen del post.
           Cada vez que se presione en la imagen de un post en la página principal, se llamará
           esta función, la que llamará al patrón de url "vista_post".'''

        return reverse('post:vista_post', args=[self.slug])

    titulo = models.CharField('Título', 
                              max_length=150, 
                              null=False, 
                              blank=False)

    fecha_creacion = models.DateField('Fecha de creación', 
                                      auto_now=False, 
                                      auto_now_add=True)

    descripcion = models.CharField('Descripción', 
                                    max_length=255, 
                                    null=False, 
                                    blank=False)

    slug = models.SlugField('Slug', 
                            max_length=100, 
                            null=False, 
                            blank=False)

    cuerpo = RichTextField('Cuerpo',
                              null=False, 
                              blank=False, default="")

    img = models.ImageField(upload_to=user_directory_path, default="post/infoblog-logo.png")

    estado = models.BooleanField('Publicado/No publicado', default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET(0))

    destacado = models.BooleanField("Destacar", default=False)

    numero_visitas = models.IntegerField(default=0, editable=False)

    numero_comentarios = models.IntegerField(default=0, editable=False)

    # la forma mas facil de ocultar un post es poniéndole una categoría que no se muestre
    # Si no, la lógica para eliminar o cambiar un atributo se vuelve complicada, ya que
    # los atributos de los modelos no son atributos como tal, si no que son agregados por metaclasses
    # a una lista _meta.fields

    class Meta:
        ordering = ('fecha_creacion', )

    def __str__(self) -> str:
        return self.titulo
