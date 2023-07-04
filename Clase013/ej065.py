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
from os import system
import sys
sys.path.append("Clase013") # Agregar al path la ruta donde se encuentran los modulos
from utilidades_1_ import *
from fechas_1_int import *


def titulo(texto):
                     # "".title().center(30)
    return f"{'-'*30}\n{texto.title().center(30)}\n{'-'*30}"


def menu(tupla_opciones):
    system("cls")
    for index,opcion in enumerate(tupla_opciones):
        if index == 0:
            print(titulo(opcion))
        else:
            print(opcion.title())

    return leer_entero_rango("INGRESE UNA OPCION:",1,8)
    


TUPLA_OPCIONES = ("COMIDAS CACHITO", 
    "1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550",
    "2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650",
    "3) Hamburguesa sola - 1300",
    "4) Hamburguesa con queso - 1400",
    "5) Gaseosa - 700",
    "6) Postre - 600",
    "7) Agregar aderezo - 100",
    "8) Terminar"
    )


def main():
    terminar = False
    while not terminar:
        op = menu(TUPLA_OPCIONES)
        if op == 8 :
            terminar = True
        
        elif op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass


main()