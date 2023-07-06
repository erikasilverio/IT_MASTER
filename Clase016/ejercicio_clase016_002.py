


CAMINO = "Clase016/"


def llenar_desde_archivo(nombre_archivo:str) -> list:
    lista_enteros = []

    archivo = open(file=nombre_archivo,mode='r',encoding='utf-8')     # abre archivo 
    for linea in archivo:
        lista_cadena = linea.rstrip().split(',')
        for cadena in lista_cadena:
            numero = int(cadena)
            lista_enteros.append(numero)

        
    archivo.close()   # cierra archivo 


    return lista_enteros



def mostrar_lista(lista:list) -> None: 
    for indice,dato in enumerate(lista):
        print(f"Lista[{indice}] = {dato}")




def main():
    lista = llenar_desde_archivo(CAMINO + "numeros2.txt")
    mostrar_lista(lista)
    print("range de len lista: ",list(range(len(lista))))
    print("enumerate lista: ",list(enumerate(lista)))
    
    
    
    


    # para encontrar archivo otra manera lista = llenar_desde_archivo("Clase016\\numeros.txt")



main()