from django.contrib import admin

from .models import Cliente

from .models import Pregunta


#admin.site.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'celular', 'sexo')

admin.site.register(Cliente,ClienteAdmin)


admin.site.register(Pregunta)
#class PreguntaAdmin (admin.ModelAdmin):
    #list_display = ('preguntas','respuestas')

#admin.site.register(Pregunta,PreguntaAdmin)

