"""
Ejercicio 065
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.
Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:
1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
3) Hamburguesa sola - 1300
4) Hamburguesa con queso - 1400
5) Gaseosa - 700
6) Postre - 600
7) Agregar aderezo - 100
8) Terminar
Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.
El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".
"""
import sys
sys.path.append("recursos/") # Agregar al path la ruta donde se encuentran los modulos
from utilidades import *
from fechas_int import *

TITULO = "COMIDAS CACHITO" +"   "+str_fecha(obtener_fecha_actual())

TUPLA_OPCIONES = (TITULO,
    "1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550",
    "2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650",
    "3) Hamburguesa sola - $1300",
    "4) Hamburguesa con queso - $1400",
    "5) Gaseosa - $700",
    "6) Postre - $600",
    "7) Agregar aderezo - $100",
    "8) Terminar"
)

TUPLA_PRECIOS = (0,1550.5,1650.25,1300.0,1400.8,700,600,100)
              #  0,  1       2       3      4    5   6   7

def proc_un_pedido(op):    
    cantidad = leer_entero(f"{TUPLA_OPCIONES[op]} Cantidad: ")      
    importe = TUPLA_PRECIOS[op] * cantidad         
    print(f"Importe {importe}")                
   
    system("pause")
    return (   TUPLA_OPCIONES[op],cantidad,importe  )


def continua(texto_pregunta):
    resp = input(f'Continua {texto_pregunta} [S/N]: ').upper()
    if resp == 'S':
        return True
    return False

def main():
    terminar_proceso = False
    nro_pedido = 0
    while not terminar_proceso:
        tupla_pedidos = ()
        terminar_pedido = False
        total_pedido = 0
        while not terminar_pedido:
            op = menu(TUPLA_OPCIONES)
            if op != 8:                                 
                tupla_pedidos += (     proc_un_pedido(op),    )
            else :
                if len(tupla_pedidos) > 0:
                    nro_pedido += 1
                    system("cls")
                    print(titulo("COMIDAS CACHITO",70))
                    print(f"Pedido: {nro_pedido} - {str_fecha(obtener_fecha_actual())}")
                    print("-"*70)
                    print(f"{'Producto':30s} {'Cantidad':8s} {'Precio':10s} {'Total':10s}")
                    print("-"*70)
                    total_pedido  = 0
                    for tupla in tupla_pedidos:
                        total = tupla[1] * tupla[2]
                        total_pedido += total
                        print(f"{tupla[0][:30]:30s} {tupla[1]:8d} {tupla[2]:10.2f} {total:10.2f}")
                    print("-"*70)    
                    print(f"Total Pedido: {total_pedido:47.2f}")
                    print("-"*70)
                    system("pause")
                terminar_pedido = True
        # fin while
        terminar_proceso = continua("Ingresando Datos")


main()