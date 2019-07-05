from django.db import models

class Conquista(models.Model):

    nome_conquista = models.CharField(max_length=50)
    valor = models.IntegerField(default = 0)
    disponivel = models.BooleanField(default = False)
    conteudo = models.FileField(upload_to='conquista/')

    def __str__(self):
        return self.nome_conquista
