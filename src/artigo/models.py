from django.db import models

from categoria.models import Categoria


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='imagem_artigo', blank=True)
    autor = models.CharField(max_length=50)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='artigos'
    )

    def __str__(self):
        return self.titulo
