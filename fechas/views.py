from django.shortcuts import render
from .models import Fecha
from .serializers import FechaSerializer
from rest_framework import viewsets
# Create your views here.

class FechaViewSet(viewsets.ModelViewSet):
	serializer_class = FechaSerializer
	queryset = Fecha.objects.all()