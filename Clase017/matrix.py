


def mostrar(lista:list)-> None:
    filas = len(lista)
    columnas = len(lista[0])
    print(f'm:({filas}x{columnas})')


    for f in range(filas):   # F = Filas          
        for c in range(columnas): # C = Columnas
            print(f'{lista[f][c]:6}', end='')

        print()


def crear_matriz(filas:int=3,columnas:int=3,desde:int=0,hasta:int=9)->list[list[int]]:
    if desde > hasta:
        desde, hasta = hasta,desde
    if filas < 0:
        filas = 0
    if columnas < 0:
        columnas = 0

    import random


    lista_filas = []

    for f in range(filas):
        lista_columnas = []
        for c in range(columnas):
            lista_columnas.append(random.randint(desde,hasta))
        lista_filas.append(lista_columnas)
    return lista_filas


def buscar(matriz:list[list[int]], numero:int)->tuple [int|None,int|None]:
    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if numero == matriz[f][c]:
                return(f,c)
            
    return "(None,None)"
                 


def main():
    mat = crear_matriz(5,7,1,10)       # (filas=4, desde=99)  # [ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ]
    mostrar(mat)
    fila,columna = buscar(mat,8)
    if fila is not None:
        print("Lo Encontre",fila,columna)
    






main()