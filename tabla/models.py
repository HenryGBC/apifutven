from django.db import models
from equipos.models import Equipo
# Create your models here.
class Tabla(models.Model):
	equipo = models.ForeignKey(Equipo)
	partidos_jugados 	= models.IntegerField()
	partidos_ganados 	= models.IntegerField()
	partidos_empatados	= models.IntegerField()
	partidos_perdidos 	= models.IntegerField()
	puntos				= models.IntegerField()

	def __unicode__(self):
		return self.equipo
