from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Modelo (models.Model):
    Categoria = models.ForeignKey (Categoria, on_delete=models.CASCADE)
    Marca = models.ForeignKey (Marca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cor (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

