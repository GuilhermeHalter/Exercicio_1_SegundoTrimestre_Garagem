from django.contrib import admin

from .models import Categoria, Marca, Modelo

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
# Register your models here.
