from django.db import models


# Create your models here.
class Categoria(models.Model):
    def user_directory_path(instance, filename: str):
        '''Toma: Una instancia del Post y el nombre de la imagen que se asigna a la categoria.
        Devuelve: Un string con el directorio donde va a ser guardada la imagen.
        Usada en: El kwarg "upload_to" del atributo "img" de la categoria.
        El kwarg "upload_to" le indica a Django dónde será guardada la imagen que le asignemos al post,
        así puede crear automáticamente esta carpeta y mover ahí el archivo en cuestión.'''
        
        return f"categorias/{instance.id}/{filename}"

    nombre = models.CharField('Nombre de la Categoría',
                              max_length=80, 
                              null=False, 
                              blank=False)

    img = models.ImageField(upload_to=user_directory_path, default="post/infoblog-logo.png")

    color = models.TextField(default="(122,122,122)")

    cuerpo = models.TextField('Cuerpo',
                              max_length=250, 
                              null=False, 
                              blank=False, default="")
                              
    estado = models.BooleanField('Categoría Activada/Categoría Desactivada',
                                 default=True)

    def __str__(self) -> str:
        return self.nombre
