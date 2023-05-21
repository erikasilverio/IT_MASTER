"""

Escribir un programa que permita al usuario ingresar un período de tiempo en segundos.
Luego, el programa debe convertir ese período de tiempo a una forma más legible y
comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos.
El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos
ingresados y su equivalente en días, horas, minutos y segundos.

Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.

Usar en el programa las siguientes instrucciones:
dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes

"""


segundos = int(input( "Tiempo en segundos: "))

dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes



print(f"{segundos}200000 segundos equivalen a {dias}  días, {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

print(f"{dias:02}:{horas:02}:{minutos:02}:{segundos_restantes:02}")