from django.shortcuts import render
from django.http import HttpResponse
from Libreria.models import Categoria, Clientes, Productos, Empleados, FacturaPagos, MetodoPago
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoriaForm
from .forms import ProductoForm
from .forms import ClienteForm
from .forms import Clientes
from .models import Empleados
from .forms import EmpleadoForm
from .models import FacturaPagos
from .forms import FacturaPagosForm
from .models import MetodoPago
from .forms import MetodoPagoForm

# Create your views here.

def inicio(request):
    return render(request, "pagina/inicio.html")

def nosotros(request):
    return render(request, 'pagina/nosotros.html')



def Catalogo(request):
    return render(request, 'Catalogo/Catalogo.html')


def Categorias_1(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'Categorias/Categorias.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CrearCategoria')  
    else:
        form = CategoriaForm()
    return render(request, 'Categorias/Form.html', {'form': form})

def Editar_categoria(request, id):
    # Obtiene la categoría o muestra un 404 si no existe
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('Categorias')  # Redirige a la lista de categorías después de editar
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'Categorias/EditarCategoria.html', {'form': form})
def BorrarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == "POST":
        categoria.delete()
        return redirect('Categorias')  # Redirige a la vista de categorías después de eliminar

    return render(request, 'Categorias/BorrarCategoria.html', {'categoria': categoria})

def Productos_1(request):
    productos = Productos.objects.all()
    return render(request, 'Productos/Productos.html', {'productos': productos})

def CrearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('Productos') 
    else:
        form = ProductoForm()
    return render(request, 'Productos/CrearProducto.html', {'form': form})

def EditarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Productos/EditarProducto.html', {'form': form})

def EliminarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('Productos')  # Cambia esto por el nombre correcto de tu URL
    return render(request, 'Productos/EliminarProducto.html', {'producto': producto})


def Clientes_1(request):
    cliente = Clientes.objects.all()  # Obtiene todas las categorías
    return render(request,'Clientes/Clientes.html', {'clientes': cliente} )

def CrearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'Clientes/CrearCliente.html', {'form': form})

def EditarCliente(request, id):
    # Obtener el cliente de la base de datos usando su ID
    cliente = get_object_or_404(Clientes, id=id)

    if request.method == 'POST':
        # Crear el formulario y pasarle los datos del cliente actual
        form = ClienteForm(request.POST, instance=cliente)
        
        if form.is_valid():  # Si el formulario es válido, guarda los datos
            form.save()
            return redirect('Clientes')  # Redirige a la lista de clientes
    else:
        # Si no es una solicitud POST, crea el formulario con la instancia del cliente
        form = ClienteForm(instance=cliente)

    # Renderiza el formulario en el template
    return render(request, 'Clientes/EditarCliente.html', {'form': form, 'cliente': cliente})

def BorrarCliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('Clientes')  # Redirige después de borrar
    return render(request, 'Clientes/BorrarCliente.html', {'cliente': cliente})

def Empleados_1(request):
    empleados = Empleados.objects.all()
    return render(request,'Empleados/Empleados.html', {'empleados': empleados} )

def CrearEmpleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo empleado.
            return redirect('Empleados')  # Redirige a la lista de empleados.
    else:
        form = EmpleadoForm()  # Si no es un POST, muestra el formulario vacío.
    return render(request, 'Empleados/CrearEmpleado.html', {'form': form})

# Vista para editar un empleado existente
def EditarEmpleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)  # Obtiene al empleado según el ID.
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()  # Guarda los cambios del empleado.
            return redirect('Empleados')  # Redirige a la lista de empleados.
    else:
        form = EmpleadoForm(instance=empleado)  # Muestra el formulario con los datos del empleado.
    return render(request, 'Empleados/EditarEmpleado.html', {'form': form, 'empleado': empleado})

# Vista para eliminar un empleado
def EliminarEmpleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)  # Obtiene al empleado según el ID.
    if request.method == 'POST':
        empleado.delete()  # Elimina el empleado.
        return redirect('Empleados')  # Redirige a la lista de empleados.
    return render(request, 'Empleados/EliminarEmpleado.html', {'empleado': empleado})  # Confirma antes de eliminar.


def FacturaPagos_1(request):
    facturapagos = FacturaPagos.objects.all()
    return render(request, 'FacturaPagos/FacturaPagos.html', {'facturapagos': facturapagos})

def CrearPago(request):
    if request.method == 'POST':
        form = FacturaPagosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FacturaPagos')
    else:
        form = FacturaPagosForm()
    return render(request, 'FacturaPagos/CrearPago.html', {'form': form})
def EditarPago(request, id):
    factura = get_object_or_404(FacturaPagos, id=id)

    if request.method == 'POST':
        form = FacturaPagosForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()  # Guarda los cambios en la factura de pago
            return redirect('FacturaPagos')  # Redirige a la lista de facturas de pago
        else:
            print(form.errors)  # Imprime los errores del formulario en la consola
    else:
        form = FacturaPagosForm(instance=factura)

    return render(request, 'FacturaPagos/EditarPago.html', {'form': form, 'factura': factura})


def BorrarPago(request, id):
    factura = get_object_or_404(FacturaPagos, id=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('FacturaPagos')
    return render(request, 'FacturaPagos/BorrarPago.html', {'factura': factura})

def MetodoPago_1(request):
    metodopagos = MetodoPago.objects.all()
    return render(request, 'MetodoPago/MetodoPago.html', {'metodopagos': metodopagos})

def AñadirMetodoPago(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MetodoPago_1')  # Redirige a la lista de métodos de pago
    else:
        form = MetodoPagoForm()
    return render(request, 'MetodoPago/AñadirMetodoPago.html', {'form': form})

def EditarMetodoPago(request, id):
    metodopago = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST, instance=metodopago)
        if form.is_valid():
            form.save()
            return redirect('MetodoPago_1')
    else:
        form = MetodoPagoForm(instance=metodopago)
    return render(request, 'MetodoPago/EditarMetodoPago.html', {'form': form, 'id': id})

def BorrarMetodoPago(request, id):
    metodopago = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        metodopago.delete()
        return redirect('MetodoPago_1')
    return render(request, 'MetodoPago/BorrarMetodoPago.html', {'metodopago': metodopago})