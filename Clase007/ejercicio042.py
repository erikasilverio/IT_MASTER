"""
Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

"""

import random


sumador = 0
contador = 0 # O contador se va a cero, porque vamos a sacar um promedio
numero = random.randint(0,10)




while numero != 0: #mientras o numero sea distindo a 0


    sumador += numero
    contador += 1
    numero = random.randint(0,100)

if contador != 0: #si o contador es distindo de cero, 
    
    promedio = sumador/contador #entonces calcular el promedio de esa manera

# si no, else

else:
    promedio = "ERROR"


print(f"Promedio: {promedio}")

