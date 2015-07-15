from django.conf.urls import include, url
from .views import InventarioView, CrearProducto, crear_categoria, DetalleProducto, EditarProducto, EliminarProducto


urlpatterns = [
    # url(r'^', include(admin.site.urls)),
    url(r'^$', InventarioView.as_view(), name='home'),
    url(r'^inventario/$', InventarioView.as_view(), name='inventario'),
    url(r'^categoria/crear/$', crear_categoria, name='crear_categoria'),
    url(r'^inventario/producto/nuevo/$',CrearProducto.as_view(), name='crear_producto'),
    url(r'^inventario/producto/(?P<pk>\d+)/$', DetalleProducto.as_view(), name='detalle_producto'),
    url(r'^inventario/producto/editar/(?P<pk>\d+)/$', EditarProducto.as_view(), name='editar_producto'),
    url(r'^inventario/producto/eliminar/(?P<slug>[-\w]+)/$', EliminarProducto.as_view(), name='eliminar_producto'),
    # url(r'^$', home, name='home'),
]
