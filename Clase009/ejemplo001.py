"""

MOSTRA LA SUMA DE CADA SUBSEQUENCIA (SUB)

1 4 5 7 8 4 0 4 7 8 5 6 9 0 0 0 0 1 0 1 4 5 7 8 0 -1

"""


mayor_suma_sub = -float('inf')
suma_total = 0
numero = int(input("Numero: "))

while numero != -1:  #mistras que o numero seja distindo a -1.  (antes)
    suma_sub = 0  


    while numero != 0:  #mienstras que o numero sea distinto de 0.
        suma_sub += numero
        suma_total += numero
        numero = int(input("Numero: "))  # (durante)

    # FIN DEL WHILE

    print(f"Suma Sub: {suma_sub}")
    if suma_sub > mayor_suma_sub :
        mayor_suma_sub = suma_sub

    # OTRAS FOMRA ==> suma_total += suma_sub
    numero = int(input("Numero: "))  # despues que mostre um numwro , volte a me mostrar outro(despues)

# FIN DEL WHILE

print(f"Suma total: {suma_total}")
print(f"La suma sub mayor es: {mayor_suma_sub}")