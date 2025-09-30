# Archivo: 07_lectura_y_escritura_de_archivos.py
# Tema: Lectura y escritura de archivos en Python
# Descripción: Este script explica cómo leer y escribir archivos de texto en Python, incluyendo ejemplos comentados y manejo de errores.

# -------------------------------
# 📌 1. Escribir en un archivo
# -------------------------------
# Usamos 'open' con modo 'w' (escribir) o 'a' (añadir) para escribir texto en un archivo.
# El bloque 'with' asegura que el archivo se cierre automáticamente.

texto = "Hola, este es un ejemplo de escritura en un archivo.\nSegunda línea de texto."

try:
    with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print("✅ Archivo escrito correctamente.")
except Exception as e:
    print(f"❌ Error al escribir el archivo: {e}")

# -------------------------------
# 📌 2. Leer todo el contenido de un archivo
# -------------------------------
# Usamos 'open' con modo 'r' (lectura) para leer el contenido completo.

try:
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    print("📄 Contenido del archivo:")
    print(contenido)
except FileNotFoundError:
    print("❌ El archivo no existe.")
except Exception as e:
    print(f"❌ Error al leer el archivo: {e}")

# -------------------------------
# 📌 3. Leer línea por línea
# -------------------------------
# Podemos iterar sobre el archivo para leerlo línea por línea.

try:
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        print("📄 Lectura línea por línea:")
        for linea in archivo:
            print(linea.strip())  # strip() elimina saltos de línea
except Exception as e:
    print(f"❌ Error al leer línea por línea: {e}")

# -------------------------------
# 📌 4. Añadir contenido a un archivo existente
# -------------------------------
# Usamos el modo 'a' para agregar texto sin borrar el contenido anterior.

try:
    with open("ejemplo.txt", "a", encoding="utf-8") as archivo:
        archivo.write("\nNueva línea añadida al archivo.")
    print("✅ Línea añadida correctamente.")
except Exception as e:
    print(f"❌ Error al añadir contenido: {e}")

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Python permite trabajar fácilmente con archivos de texto usando 'open'.
# El uso de 'with' garantiza el cierre automático del archivo.
# Podemos leer todo el contenido, línea por línea, escribir o añadir texto.
# Es importante manejar errores para evitar fallos si el archivo no existe o hay problemas de acceso.

# Fin del archivo
