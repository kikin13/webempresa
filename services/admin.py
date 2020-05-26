from django.contrib import admin
# Importamos el modelo creado de Service
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    # Campos de solo lectura created y updated
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
