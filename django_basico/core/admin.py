from django.contrib import admin
from .models import Produto, Cliente
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)