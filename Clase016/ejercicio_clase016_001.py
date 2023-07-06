
CAMINO = "Clase016/"


def llenar_desde_archivo(nombre_archivo:str) -> list:
    lista = []

    archivo = open(file=nombre_archivo,mode='r',encoding='utf-8')
    linea = archivo.readline().rstrip()    
    while linea != '':
        lista.append(int(linea))
        linea = archivo.readline()
    archivo.close()


    return lista



def mostrar_lista(lista:list) -> None:
    

    for indice,dato in enumerate(lista):
        print(f"Lista[{indice}] = {dato}")




def main():
    lista = llenar_desde_archivo(CAMINO + "numeros.txt")
    mostrar_lista(lista)
    
    
    


    # para encontrar archivo otra manera lista = llenar_desde_archivo("Clase016\\numeros.txt")



main()