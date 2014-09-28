from django.shortcuts import render
from .models import Tabla
from .serializers import TablaSerializer
from rest_framework import viewsets

class TablaViewSet(viewsets.ModelViewSet):
	serializer_class = TablaSerializer
	queryset = Tabla.objects.all()