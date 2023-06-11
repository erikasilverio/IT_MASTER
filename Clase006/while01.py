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


# ANTES DEL PROCESSO (PARA TODOS)

sumador = 0
numero = int(input("Numero: "))

while numero != 0:
        # DURANTE EL PROCESO (PARA CADA DTOS)

    sumador += numero # sumador = sumador + numero
    numero = int(input("Numero: "))

#DESPUES (TOTALES)
print(f"La suma es: {sumador}")