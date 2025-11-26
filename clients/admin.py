from django.contrib import admin
from .models import TipoDocumento, Cliente, Compra


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("numero_documento", "nombres", "apellidos", "correo", "telefono", "tipo_documento")
    search_fields = ("numero_documento", "nombres", "apellidos", "correo")
    list_filter = ("tipo_documento",)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("cliente", "fecha", "monto")
    search_fields = ("cliente__numero_documento", "cliente__nombres", "cliente__apellidos")
    list_filter = ("fecha",)