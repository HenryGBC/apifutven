from django.db import models

# Create your models here.
class Resumen_Fecha(models.Model):
	numero_fecha = models.IntegerField()
	partidos_jugados = models.IntegerField()
	goles_locales = models.IntegerField()
	goles_visitantes = models.IntegerField()
	promedio_gol = models.FloatField(default=None, null= True)
	victoria_locales = models.IntegerField()
	victoria_visitantes = models.IntegerField()

	def __unico__(self):
		return self.numero_fecha
