from django.contrib import admin

from myapps.mascota.models import Mascota, Vacuna

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)