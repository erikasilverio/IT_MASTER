"""
Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

"""

def validar_entero(cadena):
    es = False


    for caracter in cadena:
        
        if not caracter.isdigit() and caracter != '-':
            return False
        

    return True


def leer_entero(cartel):

    todo_ok = False
    while todo_ok == False:
        cadena = input(cartel)
    
        if validar_entero(cadena) == True:
            todo_ok = True
    
        else:
            print(f"{cadena} No es un numero!")

    return int(cadena)


def main():

    suma = 0
    cont = 0
    numero = leer_entero("Ingrese un numero: ") # int(input("Numero:"))

    while numero != 0:
        cont += 1
        suma += numero
        numero = leer_entero("Ingrese un numero: ")  # int(input("Numero:"))

    prom = suma/cont
    print(f"Promedio : {prom} ")


main()