"""
Ejercicio 059

Escribir un programa para un negocio de venta de granos
que desea controlar las ventas realizadas. 
De cada venta ingresa el importe total y un código 
que indica la forma de pago. 

Los códigos puede ser:

C: cheque, 20% de recargo.
E: efectivo, 10% de descuento. 
T: con tarjeta, 12% de recargo.

Se debe ingresar una F para finalizar el día de venta y arrojar los 
siguientes totales.

********************************
Forma de Pago        Total  
********************************
Efectivo en Caja     $ xxxx.xx
Tarjeta/Crédito      $ xxxx.xx
Cheques              $ xxxx.xx
Total de Venta       $ xxxx.xx
********************************
"""

RECARGO_CHEQUE = 20
DESCUENTO_EFECTIVO = 10
RECARGO_TAR = 12

CHEQUE = 'C'
EFECTIVO = 'E'
TAR_CREDITO = 'T'

tot_efe = 0
tot_tar = 0
tot_che = 0
tot_gen = 0


codigo = input("Codigo <<< C,E,T,F (FIN)>>> : ").upper()
while codigo != 'F':
    importe = float(input("Importe: "))
    if codigo == CHEQUE:
        recargo = RECARGO_CHEQUE
        descuento = 0
    elif codigo == EFECTIVO:
        recargo = 0
        descuento = DESCUENTO_EFECTIVO
        tot_efe += 
        
    else:
        recargo = RECARGO_TAR
        descuento = 0

    total = importe - (descuento*importe) + (recargo*importe)


    codigo = input("Codigo <<< C,E,T,F (FIN)>>> : ").upper()





str_totales =f"""
********************************
Forma de Pago        Total  
********************************
Efectivo en Caja     $ {tot_efe}
Tarjeta/Crédito      $ {tot_tar}
Cheques              $ {tot_che}
Total de Venta       $ {tot_gen}
********************************
"""