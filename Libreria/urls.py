from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),

    path('Catalogo', views.Catalogo, name='Catalogo'),

    path('Categorias/', views.Categorias_1, name='Categorias'),
    path('Categorias/CrearCategoria', views.crear_categoria, name='CrearCategoria'),
    path('Categorias/EditarCategoria/<int:id>', views.Editar_categoria, name='EditarCategoria'),
    path('Categorias/BorrarCategoria/<int:id>', views.BorrarCategoria, name='BorrarCategoria'),

    path('Productos', views.Productos_1, name='Productos'),
    path('Productos/CrearProducto', views.CrearProducto, name='CrearProducto'),
    path('Categorias/EditarProducto/<int:id>', views.EditarProducto, name='EditarProducto'),
    path('Productos/EliminarProducto/<int:id>', views.EliminarProducto, name='EliminarProducto'),

    path('Clientes', views.Clientes_1, name='Clientes'),
    path('Clientes/CrearCliente', views.CrearCliente, name='CrearCliente'),
    path('Clientes/EditarCliente/<int:id>', views.EditarCliente, name='EditarCliente'),
    path('Clientes/BorrarCliente/<int:id>', views.BorrarCliente, name='BorrarCliente'),

    path('Empleados', views.Empleados_1, name='Empleados'),
    path('Empleados/CrearEmpleado', views.CrearEmpleado, name='CrearEmpleado'),
    path('Empleados/EditarEmpleado/<int:id>', views.EditarEmpleado, name='EditarEmpleado'),
    path('Empleados/EliminarEmpleado/<int:id>', views.EliminarEmpleado, name='EliminarEmpleado'),

    path('FacturaPagos', views.FacturaPagos_1, name='FacturaPagos'),
    path('FacturaPagos/CrearPago', views.CrearPago, name='CrearPago'),
    path('FacturaPagos/EditarPago/<int:id>', views.EditarPago, name='EditarPago'),
    path('FacturaPagos/BorrarPago/<int:id>', views.BorrarPago, name='BorrarPago'),

    path('MetodoPago', views.MetodoPago_1, name='MetodoPago'),
    path('MetodoPago/AñadirMetodoPago', views.AñadirMetodoPago, name='AñadirMetodoPago'),
    path('MetodoPago/EditarMetodoPago/<int:id>', views.EditarMetodoPago, name='EditarMetodoPago'),
    path('MetodoPago/BorrarMetodoPago/<int:id>', views.BorrarMetodoPago, name='BorrarMetodoPago'),
]
