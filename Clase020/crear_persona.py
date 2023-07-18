
import random

# dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail



CAMINO = "Clase020/"
ARCHIVO_LOCALIDADES = "Localidades.csv"
ARCHIVO_NOMBRE_FEMININOS = "nombresFemeninos.txt"
ARCHIVO_NOMBRE_MASCULINOS = "nombresMasculinos.txt"
ARCHIVO_APELLIDOS = "Apellidos.txt"




def obtener_lista(nombre_archivo:str)->list:
    try:

        with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
            return [ linea.rstrip() for linea in archivo]
        

    except IOError as e:  
        raise RuntimeError(f"Error: {nombre_archivo}\n Pyton == > {e}")






def crear_lista_personas(cantidad_persona:int)->list:
    femininos = obtener_lista(ARCHIVO_NOMBRE_FEMININOS)
    masculinos = obtener_lista(ARCHIVO_NOMBRE_MASCULINOS)
    apellidos = obtener_lista(ARCHIVO_APELLIDOS)




def main():

    lista_personas = crear_lista_personas(10)
    


main()
