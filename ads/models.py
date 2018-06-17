from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from blogs.models import Blog
from categorias.models import Categoria


class Post(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    titulo = models.CharField(max_length=40)
    texto = models.CharField(max_length=100)
    cuerpo = models.TextField()
    URLimagen = models.FileField(null=True)
    fechapublicacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """
        Define como se representa un Post como un string

        """
        return '{0}' .format(self.titulo)
