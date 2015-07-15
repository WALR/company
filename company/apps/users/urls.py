from django.conf.urls import include, url

from .views import UserPerfilView


urlpatterns = [
    # url(r'^$', InventarioView.as_view(), name='home'),
    url(r'^login/$', 'apps.users.views.userlogin', name='login'),
    url(r'^perfil/$', UserPerfilView.as_view(), name='user_perfil'),
    url(r'^salir/$', 'apps.users.views.LogOut', name='logout'),

    # url(r'^categoria/crear/$', crear_categoria, name='crear_categoria'),
    # url(r'^inventario/producto/nuevo/$',CrearProducto.as_view(), name='crear_producto'),
    # url(r'^inventario/producto/(?P<pk>\d+)/$', DetalleProducto.as_view(), name='detalle_producto'),
    # url(r'^inventario/producto/editar/(?P<pk>\d+)/$', EditarProducto.as_view(), name='editar_producto'),
    # url(r'^inventario/producto/eliminar/(?P<producto_id>\d+)/$', EliminarProducto.as_view(), name='eliminar_producto'),
    # url(r'^$', home, name='home'),
]
