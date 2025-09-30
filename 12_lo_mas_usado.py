# Archivo: 09_credenciales_logs_validacion.py
# Tema: Uso de variables de entorno, logs, validación de datos y argumentos con dotenv, logging y argparse
# Descripción: Este script muestra cómo manejar credenciales con variables de entorno, registrar logs, validar datos antes de insertar en PostgreSQL y aceptar argumentos desde la terminal.

# -------------------------------
# 📌 1. Uso de variables de entorno con dotenv
# -------------------------------
# Instalar dotenv: pip install python-dotenv
# python-dotenv en Python se utiliza para cargar variables de entorno desde un archivo .env 
# al entorno de ejecución de tu aplicación. Esto es especialmente útil para mantener configuraciones 
# sensibles (como contraseñas, claves API, rutas, etc.) fuera del código fuente, lo que mejora la seguridad y la portabilidad.

# Archivo .env
'''
DB_USER=admin
DB_PASSWORD=secreta123
API_KEY=abc123xyz
'''

import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env   en el directorio actua
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# -------------------------------
# 📌 2. Configuración de logs con logging
#  sirve para registrar mensajes de log (registro) durante la ejecución de un programa.
#  Es una herramienta muy útil para depurar, monitorear y entender el comportamiento de tu aplicación 
# -------------------------------
import logging

# Configurar el logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Usar diferentes niveles
logging.debug("Este es un mensaje de depuración")
logging.info("Inicio del programa")
logging.warning("Advertencia: algo no está bien")
logging.error("Error: no se pudo conectar a la base de datos")
logging.critical("Error crítico: sistema caído")


# -------------------------------
# 📌 3. Validación de datos antes de insertar
# -------------------------------
def validar_empleado(nombre, edad):
    """Valida que el nombre no esté vacío y la edad sea positiva."""
    if not nombre or not isinstance(nombre, str):
        logging.error("Nombre inválido.")
        return False
    if not isinstance(edad, int) or edad <= 0:
        logging.error("Edad inválida.")
        return False
    return True

# -------------------------------
# 📌 4. Conexión y operación con psycopg2
# -------------------------------
import psycopg2

def insertar_empleado(nombre, edad):
    """Inserta un empleado en la base de datos si los datos son válidos."""
    if not validar_empleado(nombre, edad):
        logging.warning("Datos inválidos. No se insertó el empleado.")
        return

    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO empleados (nombre, edad) VALUES (%s, %s);", (nombre, edad))
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Empleado {nombre} insertado correctamente.")
    except Exception as e:
        logging.error(f"Error al insertar empleado: {e}")

# -------------------------------
# 📌 5. Uso de argparse para argumentos desde terminal
# -------------------------------
import argparse

def main():
    parser = argparse.ArgumentParser(description="Insertar empleado en PostgreSQL.")
    parser.add_argument("--nombre", required=True, help="Nombre del empleado")
    parser.add_argument("--edad", type=int, required=True, help="Edad del empleado")
    args = parser.parse_args()

    insertar_empleado(args.nombre, args.edad)

# Punto de entrada del script
if __name__ == "__main__":
    main()

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Este script demuestra buenas prácticas:
# - Uso de variables de entorno para proteger credenciales.
# - Registro de eventos y errores con logging.
# - Validación de datos antes de operaciones críticas.
# - Uso de argparse para recibir parámetros desde la terminal.

# Fin del archivo
