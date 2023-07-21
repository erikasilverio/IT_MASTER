


# dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail



CAMINO = "Clase020/"
ARCHIVO_LOCALIDADES = "Localidades.csv"
ARCHIVO_NOMBRE_FEMENINOS = "nombresFemeninos.txt"
ARCHIVO_NOMBRE_MASCULINOS = "nombresMasculinos.txt"
ARCHIVO_APELLIDOS = "Apellidos.txt"


import random



def obtener_lista(nombre_archivo:str)->list:
    try:
        with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
            return [ linea.rstrip() for linea in archivo]
    except IOError as e:  
        raise RuntimeError(f"Error: {nombre_archivo}\nPyton == > {e}")





def obtener_dicc(nombre_archivo:str)->dict:
    dic = {}
    try:
        with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
            for linea in archivo:
                pais,provincia,localidad = linea.rstrip().split(',')
                if provincia in dic.keys():
                    dic[provincia].append(localidad)
                else:
                    dic[provincia] = [localidad]

            return dic

    except IOError as e:  
        raise RuntimeError(f"Error: {nombre_archivo}\nPyton == > {e}")


def crear_lista_personas(cantidad_personas:int)->list:
    femeninos = obtener_lista(ARCHIVO_NOMBRE_FEMENINOS)
    masculinos = obtener_lista(ARCHIVO_NOMBRE_MASCULINOS)
    apellidos = obtener_lista(ARCHIVO_APELLIDOS)
    dic_provincias = obtener_dicc(ARCHIVO_LOCALIDADES)

    lista_personas = []
    titulos = "dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail".split(',')

    # dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail


    for x in range(cantidad_personas):
        lista = []
        dni = str(random.randint(15000000,49000000))
        sexo = random.choice("MF")
        edad = str.randint(18,75)
        provincia = random.choice(list(dic_provincias.keys()))
        localidad = random.choice(dic_provincias[provincia])
        if sexo == 'M':
            nombre = ' '.join(random.choices(masculinos,k=random.randint(1,3)))

        else:
            nombre = ' '.join(random.choices(femeninos,k=random.randint(1,3)))

        apellido =  ' '.join(random.choices(apellidos,k=random.randint(1,2)))

        calle = random.choice (dic_provincias[random.choice(list(dic_provincias.keys())) ] )
        
        altura = str(random.randint(50,9999))

        ubicacion = random.choice(["Casa", f"Dto {random.randint(1,20)}", f"Dto{random.choice('ABCDEF')}"])

        mail = f"{nombre.split()[0]}@.{random.choice(['com','com.ar'])}"

        

        lista_personas.append(dict(zip(titulos,titulos, [ dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail]  )))

    return lista_personas




def main():

    lista_personas = crear_lista_personas(10)
    for persona in lista_personas:
        print (list(persona.values()))
    


main()
