from django.db import models

# Create your models here.

class ArticuloTipo(models.Model):

	nombre = models.CharField(max_length=50)
	class Meta:
		verbose_name = "Tipo de articulo"
		verbose_name_plural = "Tipos de articulo"

	def __str__(self):
		return self.nombre

class Etiqueta(models.Model):
	nombre = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Etiqueta"
		verbose_name_plural = "Etiquetas"

	def __str__(self):
		return self.nombre
        
class Articulo(models.Model):
	# TODO: Define fields here
	titulo = models.CharField(max_length=200)
	fecha = models.DateField()
	categoria = models.ForeignKey(ArticuloTipo)
	autor = models.CharField(max_length=50)
	contenido_pri = models.TextField('contenido principal')
	contenido_ext = models.TextField('contenido extendido')
	imagen_pri = models.ImageField('imagen principal')
	slug = models.SlugField()
	etiqueta = models.ManyToManyField(Etiqueta)
	class Meta:
		verbose_name = "Articulo"
		verbose_name_plural = "Articulos"

	def __str__(self):
		pass

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*args, **kwargs)

    # TODO: Define custom methods here

    