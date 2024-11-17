from django.contrib import admin
from .models import Empleados, Categoria, Productos, MetodoPago, Clientes, FacturaPagos

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Usuario', 'Rol']

class CategoriaAdmin(admin.ModelAdmin):  # Cambia de 'CategoriasAdmin' a 'CategoriaAdmin'
    list_display = ['nombre', 'descripcion']  # Cambia las propiedades a minúsculas

class ClientesAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Correo', 'Identificacion']

class FacturaPagosAdmin(admin.ModelAdmin):
    list_display = ['Fecha', 'CantidadProductos', 'Valor', 'Productos', 'MetodoPago', 'Clientes']

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Precio', 'Empleados', 'Categoria', 'Imagen']  # Cambia 'Categorias' a 'Categoria'

# Registro de modelos en el panel de administración
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Categoria, CategoriaAdmin)  # Cambia de 'CategoriasAdmin' a 'CategoriaAdmin'
admin.site.register(Productos, ProductosAdmin)
admin.site.register(MetodoPago)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(FacturaPagos, FacturaPagosAdmin)
