from rest_framework import serializers
from .models import Resumen_Fecha


class ResumenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resumen_Fecha
		fields = ('id','numero_fecha','partidos_jugados','goles_locales','goles_visitantes','promedio_gol','victoria_locales','victoria_visitantes')