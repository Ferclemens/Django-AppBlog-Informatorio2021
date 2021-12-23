from django.db import models
from django.db.models.deletion import CASCADE
from app.post.models import Post
from django.contrib.auth.models import User
import random
# Create your models here.


class Comentarios(models.Model):   
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor   = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha   = models.DateField('Fecha de Creación',
                             auto_now=False,
                             auto_now_add=True)
    cuerpo  = models.TextField('Cuerpo', max_length=255)
    estado  = models.BooleanField(default=True)

    class Meta:
        ordering = ('fecha', )

    def __str__(self) -> str:
        return str(self.autor)

    def obtener_imagen(self):
        try:
            letra = self.autor.username[0].upper()
        except AttributeError:
            letra = self.autor.username[0]
            
        num = random.choice((0,1))
        return f"{letra}_{num}.png"
