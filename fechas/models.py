from django.db import models
from equipos.models import Equipo
# Create your models here.
class Fecha(models.Model):
	numero_fecha = models.IntegerField()
	equipo_local = models.ForeignKey(Equipo, related_name='fechas_equipo_local')
	resultado_local = models.IntegerField(blank=True)
	equipo_visitante = models.ForeignKey(Equipo, related_name='fechas_equipo_visitante')
	resultado_visitante = models.IntegerField(blank= True)


	def __unicode__(self):
		return ("%s - %s - %s") % (self.numero_fecha, self.equipo_local, self.equipo_visitante)