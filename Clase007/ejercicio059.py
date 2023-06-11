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


-----------------------------------------

ejemplo: 

RECARGO_CHEQUE = 20
DESCUENTO_EFECTIVO = 10
RECARGO_TAR = 12

CHEQUE = 'C'
EFECTIVO = 'E'
TAR_CREDITO = 'T'

tot_efe = 0 #TOTAL DE EFETIVO
tot_tar = 0 #TOTAL DE TARJETA
tot_che = 0 #TOTAL DE CHEQUE
tot_gen = 0 #TOTAL GENERAL




codigo = input("Codigo <<< C,E,T,F (FIN)>>> : ").upper() # CODIGO C,E,T,F E FINALIZA
while codigo != 'F': #MIENTRAS EL CODIGO SEA DISTINTO DE F:

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





str_totales =f
********************************
Forma de Pago        Total  
********************************
Efectivo en Caja     $ {tot_efe}
Tarjeta/Crédito      $ {tot_tar}
Cheques              $ {tot_che}
Total de Venta       $ {tot_gen}
********************************
"""


RECARGO_CHEQUE = 20
DESCUENTO_EFECTIVO = 10
RECARGO_TARJETA = 12

CHEQUE = "C"
EFECTIVO = "E"
TARJETA_CREDITO = "T"




codigo = input("Codigo [C,E,T,F (FIN)] :  ").upper() # UPPER.() CONVERTE QUALQUER CANDENA EM MAYUSCULA


while codigo != "F": # mientras el codigo sea distinfo de F
    importe = float(input("Importe: "))
    if codigo == CHEQUE:    #SI EL CODIGO ES IGUAL A CHEQUE
        recargo = RECARGO_CHEQUE # o recargo es igual a Recargo_cheque
        descuento = 0
    elif codigo == EFECTIVO: # y si el codigo es igual a efectivo
        recargo = 0
        descuento = DESCUENTO_EFECTIVO
        total_efectivo += 


        
    else:
        recargo = TARJETA_CREDITO
        descuento = 0

    
    total = importe - (descuento*importe) + (recargo*importe) # TOTAL ES IMPORTE MENOS DESCUENTO MULTIPLICA POR IMPORTE ,
                                                                # MAIS O RECARGO MULTIPLICADO PELO IMPORTE 
                                                                # (SUMA E RESTA , RECARGOS Y DESCUENTOS)


    



    codigo = input("Codigo [C,E,T,F (FIN)] :  ").upper() 







str_totales =f"""
********************************
Forma de Pago        Total  
********************************
Efectivo en Caja     $ {total_efectivo}
Tarjeta/Crédito      $ {total_tarjeta}
Cheques              $ {total_cheques}
Total de Venta       $ {total_general}
********************************
"""
