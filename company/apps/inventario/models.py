from django.db import models
from django.template.defaultfilters import slugify

from django.conf import settings


class TimeStampModel(models.Model):

	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	slug = models.SlugField(editable=False, blank=True, null=True)
	descripcion = models.TextField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre


class Marca(models.Model):
	nombre = models.CharField(max_length=100)
	slug = models.SlugField(editable=False, blank=True, null=True)
	descripcion = models.TextField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Marca, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre



class Proveedor(TimeStampModel):
	nombre = models.CharField(max_length=100)
	encargado = models.CharField(max_length=100)
	telefono = models.PositiveIntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)


	def __unicode__(self):
		return self.nombre


class Sucursal(TimeStampModel):
	nombre = models.CharField(max_length=100)
	encargado = models.ForeignKey(settings.AUTH_USER_MODEL)
	direccion = models.CharField(max_length=100)
	telefono = models.PositiveIntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)

	def __unicode__(self):
		return self.nombre


class Producto(TimeStampModel):
	barcode = models.PositiveIntegerField(blank=True, null=True)
	nombre = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(editable=False, blank=True, null=True)
	descripcion = models.TextField(blank=True, null=True)
	marca = models.ForeignKey(Marca, blank=True, null=True)
	existencia = models.PositiveIntegerField(blank=True, null=True)
	precioVenta = models.DecimalField(max_digits=6, decimal_places=2)
	precioCompra = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	precioPorMayor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	imagen = models.ImageField(upload_to = 'producto', blank=True, null=True)

	sucursal = models.ForeignKey(Sucursal, blank=True)
	proveedor = models.ForeignKey(Proveedor, blank=True)
	categoria = models.ForeignKey(Categoria)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	# creado = models.DateTimeField(auto_now_add=True)
	# actualizado = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Producto, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre
