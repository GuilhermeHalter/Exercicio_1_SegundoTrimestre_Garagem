from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Modelo, Acessorio, Cor, Marca, Veiculo
from garagem.serializers import CategoriaSerializer, AcessorioSerializer, CorSerializer, MarcaSerializer, ModeloSerializer, VeiculoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

# Create your views here.
