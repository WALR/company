from django.contrib import admin
from .models import User
from .actions import export_as_excel

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

	list_display = ('username', 'nombre', 'apellido', 'email')
	search_fields = ('username', 'email')
	list_filter = ('is_superuser', )
	ordering = ('username', )
	filter_horizontal = ('groups', 'user_permissions')
	actions = [export_as_excel]

	fieldsets = (
			('Usuario', {'fields' : ('username', 'password') }),
			('Informacion Personal', {'fields' : (
									'nombre', 
									'apellido', 
									'email', 
									'avatar'
								)}),
			('Permisos', {'fields':(
					'is_active',
					'is_staff',
					'is_superuser',
					'groups',
					'user_permissions',
				)}),
		)