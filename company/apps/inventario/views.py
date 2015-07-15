from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin, GroupRequiredMixin

from .models import Categoria, Proveedor, Producto
from .forms import CategoriaForm, ProductoForm
from apps.users.models import User


# def home(request):
# 	producto = Producto.objects.all()
# 	return render(request, "inventario.html", {'producto' : producto})

class InventarioView(TemplateView):

	template_name = 'inventario.html'


	def get_context_data(self, **kwargs):
	    context = super(InventarioView, self).get_context_data(**kwargs)
	    context['producto'] = Producto.objects.all()
	    # context['cantidad_producto'] = context['producto'].count()
	    return context

def crear_categoria(request):
	if request.method == 'POST':
		modelForm = CategoriaForm(request.POST)
		if modelForm.is_valid():
			modelForm.save()
			return redirect(reverse('inventario_app:crear_categoria'))
	else:
		modelForm = CategoriaForm()
		return render(request, 'categoria/crear_categoria.html', {'form' : modelForm})

# def crear_producto(request):
# 	if request.method == 'POST':
# 		modelForm = ProductoForm(request.POST, request.FILES)
# 		if modelForm.is_valid():
# 			modelForm.save()
# 			return redirect(reverse('inventario_app:inventario'))
# 	else:
# 		modelForm = ProductoForm()

# 	return render(request, 'producto/crear_producto.html', {'form' : modelForm})

class CrearProducto(LoginRequiredMixin, CreateView):

	form_class = ProductoForm
	template_name = 'producto/crear_producto.html'
	success_url = reverse_lazy('inventario_app:inventario')
	login_url = "/login/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CrearProducto, self).form_valid(form)


# def detalle_producto(request, producto_id):
# 	producto = get_object_or_404(Producto, pk=producto_id)
# 	return render(request, 'producto/detalle_producto.html', { 'producto' : producto})

class DetalleProducto(LoginRequiredMixin, DetailView):

	template_name = 'producto/detalle_producto.html'
	model = Producto
	login_url = "/login/"


# def editar_producto(request, producto_id):
# 	producto = get_object_or_404(Producto, pk=producto_id)

# 	if request.method == 'POST':
# 		modelForm = ProductoForm(request.POST, request.FILES, instance=producto)
# 		if modelForm.is_valid():
# 			modelForm.save()
# 			return redirect(reverse('inventario_app:inventario'))
# 	else:
# 		modelForm = ProductoForm(instance=producto)

# 	return render(request, 'producto/editar_producto.html', {'form' : modelForm, 'producto':producto})

class EditarProducto(LoginRequiredMixin, UpdateView):

	template_name = 'producto/editar_producto.html'
	success_url = reverse_lazy('inventario_app:inventario')
	model = Producto
	form_class = ProductoForm
	login_url = "/login/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(EditarProducto, self).form_valid(form)

# def eliminar_producto(request, producto_id):
# 	producto = get_object_or_404(Producto, pk=producto_id)

# 	if request.method == 'POST':
# 		producto.delete()
# 		return redirect(reverse('inventario_app:inventario'))

# 	return render(request, 'producto/eliminar_producto.html', {'producto':producto})

class EliminarProducto(LoginRequiredMixin, GroupRequiredMixin, DeleteView):

	template_name = 'producto/eliminar_producto.html'
	model = Producto
	success_url = reverse_lazy('inventario_app:inventario')
	context_object_name = 'producto'
	group_required = [u"cajero", u"admin"]
	login_url = "/login/"
