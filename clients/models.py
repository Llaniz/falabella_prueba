from django.db import models

class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=10, unique=True)  # CC, NIT, PAS
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=30, unique=True)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    correo = models.EmailField()
    telefono = models.CharField(max_length=30)

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.numero_documento})"


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="compras")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Compra de {self.monto} — Cliente {self.cliente.numero_documento}"

