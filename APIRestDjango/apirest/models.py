from django.db import models

# Create your models here.
class Cliente(models.Model):
    

    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    celular=models.CharField(max_length=20, null=True)
    sexo=models.CharField(max_length=7)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def _str_(self):
        return self.nombres

class Pregunta(models.Model):

    preguntas=models.CharField(max_length=90)
    respuestas=models.CharField(max_length=80)

    class Meta:
        verbose_name = ("Pregunta")
        verbose_name_plural = ("Preguntas")

    def __str__(self):
        return self.preguntas
      