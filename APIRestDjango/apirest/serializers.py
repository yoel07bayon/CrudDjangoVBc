from rest_framework import serializers
from .models import Cliente

from .models import Pregunta

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Cliente
        fields=['id','nombres','apellidos','dni','celular','sexo']

        
class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Pregunta
        fields=['id','preguntas','respuestas']     

        