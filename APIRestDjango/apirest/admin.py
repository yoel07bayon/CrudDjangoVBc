from django.contrib import admin

from .models import Cliente


#admin.site.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'celular', 'email')

admin.site.register(Cliente,ClienteAdmin)

