# Archivo: 06_estructuras_de_datos.py
# Tema: Listas, Diccionarios, Tuplas y Sets en Python
# Descripción: Este script explica las principales estructuras de datos en Python con ejemplos comentados.

# -------------------------------
# 📌 1. Listas (list)
# -------------------------------
# Las listas son colecciones ordenadas y mutables. Se definen con corchetes [].

frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", frutas)

# Acceder a elementos
print("Primera fruta:", frutas[0])

# Agregar elementos
frutas.append("naranja")
print("Lista actualizada:", frutas)

# Eliminar elementos
frutas.remove("banana")
print("Lista después de eliminar:", frutas)

# -------------------------------
# 📌 2. Diccionarios (dict)
# -------------------------------
# Los diccionarios almacenan pares clave-valor. Se definen con llaves {}.

persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario persona:", persona)

# Acceder a valores
print("Nombre:", persona["nombre"])

# Agregar o modificar valores
persona["edad"] = 31
persona["profesion"] = "Ingeniera"
print("Diccionario actualizado:", persona)

# -------------------------------
# 📌 3. Tuplas (tuple)
# -------------------------------
# Las tuplas son colecciones ordenadas e inmutables. Se definen con paréntesis ().

coordenadas = (10.5, 20.3)
print("Tupla coordenadas:", coordenadas)

# Acceder a elementos
print("Latitud:", coordenadas[0])

# Las tuplas no se pueden modificar directamente

# -------------------------------
# 📌 4. Sets (set)
# -------------------------------
# Los sets son colecciones no ordenadas y sin elementos duplicados. Se definen con llaves {} o la función set().

numeros = {1, 2, 3, 2, 1}
print("Set de números (sin duplicados):", numeros)

# Agregar elementos
numeros.add(4)
numeros.add(1)
print("Set actualizado:", numeros)

# Eliminar elementos
numeros.discard(2)
print("Set después de eliminar:", numeros)

# -------------------------------
# ✅ Conclusión
# -------------------------------
# Python ofrece varias estructuras de datos para organizar la información:
# - Las listas son útiles para colecciones ordenadas y modificables.
# - Los diccionarios permiten asociar claves con valores.
# - Las tuplas son ideales para datos constantes.
# - Los sets son útiles para eliminar duplicados y realizar operaciones de conjuntos.

# Fin del archivo
