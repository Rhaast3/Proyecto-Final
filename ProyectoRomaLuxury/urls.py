"""
URL configuration for ProyectoRomaLuxury project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Libreria import views  # Importa las vistas desde Libreria



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Libreria.urls')),
    path('Categorias/CrearCategoria', views.crear_categoria, name='CrearCategoria'),  
    path('Categorias/EditarCategoria/<int:id>', views.Editar_categoria, name='EditarCategoria'),
    path('Productos/', views.Productos_1, name='Productos'),
    path('Productos/CrearProducto', views.CrearProducto, name='CrearProducto'),
    path('Productos/EditarProducto/<int:id>', views.EditarProducto, name='EditarProducto'),
    path('Productos/EliminarProducto/<int:id>', views.EliminarProducto, name='EliminarProducto'),
    path('clientes/', views.Clientes_1, name='clientes'),
    path('clientes/crear/', views.CrearCliente, name='crear_cliente'),
    path('clientes/editar/<int:id>/', views.EditarCliente, name='EditarCliente'),
    path('clientes/borrar/<int:id>/', views.BorrarCliente, name='BorrarCliente'),
    path('FacturaPagos/', views.FacturaPagos_1, name='FacturaPagos'),
    path('FacturaPagos/CrearPago/', views.CrearPago, name='CrearPago'),
    path('FacturaPagos/EditarPago/<int:id>/', views.EditarPago, name='EditarPago'),
    path('FacturaPagos/BorrarPago/<int:id>/', views.BorrarPago, name='BorrarPago'),
    path('metodopago/', views.MetodoPago_1, name='MetodoPago_1'),
    path('metodopago/añadir/', views.AñadirMetodoPago, name='AñadirMetodoPago'),
    path('metodopago/editar/<int:id>/', views.EditarMetodoPago, name='EditarMetodoPago'),
    path('metodopago/borrar/<int:id>/', views.BorrarMetodoPago, name='BorrarMetodoPago'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    