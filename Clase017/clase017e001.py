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

    try:
        with open(file=nombre_archivo,mode="r") as archivo:
            for linea in archivo:
                lista_cadena = linea.rstrip().split(',')
                lista_numeros = []
                for cadena in lista_cadena:
                    lista_numeros.append(int(cadena))

                lista.append(lista_numeros)


    except IOError as ex:
        print(f"Error al crear el archivo: ")

    return lista




def agregarMedia(nombre_archivo:str) -> None:


    lista = obterne_desde_archivo(nombre_archivo)

    

    try:
        with open(file=nombre_archivo,mode="w") as archivo:
            for lista_numeros in lista:
                promedio = sum(lista_numeros)/len(lista_numeros)   # SUMA DIVIDADA PELA QUANTIDADE DE ELEMENTOS.
                linea_texto = " "
                for numero in lista_numeros:
                    linea_texto += str(numero) + ","
                

                archivo.write(linea_texto[:-1] + '\n')
                archivo.write(str  (  round  (  promedio,2 )  )  +"\n")

            
    except IOError as ex:
        print(f"Error al crear el archivo: ")


    



def generar_archivo(nombre_archivo:str,lineas_desde:int,linea_hasta:int,
                        cantnum_desde:int,cantnum_hasta:int,
                            numero_desde:int,numero_hasta:int) -> None:

    try:
        with open(file=nombre_archivo,mode="w") as archivo:
            cantidad_lineas = random.randint(lineas_desde,linea_hasta)
            for linea in range(cantidad_lineas):
                cantidad_numero  = random.randint(cantnum_desde,cantnum_hasta)
                for numero in range(cantidad_numero):
                    dato = random.randint(numero_desde,numero_hasta)
                    archivo.write(str(dato))
                    if numero < cantidad_numero-1:
                        archivo.write(",")
                archivo.write("\n")


    except IOError as ex:    # EX significa exepcion
        print(f"Error al crear el archivo:")



def main():
    generar_archivo("Clase017/numeros.csv",1,10,1,10,1,10)
    agregarMedia("Clase017/numeros.csv")
    # lista = "La casa grande".split()  --->  ['La', 'casa', 'grande']
    # lista = "1,7,8,9,4\n".split() # ['1,7,8,9,4']

    """lista = [1,2,3]
    promedio = sum(lista)/len(lista)
    print(lista,promedio)
    cadena = ','.join(lista)  # 1,7,8,9,4
    print(cadena)"""



main()
