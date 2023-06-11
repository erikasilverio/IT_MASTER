enunciado = """
Ejercicio 033
La farmacia Sindical efectúa descuentos a sus afiliados según 
el importe de la compra con la siguiente escala:

Menor de 5500.0 el descuento es del 4.5%
Entre 5500.0 y 10000.0 el descuento es del 8%
Más de 10000.0 el descuento es del 10.5%

Escribir un programa que reciba un importe e informe: 
el descuento y el precio neto a cobrar, con mensajes aclaratorios.
"""

print(enunciado)

importe = float(input("Ingresse o importe: "))
if importe < 5500.0: #SI O IMPORTE ES Menor de 5500.0
    descuento = importe * 4.5/100 #el descuento es del 4.5%
elif importe <= 1000.0: 
    descuento = importe * 8.0/100
else: #ENTONCES
    descuento = importe * 10.5/100


# ACA CON O F STRING , HACEMOS UNA CADENA FORMATEADA!!!
# o que significa 10.2f => 10 é a quantidade de espaço, seria o largo do numero e 2f => seriam os decimais
# IMPORTE MENOS O DESCUENTO, EN LO FORMATO 10.2F - SON 10 NUMERO Y DOS DECIMALES
pantalla = f"""                                     
Importe:   {importe:10.2f}                          
descuento: {descuento:10.2f}
-----------------------------
Imp.Total: {importe-descuento:10.2f} 

"""

print(pantalla)