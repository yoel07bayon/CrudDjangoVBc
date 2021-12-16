from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer

from .serializers import PreguntaSerializer
from .models import Cliente

from .models import Pregunta


class ClienteViewSet(viewsets.ModelViewSet):
    queryset=Cliente.objects.all();
    serializer_class=ClienteSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset=Pregunta.objects.all();
    serializer_class=PreguntaSerializer

# Create your views here.
