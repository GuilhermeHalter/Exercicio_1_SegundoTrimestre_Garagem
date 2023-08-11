from django.contrib import admin

from .models import Categoria, Marca, Modelo, Cor, Acessorio

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Cor)
admin.site.register(Acessorio)

# Register your models here.
