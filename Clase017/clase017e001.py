"""
Se tiene un archivo CSV con valores enteros 
(cada línea del archivo puede tener uno o más valores separado por una coma en la misma línea) 
Desarrolle una función agregarMedia que reciba como parámetro el nombre del archivo y agregue 
debajo de cada línea del archivo el promedio de los valores que contiene dicha línea. 
Ayuda: Para Desarrollar el proceso, cargar inicialmente todo el archivo como una lista y 
luego reescribir el archivo con lo solicitado.
"""

import random


def obterne_desde_archivo(nombre_archivo:str) -> list:
    lista = []




    return lista


def agregarMedia(nombre_archivo:str) -> None:


    lista = obterne_desde_archivo(nombre_archivo)
    try:
        with open(file=nombre_archivo,mode="w") as archivo:
            for lista_numeros in lista:
                promedio = sum(lista_numeros)/len(lista_numeros)   # SUMA DIVIDADA PELA QUANTIDADE DE ELEMENTOS.
                linea_texto = f"{','.join}\n"


            
    except IOError as ex:
        print(f"Error al crear el archivo: ")


    



def generar_archivo(nombre_archivo:str,lineas_desde:int,linea_hasya:int,
                        cantnum_desde:int,cantnum_hasta:int,
                            numero_desde:int,numero_hasta:int) -> None:

    try:
        with open(file=nombre_archivo,mode="w") as archivo:
            cantidad_lineas = random.randint(lineas_desde,linea_hasya)
            for linea in range(cantidad_lineas):
                cantidad_numero  = random.randint(cantnum_desde,cantnum_hasta)
                for numero in range(cantidad_numero):
                    dato = random.randint(numero_desde,numero_hasta)
                    archivo.write(str(dato))
                    if numero < cantidad_numero-1:
                        archivo.write(",")
                archivo.write("\n")


    except IOError as ex:
        print(f"Error al crear el archivo:")



def main():
    # generar_archivo("Clase017/numeros.csv",1,100,1,100,1,100)
    # agregarMedia("Clase017/numeros.csv")
    # lista = "La casa grande".split()  --->  ['La', 'casa', 'grande']
    lista = "1,7,8,9,4\n".split() # ['1,7,8,9,4']
    print(lista)
    cadena = ','.join(lista)  # 1,7,8,9,4
    print(cadena)



main()
