from django.urls import path
from .views import ClientePorDocumentoView, ExportarClienteView, ReporteFidelizacionView

urlpatterns = [
    path("clientes/", ClientePorDocumentoView.as_view(), name="cliente-por-documento"),
    path("exportar-cliente/", ExportarClienteView.as_view(), name="exportar-cliente"),
    path("reporte-fidelizacion/", ReporteFidelizacionView.as_view(), name="reporte-fidelizacion"),
]
