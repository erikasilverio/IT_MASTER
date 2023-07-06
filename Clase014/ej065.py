"""
Ejercicio 065
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales
de autoservicio que permita a los clientes armar su propio menú.

Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.
Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
3) Hamburguesa sola - 1300
4) Hamburguesa con queso - 1400
5) Gaseosa - 700
6) Postre - 600
7) Agregar aderezo - 100
8) Terminar

Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si
desea agregar más productos a su pedido antes de terminar.

El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo,
se debe sumar el importe total al subtotal.

Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y
calcular el valor total antes de sumarlo al subtotal.

Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".

"""
import sys
sys.path.append('recursos/') # Agregar al path la ruta donde se encuentran los modulos
from utilidades import *
from fechas_int import *




TUPLA_OPCIONES = ("COMIDAS CACHITO", 
    "1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550",
    "2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650",
    "3) Hamburguesa sola - $1300",
    "4) Hamburguesa con queso - $1400",
    "5) Gaseosa - $700",
    "6) Postre - $600",
    "7) Agregar aderezo - $100",
    "8) Terminar"
    )

TUPLA_PRECIOS = (0,1550.50,1650.25,1300.0,1400.8,700,600,100)
            #    0       1    2       3     4      5   6   7

def main():
    terminar_pedido = False
    while not terminar_pedido:
        op = menu(TUPLA_OPCIONES)
        if op == 8 :
            terminar_pedido = True
        
        elif op == 1:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 2:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 3:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 4:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 5:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 6:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 7:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")
        elif op == 8:
            cantidad = leer_entero("Cantidad: ")
            importe = TUPLA_PRECIOS[op] * cantidad
            print("Importe", importe)
            system("pause")

    return 


main()