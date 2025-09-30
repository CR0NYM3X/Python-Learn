# Archivo: 03_funciones_y_modulos.py
# Tema: Funciones y Módulos en Python
# Descripción: Este script explica cómo usar funciones y módulos en Python desde cero, con ejemplos comentados.

# -------------------------------
# 📌 1. ¿Qué es una función?
# -------------------------------
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define con la palabra clave 'def'.

def saludar():
    """Función simple que imprime un saludo."""
    print("¡Hola! Bienvenido a Python.")

saludar()  # Llamamos a la función


# -------------------------------
# 📌 2. Funciones con parámetros
# -------------------------------
# Podemos pasar valores a una función mediante parámetros.

def saludar_persona(nombre):
    """Saluda a la persona con su nombre."""
    print(f"Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Luis")


# -------------------------------
# 📌 3. Funciones que retornan valores
# -------------------------------
# Las funciones pueden devolver resultados usando 'return'.

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)


# -------------------------------
# 📌 4. Funciones anidadas
# -------------------------------
# Podemos definir funciones dentro de otras funciones.

def operacion_compleja(x, y):
    """Ejemplo de función anidada."""
    def multiplicar(a, b):
        return a * b
    suma = x + y
    producto = multiplicar(x, y)
    return suma, producto

suma, producto = operacion_compleja(4, 6)
print("Suma:", suma)
print("Producto:", producto)


# -------------------------------
# 📌 5. Uso de módulos estándar
# -------------------------------
# Python incluye muchos módulos útiles como 'math' y 'datetime'.

import math
import datetime

# Usando el módulo math
print("Raíz cuadrada de 16:", math.sqrt(16))
print("Valor de pi:", math.pi)

# Usando el módulo datetime
hoy = datetime.datetime.now()
print("Fecha y hora actual:", hoy)


# -------------------------------
# 📌 6. Crear e importar módulos personalizados
# -------------------------------
# Podemos crear nuestros propios módulos. Supongamos que tenemos un archivo llamado 'mimodulo.py'
# con una función llamada 'saludo_personalizado(nombre)'.

# Contenido de mimodulo.py (debe estar en el mismo directorio):
# def saludo_personalizado(nombre):
#     print(f"¡Hola desde el módulo, {nombre}!")

# Para usarlo:
# import mimodulo
# mimodulo.saludo_personalizado("Carlos")

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Las funciones y módulos permiten organizar mejor el código, reutilizarlo y hacerlo más legible.

# Fin del archivo
