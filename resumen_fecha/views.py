from django.shortcuts import render
from .models import Resumen_Fecha
from .serializers import ResumenSerializer
from rest_framework import viewsets

class ResumenViewSet(viewsets.ModelViewSet):
	serializer_class = ResumenSerializer
	queryset = Resumen_Fecha.objects.all()
