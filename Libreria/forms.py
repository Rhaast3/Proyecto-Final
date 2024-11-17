from django import forms
from .models import Categoria
from .models import Productos
from .models import Clientes
from .models import Empleados
from .models import FacturaPagos
from .models import MetodoPago


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['Nombre', 'Precio', 'Empleados', 'Categoria', 'Imagen']
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['Nombre', 'Correo', 'Identificacion']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['Nombre', 'Usuario', 'Rol']  # Los campos del formulario que se utilizarán.
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del empleado'}),
            'Usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'Rol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rol del empleado'}),
        }
        

class FacturaPagosForm(forms.ModelForm):
    class Meta:
        model = FacturaPagos
        fields = ['Fecha', 'CantidadProductos', 'Valor', 'Productos', 'MetodoPago', 'Clientes']
        


class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['Nombre']  