"""

Leer numeros hasta que se ingrese un cero.
Mostrar la suma

lista1 ==> 1,5,4,7,8,9,5,4,1,7,8,5,1,0
lista2 ==> 1,5,4,8,5,1,0
lista3 ==> 0



#ANTES DEL PROCESSO

numero = int(input("Numero: "))

while numero != 0:


#DURANTE EL PROCESO
    numero = int(input("Numero: "))

#DESPUES


# EL PROCESO TERMINA CUANDO INGRESO UN CERO, ES UN CICLO DE CONTROL


"""

import random

# ANTES DEL PROCESSO (PARA TODOS)

sumador = 0
contador = 0

numero = random.randint(0,1000)

while numero != 0:
# DURANTE EL PROCESO (PARA CADA DTOS)


    sumador += numero # sumador = sumador + numero
    contador += 1 # Contador es contador + 1


    numero = random.randint(0,1000)

#DESPUES (TOTALES)

print(f"La cantidad de numero es: {contador}\n\n\nLa suma es: {sumador}") # \n salta linea
