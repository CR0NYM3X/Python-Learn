# Archivo: 06_librerias_comunes.py
# Tema: Uso de librerías comunes en Python
# Descripción: Este script explica cómo utilizar algunas librerías estándar de Python como os, shutil, datetime, entre otras, con ejemplos comentados.

# -------------------------------
# 📁 1. Módulo os
# -------------------------------
# El módulo 'os' permite interactuar con el sistema operativo.
import os

# Obtener el directorio actual
directorio_actual = os.getcwd()
print(f"📂 Directorio actual: {directorio_actual}")

# Listar archivos en el directorio actual
archivos = os.listdir()
print(f"📄 Archivos en el directorio: {archivos}")

# -------------------------------
# 📦 2. Módulo shutil
# -------------------------------
# El módulo 'shutil' permite realizar operaciones de alto nivel con archivos y directorios.
import shutil

# Copiar un archivo (ejemplo: copiar este script a una copia)
# shutil.copy('06_librerias_comunes.py', '06_librerias_comunes_copia.py')
print("✅ Ejemplo de copia de archivo con shutil (comentado para evitar errores si no existe el archivo).")

# -------------------------------
# 🕒 3. Módulo datetime
# -------------------------------
# El módulo 'datetime' permite trabajar con fechas y horas.
from datetime import datetime, timedelta

# Obtener la fecha y hora actual
ahora = datetime.now()
print(f"🕒 Fecha y hora actual: {ahora}")

# Crear una fecha específica
fecha_especifica = datetime(2023, 1, 1)
print(f"📅 Fecha específica: {fecha_especifica}")

# Sumar días a una fecha
nueva_fecha = ahora + timedelta(days=5)
print(f"📅 Fecha dentro de 5 días: {nueva_fecha}")

# -------------------------------
# 🔢 4. Módulo random
# -------------------------------
# El módulo 'random' permite generar números aleatorios.
import random

numero_aleatorio = random.randint(1, 100)
print(f"🎲 Número aleatorio entre 1 y 100: {numero_aleatorio}")

# -------------------------------
# 📊 5. Módulo math
# -------------------------------
# El módulo 'math' proporciona funciones matemáticas.
import math

raiz = math.sqrt(16)
print(f"🧮 Raíz cuadrada de 16: {raiz}")

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Estas librerías estándar de Python permiten realizar tareas comunes como manipulación de archivos,
# manejo de fechas, generación de números aleatorios y cálculos matemáticos.

# Fin del archivo
