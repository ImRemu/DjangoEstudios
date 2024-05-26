from django.contrib import admin

from productos.models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)