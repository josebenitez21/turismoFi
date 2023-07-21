from django.contrib import admin
from .models import Canton, Provincia, Parroquia,Catalogo,Establecimiento,EstablecimientoRegistro,Items

admin.site.register(Canton)
admin.site.register(Provincia)
admin.site.register(Parroquia)
admin.site.register(Catalogo)
admin.site.register(Establecimiento)
admin.site.register(EstablecimientoRegistro)
admin.site.register(Items)