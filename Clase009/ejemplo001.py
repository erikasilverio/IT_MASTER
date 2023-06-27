"""

MOSTRA LA SUMA DE CADA SUBSEQUENCIA (SUB)

1 4 5 7 8 4 0 4 7 8 5 6 9 0 1 0 1 4 5 7 8 0 -1

"""

numero = int(input("Numero: "))

while numero != -1:
    suma_sub = 0


    while numero != 0:
       
        suma_sub += numero
        numero = int(input("Numero: "))


    # FIN DEL WHILE

    print(f"Suma: {suma_sub}")
    numero = int(input("Numero: "))

# FIN DEL WHILE

