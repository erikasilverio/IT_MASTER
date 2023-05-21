"""
Ejercicio 030
Escribir un programa que permita al usuario generar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)


ejemplo:
# constantes simbólicas
COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

num_paginas = int(input("Ingrese el número de páginas del libro: "))
costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)

# Escriba lo que falta de la solución aquí

print("El costo del libro es: $", costo)


----------------------

    a = randint(1,100)
    b = randint(1,100)
    

    if a > b:
        resultado = f"{a} es div. por {b} ==> {(a%b) == 0}"
    else: 
        resultado = f"{b} es div. por {a} ==> {(b%a) == 0}"

    print(resultado)

    ---------------------------


"""

from random import randint # ingressar os dados do sistema

terminar = bool(False)
while not terminar: # mientras nao terminar

    a = randint(1,100)
    b = randint(1,100)


    if a > b:
        es_divisible = (a%b) == 0 # si es divisible
        resultado = f"{a} es div. por {b} ==> {es_divisible}"
    else: 
        es_divisible = (b%a) == 0
        resultado = f"{b} es div. por {a} ==> {es_divisible}"
    
    if es_divisible == True: # se rompe el ciclo y se termina
        terminar = True

    print(resultado)