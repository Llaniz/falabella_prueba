## Prueba Técnica (Falabella Colombia) - Daniel Suarez

Aplicación web para el equipo de SAC que permite:

- Consultar la información de un cliente ingresando solo su número de documento.
- Exportar la información del cliente a archivo (CSV/Excel).
- Generar un reporte de fidelización en Excel con los clientes cuyo total de compras del último mes supera los 5’000.000 COP.

Backend en **Python/Django + Django REST Framework**, frontend web básico con HTML + JavaScript, base de datos **SQLite** y uso de **pandas** para generación de reportes.

---

### 1. Requisitos previos

- Python 3.13 (o 3.10+ compatible con Django 5.x)
- Git
- Pip (gestor de paquetes de Python)

Opcional pero recomendado:
- Virtualenv / venv

---

### 2. Clonado del proyecto


- `git clone https://github.com/Llaniz/falabella_prueba.git`
- `cd falabella_prueba`

---

### 3. Instalación y configuración

#### 3.1. Crear y activar entorno virtual

- `python -m venv venv`
# Windows:
- `venv\Scripts\activate`
# Linux / macOS:
- `source venv/bin/activate`

#### 3.2. Instalar dependencias

- `pip install -r requirements.txt`

#### 3.3. Migrar la base de datos

Desde la carpeta raíz del proyecto:

- `python manage.py migrate`

#### 3.4. Crear superusuario para el admin de Django

- `python manage.py createsuperuser`

Sigue las instrucciones (usuario, correo, contraseña).

---

### 4. Carga de datos de prueba

1. Levanta el servidor:

  
- `python manage.py runserver`
   2. Entra al admin: `http://127.0.0.1:8000/admin/` e inicia sesión con el superusuario.

3. Crea registros en este orden:

   - `TipoDocumento`  
     - Ejemplo:
       - `codigo=1`, `nombre=Cédula`
       - `codigo=2`, `nombre=NIT`
       - `codigo=3`, `nombre=Pasaporte`
   - `Cliente`  
     - Campos: tipo_documento, número_documento, nombres, apellidos, correo, teléfono.
   - `Compra`  
     - Campos: cliente, fecha, monto, descripción.  
     - Asegúrate de crear al menos un cliente con compras que en el **último mes** sumen más de **5’000.000 COP** para probar el reporte de fidelización.

> La base de datos se almacena en `db.sqlite3` en la raíz del proyecto.

---

### 5. Ejecución de la aplicación

Con el entorno virtual activado:

python manage.py runserver- Frontend: `http://127.0.0.1:8000/`
- Admin Django: `http://127.0.0.1:8000/admin/`
- Endpoints API (principales):
  - `GET /api/clientes/?numero_documento=NUMERO`
  - `GET /api/exportar-cliente/?numero_documento=NUMERO&formato=csv`
  - `GET /api/reporte-fidelizacion/`

---

### 6. Video de la aplicación

El video se encuentra disponible en el siguiente enlace https://youtu.be/o1ARFpaOJzA
