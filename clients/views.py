from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import Cliente, TipoDocumento, Compra
from .serializers import ClienteSerializer, TipoDocumentoSerializer
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from django.db.models import Sum
from .utils import generar_archivo_cliente, obtener_rango_mes_pasado, generar_reporte_fidelizacion

def home(request):
    return render(request, "index.html")

class ClientePorDocumentoView(APIView):
    def get(self, request):
        numero_documento = request.query_params.get("numero_documento", None)

        if not numero_documento:
            return Response(
                {"error": "Debe enviar el parámetro numero_documento"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cliente = (
                Cliente.objects
                .prefetch_related("compras")
                .select_related("tipo_documento")
                .get(numero_documento=numero_documento)
            )
        except Cliente.DoesNotExist:
            return Response(
                {"error": "Cliente no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClienteSerializer(cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListaTiposDocumentoView(ListAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class ExportarClienteView(APIView):
    def get(self, request):
        numero_documento = request.query_params.get("numero_documento")
        formato = request.query_params.get("formato", "csv") 

        if not numero_documento:
            return Response({"error": "Debe enviar numero_documento"}, status=400)

        try:
            cliente = (
                Cliente.objects
                .select_related("tipo_documento")
                .get(numero_documento=numero_documento)
            )
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=404)

        contenido, mime = generar_archivo_cliente(cliente, formato)

        extension = "csv" if formato == "csv" else "xlsx"
        nombre_archivo = f"cliente_{cliente.numero_documento}.{extension}"

        response = HttpResponse(contenido, content_type=mime)
        response["Content-Disposition"] = f'attachment; filename="{nombre_archivo}"'

        return response


class ReporteFidelizacionView(APIView):
    def get(self, request):

        fecha_inicio, fecha_fin = obtener_rango_mes_pasado()

        compras = (
            Compra.objects
            .filter(fecha__range=[fecha_inicio, fecha_fin])
            .values("cliente")
            .annotate(total_mes=Sum("monto"))
            .filter(total_mes__gt=5000000)
        )

        if not compras:
            return Response({"mensaje": "No hay clientes para fidelizar este mes"}, status=200)

        clientes_compras = []

        for item in compras:
            cliente = Cliente.objects.get(id=item["cliente"])
            clientes_compras.append({
                "Número de documento": cliente.numero_documento,
                "Tipo de documento": cliente.tipo_documento.nombre,
                "Nombres": cliente.nombres,
                "Apellidos": cliente.apellidos,
                "Correo": cliente.correo,
                "Teléfono": cliente.telefono,
                "Total compras mes": item["total_mes"],
            })

        contenido, mime = generar_reporte_fidelizacion(clientes_compras)

        nombre_archivo = f"reporte_fidelizacion_{fecha_inicio.month}-{fecha_inicio.year}.xlsx"
        response = HttpResponse(contenido, content_type=mime)
        response["Content-Disposition"] = f'attachment; filename="{nombre_archivo}"'

        return response
