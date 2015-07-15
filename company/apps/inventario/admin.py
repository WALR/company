from django.contrib import admin
from .models import Categoria, Marca, Proveedor, Sucursal, Producto
# from .actions import export_as_excel

# admin.site.register(Categoria)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'descripcion',)
	search_fields = ('nombre',)
	ordering = ('nombre', )
	# actions = [export_as_excel]


# admin.site.register(Marca)
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'descripcion',)
	search_fields = ('nombre',)
	ordering = ('nombre', )
	# actions = [export_as_excel]

# admin.site.register(Proveedor)
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'encargado', 'telefono', 'email')
	search_fields = ('nombre', 'encargado')
	ordering = ('nombre', )
	# actions = [export_as_excel]


# admin.site.register(Sucursal)
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'encargado', 'direccion','telefono', 'email')
	search_fields = ('nombre', 'encargado', 'direccion')
	ordering = ('nombre', )
	# actions = [export_as_excel]


# admin.site.register(Producto)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'descripcion', 'marca', 'existencia', 'sucursal', 'proveedor', 'categoria', 'precioVenta', 'precioCompra', 'precioPorMayor')
	search_fields = ('nombre', 'marca', 'sucursal', 'proveedor', 'categoria')
	list_filter = ('marca', 'sucursal', 'categoria', 'proveedor')
	ordering = ('nombre', )
	# actions = [export_as_excel]





# class SignUpAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__", "timestamp", "updated"]
# 	form = SignUpForm
# 	# class Meta:
# 	# 	model = SignUp


# admin.site.register(SignUp, SignUpAdmin)

# from django.contrib import admin
# from .models import User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):

# 	list_display = ('username', 'nombre', 'apellido', 'email')
# 	search_fields = ('username', 'email')
# 	list_filter = ('is_superuser', )
# 	ordering = ('username', )
# 	filter_horizontal = ('groups', 'user_permissions')
# 	actions = [export_as_excel]

# 	fieldsets = (
# 			('Usuario', {'fields' : ('username', 'password') }),
# 			('Informacion Personal', {'fields' : (
# 									'nombre', 
# 									'apellido', 
# 									'email', 
# 									'avatar'
# 								)}),
# 			('Permisos', {'fields':(
# 					'is_active',
# 					'is_staff',
# 					'is_superuser',
# 					'groups',
# 					'user_permissions',
# 				)}),
# 		)
