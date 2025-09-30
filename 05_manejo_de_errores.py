# Archivo: 05_manejo_de_errores.py
# Tema: Manejo de errores en Python (try, except)
# Descripción: Este script explica cómo manejar errores en Python usando bloques try y except, con ejemplos comentados.

# -------------------------------
# 📌 1. ¿Qué es el manejo de errores?
# -------------------------------
# El manejo de errores permite controlar situaciones inesperadas durante la ejecución del programa,
# evitando que el programa se detenga abruptamente.

# -------------------------------
# 📌 2. Uso básico de try y except
# -------------------------------
# Intentamos ejecutar un bloque de código con 'try'.
# Si ocurre un error, se captura con 'except'.

valor = "abc"  # Simulamos una entrada incorrecta

try:
    numero = int(valor)
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("❌ Error: No se pudo convertir el valor a entero.")

# -------------------------------
# 📌 3. Capturar múltiples tipos de errores
# -------------------------------
# Podemos usar múltiples bloques except para manejar distintos errores.

try:
    lista = [1, 2, 3]
    print(lista[5])  # Índice fuera de rango
except IndexError:
    print("❌ Error: El índice está fuera del rango de la lista.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")

# -------------------------------
# 📌 4. Uso de else y finally
# -------------------------------
# 'else' se ejecuta si no ocurre ningún error.
# 'finally' se ejecuta siempre, ocurra o no un error.

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("❌ No se puede dividir entre cero.")
else:
    print(f"✅ Resultado: {resultado}")
finally:
    print("🔚 Fin del bloque try-except.")

# -------------------------------
# 📌 5. Crear excepciones personalizadas
# -------------------------------
# Podemos definir nuestras propias excepciones usando la clase Exception.

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print(f"Edad válida: {edad}")

try:
    verificar_edad(-5)
except ValueError as error:
    print(f"❌ Error personalizado: {error}")

# -------------------------------
# ✅ Conclusión
# -------------------------------
# El manejo de errores con try y except permite que nuestros programas sean más robustos y seguros.
# Podemos capturar errores específicos, ejecutar código adicional con else y finally,
# e incluso definir nuestras propias excepciones.

# Fin del archivo
