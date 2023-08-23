from django.contrib import admin
from .models import CategoriaManutencao, Servico, ServicoAdicional

admin.site.register(CategoriaManutencao)
admin.site.register(Servico)
admin.site.register(ServicoAdicional)