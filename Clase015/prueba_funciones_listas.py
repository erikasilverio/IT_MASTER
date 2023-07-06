
import random

def esprimo(numero):
    for div in range(2,numero):
        if numero % div == 0:
            return False
    return True



def generar_lista_enteros_random(cantidad,desde,hasta):
    lista = []
    for x in range(cantidad):
        numero = random.randint(desde,hasta)
        lista.append(numero)
    return lista

def generar_lista_enteros_random_sin_repetir(cantidad,desde,hasta):
    lista = []
    for x in range(cantidad):
        numero = random.randint(desde,hasta)
        if numero not in lista:
            lista.append(numero)
    return lista

def generar_lista_enteros_random_sin_repetir_otro(cantidad,desde,hasta):
    lista = []
    for x in range(cantidad):
        numero = random.randint(desde,hasta)
        lista.append(numero)
    
    return list( set( lista ) )




def main():
    lista_numeros = generar_lista_enteros_random_sin_repetir_otro(1500,1,10)
    print(lista_numeros)





main()





