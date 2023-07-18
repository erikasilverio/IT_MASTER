


# dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail



CAMINO = "Clase020/"
ARCHIVO_LOCALIDADES = "Localidades.csv"
ARCHIVO_NOMBRE_FEMININOS = "nombresFemeninos.txt"
ARCHIVO_NOMBRE_MASCULINOS = "nombresMasculinos.txt"
ARCHIVO_APELLIDOS = "Apellidos.txt"




def obter_lista(nombre_archivo:str)->list:
    try:

    except IOError:
        






def crear_lista_persona(cantidad_persona:int)->list:
    femininos = obtener_lista(ARCHIVO_NOMBRE_FEMININOS)
    masculinos = obtener_lista(ARCHIVO_NOMBRE_MASCULINOS)
    apellidos = obter_lista(ARCHIVO_APELLIDOS)




def main():
    lista_personas = crear_lista_personas(10)
    


main()
