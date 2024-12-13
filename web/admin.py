from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto

admin.site.register(Categoria)
# admin.site.register(Producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # que cosas quiero que se muestren en mi listado de admin
    list_display = ('nombre','precio','categoria','fecha_registro')
    list_editable = ['precio',]
    list_filter=['nombre']
    search_fields = ['nombre' ] 