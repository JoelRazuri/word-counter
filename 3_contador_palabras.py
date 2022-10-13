"""
    Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia e imprimimos en 
    la salida el resultado.

    Ejemplo:

    Pregunta: ¿En qué estás pensando?
    Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
    Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!
"""

import os 

contador = 1
frase = input("En que estas pensando?: ")
print()

for i in range(len(frase)):
    if frase[i]==" ":
        contador+=1

print(f"Entrada: {frase}")
print(f"Salida: Muy bien, tu me has mostrado tu pensamiento en {contador} palabras.")
print()
input("Ingrese cualquier tecla para salir..")


