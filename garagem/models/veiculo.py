from django.db import models
from garagem.models import Cor, Modelo
from uploader.models import Image

class Veiculo (models.Model):
    cor = models.ForeignKey (Cor, on_delete=models.CASCADE)
    modelo = models.ForeignKey (Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ForeignKey(Image, related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,)

    def __str__ (self):
        return self.descricao