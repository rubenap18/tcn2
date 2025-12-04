# Sistema Gestor de Venta de Boletos de Autobus - Transportes Cuervo Negro

Sistema de gestion de boletos de autobus desarrollado en Python con arquitectura MVC (Model-View-Controller) y PySide6 como libreria de Interfaz Grafica.

## Instalacion y Ejecucion

Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1. Requisitos Previos
* Python 3.8+
* Servidor MySQL/MariaDB (debe estar corriendo en `localhost:3306`)
* De ser necesario, puedes cambiar las variables de entorno para la conexion con la BD en el archvo `config.py`
* Una vez iniciado el servidor de BD, ejecuta el archivo `dao/tcn_database.sql` en el Gestor de BBDD. 

### 2. Configuracion del Entorno Virtual (venv)
```bash
# Crea el entorno virtual, la terminal debe estar abierta en la raiz del proyecto.
python -m venv .venv

# Activa el entorno virtual (Linux o macOS)
source .venv/bin/activate
# Activa el entorno virtual (Windows)
.\.venv\Scripts\activate
```

### 3. Instalacion de Dependencias
Una vez activado el entorno virtual, instala todas las librerías necesarias del proyecto:
```bash
pip install -r requerimientos.txt
```

### 4. Ejecuta el archivo main.py
```bash
python main.py
```
