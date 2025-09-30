# Archivo: 06_automatizacion_archivos_y_carpetas.py
# Tema: Automatización de archivos y carpetas en Python
# Descripción: Este script muestra cómo automatizar tareas comunes con archivos y carpetas usando el módulo 'os' y 'shutil'.

# -------------------------------
# 📁 1. Crear carpetas y subcarpetas
# -------------------------------
import os

# Crear una carpeta llamada 'proyecto'
os.makedirs('proyecto/subcarpeta', exist_ok=True)
print("Carpetas creadas: proyecto/subcarpeta")

# -------------------------------
# 📄 2. Crear y escribir en archivos
# -------------------------------
# Crear un archivo de texto dentro de la carpeta
ruta_archivo = 'proyecto/subcarpeta/archivo.txt'

with open(ruta_archivo, 'w') as archivo:
    archivo.write("Este es un archivo creado automáticamente.\n")
    archivo.write("Puedes escribir múltiples líneas.\n")

print(f"Archivo creado y escrito: {ruta_archivo}")

# -------------------------------
# 📂 3. Listar archivos en una carpeta
# -------------------------------
# Listar el contenido de la carpeta 'proyecto'
contenido = os.listdir('proyecto')
print("Contenido de la carpeta 'proyecto':", contenido)

# -------------------------------
# 🔄 4. Mover y copiar archivos
# -------------------------------
import shutil

# Copiar el archivo a otra carpeta
os.makedirs('proyecto/copia', exist_ok=True)
shutil.copy(ruta_archivo, 'proyecto/copia/archivo_copiado.txt')
print("Archivo copiado a: proyecto/copia/archivo_copiado.txt")

# -------------------------------
# ❌ 5. Eliminar archivos y carpetas
# -------------------------------
# Eliminar archivo copiado
os.remove('proyecto/copia/archivo_copiado.txt')
print("Archivo eliminado: proyecto/copia/archivo_copiado.txt")

# Eliminar carpeta vacía
os.rmdir('proyecto/copia')
print("Carpeta eliminada: proyecto/copia")

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Python permite automatizar tareas de gestión de archivos y carpetas fácilmente.
# Los módulos 'os' y 'shutil' son esenciales para crear, mover, copiar y eliminar archivos de forma programática.

# Fin del archivo
