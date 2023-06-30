"""

5 5 5 5 2 2 2 2 2 2 2 2 2 2 2 2 2  8 8 8 8 8 3 3 3 3 3 3 3 7 4 4 4 0

1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 7 7 7 7 7 9 9 9 9 9 9 9 9 0

"""

cantidad_numeros = 0
numero = int(input("Numero: "))
while numero != 0: # FINDE DATOS
        numero_proceso = numero
        repeticiones = 0

        while numero != 0 and numero_proceso == numero: # FIN DE DATOS Y EL MISMO NUMERO
            repeticiones += 1
            # cantidad_numeros += 1
            numero = int(input("Numero: "))

        # FIN DEL NUMERO, FIN DEL CICLO

        print(f"Numero: {numero_proceso} Repeticiones: {repeticiones}")
        cantidad_numeros += repeticiones

# FIN DE DATOS
print(f"Cantidade de Numeros: {cantidad_numeros}")