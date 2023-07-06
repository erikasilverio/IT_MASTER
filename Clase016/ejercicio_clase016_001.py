



def llenar_desde_archivo(nombre_archivo):
    lista = []

    archivo = open(file=nombre_archivo,mode='r',encoding='utf-8')

    linea = archivo.readline()
    while linea != '':
        print(linea)

        linea = archivo.readline()

    archivo.close()



    return lista



CAMINO = "Clase016/"

def main():
    lista = llenar_desde_archivo(CAMINO + "numeros.txt")  
    


    # para encontrar archivo otra manera lista = llenar_desde_archivo("Clase016\\numeros.txt")



main()