from rest_framework import serializers
from .models import Fecha



class FechaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fecha
		fields = ('id', 'numero_fecha','equipo_local','resultado_local','equipo_visitante','resultado_visitante',)












