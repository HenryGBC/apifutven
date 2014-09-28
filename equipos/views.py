from django.shortcuts import render
from .models import Equipo
from .serializers import EquipoSerializer
from rest_framework import viewsets

class EquipoViewSet(viewsets.ModelViewSet):
	serializer_class = EquipoSerializer
	queryset = Equipo.objects.all()

	 