# Archivo: 06_programacion_orientada_a_objetos.py
# Tema: Programación Orientada a Objetos (OOP) en Python
# Descripción: Este script explica los conceptos fundamentales de la Programación Orientada a Objetos en Python desde cero, con ejemplos comentados.

# -------------------------------
# 📌 1. ¿Qué es la Programación Orientada a Objetos?
# -------------------------------
# Es un paradigma de programación que organiza el código en "objetos", que son instancias de "clases".
# Permite modelar entidades del mundo real con atributos (datos) y métodos (comportamientos).

# -------------------------------
# 📌 2. Definición de una clase
# -------------------------------
# Una clase es una plantilla para crear objetos. Se define con la palabra clave 'class'.

class Persona:
    """Clase que representa a una persona."""

    # Método constructor: se ejecuta al crear un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    # Método de instancia
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# -------------------------------
# 📌 3. Crear objetos
# -------------------------------
# Un objeto es una instancia de una clase.

persona1 = Persona("Ana", 30)
persona1.saludar()  # Llamamos al método saludar del objeto

# -------------------------------
# 📌 4. Herencia
# -------------------------------
# Permite que una clase herede atributos y métodos de otra clase.

class Empleado(Persona):
    """Clase que hereda de Persona y añade nuevos atributos."""

    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.puesto = puesto

    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.puesto}.")

empleado1 = Empleado("Luis", 25, "Ingeniero")
empleado1.saludar()
empleado1.trabajar()

# -------------------------------
# 📌 5. Encapsulamiento
# -------------------------------
# Es el principio de ocultar detalles internos de una clase.
# Se puede usar un guion bajo (_) para indicar que un atributo es privado.

class CuentaBancaria:
    """Clase que representa una cuenta bancaria."""

    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es ${self._saldo}")

    def depositar(self, cantidad):
        self._saldo += cantidad
        print(f"Se depositaron ${cantidad}. Nuevo saldo: ${self._saldo}")

cuenta = CuentaBancaria("Carlos", 1000)
cuenta.mostrar_saldo()
cuenta.depositar(500)

# -------------------------------
# ✅ Conclusión
# -------------------------------
# La Programación Orientada a Objetos permite estructurar el código de forma más clara y reutilizable.
# Los conceptos clave son: clases, objetos, atributos, métodos, herencia y encapsulamiento.
# Este paradigma es ampliamente utilizado en el desarrollo de software moderno.

# Fin del archivo
