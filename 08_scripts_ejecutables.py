# Archivo: 07_scripts_ejecutables.py
# Tema: Scripts ejecutables en Python
# Descripción: Este script explica cómo crear y ejecutar scripts de Python como archivos ejecutables desde la terminal, incluyendo el uso de la línea shebang y permisos en sistemas Linux.

# -------------------------------
# 📌 1. ¿Qué es un script ejecutable?
# -------------------------------
# Un script ejecutable es un archivo que se puede ejecutar directamente desde la terminal sin necesidad de invocar explícitamente el intérprete de Python.

# -------------------------------
# 📌 2. Línea Shebang (#!)
# -------------------------------
# La línea shebang se coloca al inicio del archivo para indicar qué intérprete debe usarse.
# En sistemas Unix/Linux, se usa comúnmente:
#   #!/usr/bin/env python3

# Ejemplo de script ejecutable:
# --------------------------------
# #!/usr/bin/env python3
# print("¡Hola! Este script es ejecutable desde la terminal.")

# -------------------------------
# 📌 3. Hacer el archivo ejecutable (Linux/macOS)
# -------------------------------
# 1. Guardar el archivo con extensión .py, por ejemplo: hola.py
# 2. Dar permisos de ejecución con el comando:
#    chmod +x hola.py
# 3. Ejecutar el script directamente:
#    ./hola.py

# -------------------------------
# 📌 4. Consideraciones en Windows
# -------------------------------
# En Windows, los scripts .py se ejecutan con:
#    python hola.py
# También se puede asociar la extensión .py con el intérprete de Python para doble clic.

# -------------------------------
# 📌 5. Ejemplo práctico
# -------------------------------

def main():
    """Función principal del script."""
    print("Este script puede ejecutarse directamente si tiene permisos y línea shebang.")

# Punto de entrada del script
if __name__ == "__main__":
    main()

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Para crear scripts ejecutables en Python:
# - Añade la línea shebang al inicio del archivo.
# - Da permisos de ejecución en sistemas Unix/Linux.
# - Usa `if __name__ == "__main__"` para definir el punto de entrada.
# Esto permite ejecutar tus scripts de forma más flexible y profesional.

# Fin del archivo
