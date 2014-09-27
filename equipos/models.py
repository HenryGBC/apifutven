from django.db import models

# Create your models here.
class Equipo (models.Model):
	nombre = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=100)
	estadio = models.CharField(max_length=100)
	capacidad = models.CharField(max_length=15)

	def __unicode__(self):
		return self.nombre

