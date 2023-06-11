"""
Ejercicio 028
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

"""

import random

#numero_de_mes = int(input("Numero de mes:"))
numero_de_mes = random.randint(1,12) #para numeros aleatorios.

if numero_de_mes == 1:
    nombre = "janeiro"
elif numero_de_mes == 2:
        nombre = "fevereiro"
elif numero_de_mes == 3:
        nombre = "março"
elif numero_de_mes == 4:
        nombre = "abril"
elif numero_de_mes == 5:
        nombre = "mayo"
elif numero_de_mes == 6:
        nombre = "junio"
elif numero_de_mes == 7:
        nombre = "julio"
elif numero_de_mes == 8:
        nombre = "agosto"
elif numero_de_mes == 9:
        nombre = "setembro"
elif numero_de_mes == 10:
        nombre = "outubro"
elif numero_de_mes == 11:
        nombre = "novembro"
elif numero_de_mes == 12:
        nombre = "dezembro"
else:
        nombre = "ERROR"

print(f"Numero do mes: {numero_de_mes}\nNombre do Mes: {nombre} ")