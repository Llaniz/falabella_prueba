import pandas as pd
from io import BytesIO, StringIO
from datetime import date, timedelta

def generar_archivo_cliente(cliente, formato="csv"):
    """
    cliente: objeto Cliente con .compras prefetched
    formato: 'csv' o 'xlsx'
    """

    info_cliente = {
        "Numero de documento": cliente.numero_documento,
        "Tipo de documento": cliente.tipo_documento.nombre,
        "Nombres": cliente.nombres,
        "Apellidos": cliente.apellidos,
        "Correo": cliente.correo,
        "Telefono": cliente.telefono,
    }

    # se pasa a df (1 fila)
    df_cliente = pd.DataFrame([info_cliente])

    # Crear archivo en memoria
    if formato == "csv":
        buffer = StringIO()
        df_cliente.to_csv(buffer, index=False, encoding="utf-8")
        buffer.seek(0)
        return buffer.getvalue(), "text/csv"

    elif formato == "xlsx":
        buffer = BytesIO()
        df_cliente.to_excel(buffer, index=False)
        buffer.seek(0)
        return buffer.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    else:
        raise ValueError("Formato inválido")




def obtener_rango_mes_pasado():
    # se obtiene el rango de fechas del mes pasado
    hoy = date.today()
    primer_dia_mes_actual = hoy.replace(day=1)
    ultimo_dia_mes_pasado = primer_dia_mes_actual - timedelta(days=1)
    primer_dia_mes_pasado = ultimo_dia_mes_pasado.replace(day=1)
    return primer_dia_mes_pasado, ultimo_dia_mes_pasado


def generar_reporte_fidelizacion(clientes_compras):

    df = pd.DataFrame(clientes_compras)

    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)

    return buffer.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

