import random

def obtener_desde_archivo(nombre_archivo:str) ->list:
    lista = []
    try:
        with open(file=nombre_archivo,mode='r') as archivo:
            for linea in archivo:
                lista_cadenas = linea.rstrip().split(',')
                lista_numeros = []
                for cadena in lista_cadenas:
                    lista_numeros.append(int(cadena))
                lista.append(lista_numeros)    
    except IOError as ex:
        print(f"Error al crear el archivo: ")
    return lista




def agregarMedia(nombre_archivo:str)->None:

    lista = obtener_desde_archivo(nombre_archivo)

    

    try:
        with open(file=nombre_archivo,mode='w') as archivo:
            for lista_numeros in lista:
                prom = sum(lista_numeros)/len(lista_numeros)
                linea_texto = ""
                for numero in lista_numeros:
                    linea_texto += str(numero) + ","
                
                archivo.write(linea_texto[:-1] + '\n')
                archivo.write(str(round(prom,2))+"\n")
        
    except IOError as ex:
        print(f"Error al crear el archivo: ")


def generar_archivo(nombre_archivo:str,lineas_desde:int,lineas_hasta:int,
                        cantnum_desde:int,cantnum_hasta:int,
                            numero_desde:int,numero_hasta:int)->None:
    try:
        with open(file=nombre_archivo,mode='w') as archivo:
            cantidad_lineas = random.randint(lineas_desde,lineas_hasta)
            for linea in range(cantidad_lineas):
                cantidad_numeros = random.randint(cantnum_desde,cantnum_hasta)
                for numero in range(cantidad_numeros):
                    dato = random.randint(numero_desde,numero_hasta)
                    archivo.write(str(dato))
                    if numero < cantidad_numeros-1:
                        archivo.write(",")
                archivo.write("\n")
    except IOError as ex:
        print(f"Error al crear el archivo: ")

def main():
    generar_archivo("clase017/numeros.csv",1,10,1,10,1,10)
    agregarMedia("clase017/numeros.csv")
    """lista = [1,2,3]
    prom = sum(lista)/len(lista)
    print(lista,prom)
    cadena = '-'.join(lista)
    print(cadena)"""
main()