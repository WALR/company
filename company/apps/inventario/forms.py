from django import forms
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		exclude = ('slug',)


class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ('slug',)
		widgets = {
			'barcode' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '2'}),
			'marca' : forms.Select(attrs={'class' : 'form-control'}),
			'existencia' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'precioVenta' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'precioCompra' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'precioPorMayor' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'imagen' : forms.FileInput(attrs={'class' : 'form-control'}),

			'sucursal' : forms.Select(attrs={'class' : 'form-control'}),
			'proveedor' : forms.Select(attrs={'class' : 'form-control'}),
			'categoria' : forms.Select(attrs={'class' : 'form-control'}),
			'user' : forms.Select(attrs={'class' : 'form-control'})
		}
