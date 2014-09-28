from rest_framework import serializers
from .models import Tabla


class TablaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tabla
		fields = ('id', 'equipo', 'partidos_jugados', 'partidos_ganados', 'partidos_empatados', 'partidos_perdidos', 'puntos')

