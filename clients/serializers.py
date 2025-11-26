from rest_framework import serializers
from .models import Cliente, Compra, TipoDocumento


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ["id", "codigo", "nombre"]


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ["id", "fecha", "monto", "descripcion"]


class ClienteSerializer(serializers.ModelSerializer):
    tipo_documento = TipoDocumentoSerializer()
    compras = CompraSerializer(many=True)

    class Meta:
        model = Cliente
        fields = [
            "id",
            "tipo_documento",
            "numero_documento",
            "nombres",
            "apellidos",
            "correo",
            "telefono",
            "compras",
        ]
