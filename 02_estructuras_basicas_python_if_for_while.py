
# `if`, `elif`, `else`
edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres niño.")



# `for` Se usa para iterar sobre secuencias (listas, cadenas, rangos, etc.).
# `foreach` (equivalente a `for` en Python) En Python, el `for` ya actúa como un `foreach`.
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)

 

# `while` Ejecuta un bloque de código mientras una condición sea verdadera.
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1


###  `do while` (simulado en Python) Python no tiene `do while`, pero se puede simular con `while True` y `break`.    
# Simulación de do-while
while True:
    numero = int(input("Ingresa un número mayor a 10: "))
    if numero > 10:
        print("¡Correcto!")
        break
