




TITULOS = "CALLE,SUPERFICIE,PRECIOUSD,PRECIOPESOS,USDM2,ANTIG,EN_GALERIA,COTIZ,TRIMESTRE,BARRIO,COMUNA"
#            0       1         2           3




CAMINO = 'Clase018/'
NOMBRE_ARCHIVO = CAMINO+'locales-en-venta-2020-transformado.csv'
CALLE = 0
SUPERFICIE = 1
PRECIOUSD = 2
PRECIOPESOS = 3
USDM2= 4
ANTIG= 5
EN_GALERIA =6
COTIZ= 7
TRIMESTRE=8
BARRIO= 9
COMUNA=10




def obtener_lista_desde_archivo(nombre_archivo:str)->list:
    locales = []

    try:
        with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
            titulos = archivo.readline().rstrip().split(',')
            # linea "BULNES 100,47,78000,4914000,1660,0,NO,63,PRIMER,ALMAGRO,5"
            # lista_cadenas = ["BULNES 100","47","78000","4914000","1660","0","NO","63","PRIMER","ALMAGRO","5"]
            #                       0
            for linea in archivo:
                lista_cadenas = linea.rstrip().split(',')
                calle = lista_cadenas[CALLE].upper()
                superficie = float(lista_cadenas[SUPERFICIE])
                preciousd = float(lista_cadenas[PRECIOUSD])
                preciopesos = float(lista_cadenas[PRECIOPESOS])
                usdm2 = float(lista_cadenas[USDM2])
                antiguedad = int(lista_cadenas[ANTIG])
                engaleria = lista_cadenas[EN_GALERIA].upper()
                cotizacion = float(lista_cadenas[COTIZ])
                trimestre = lista_cadenas[TRIMESTRE].upper()
                barrio = lista_cadenas[BARRIO].upper()
                comuna = int(lista_cadenas[COMUNA])
                
                locales.append([calle,superficie,preciousd,preciopesos,usdm2,antiguedad,engaleria,cotizacion,trimestre,barrio,comuna])      

    except IOError as e:
        print(f"Error al intentar leer el archivo: {nombre_archivo} \n {e}")

    return locales

def obtener_lista_barrios(locales:list)->list:
    barrios = []

    for local in locales:
        if local[BARRIO] not in barrios:
            barrios.append(local[BARRIO])

    return barrios
    

def crear_archivo(nombre_archivo:str,locales:list):
    try:
        with open(file=nombre_archivo,mode='w',encoding='utf-8') as archivo:
            linea = ''
            for local in locales:
                for index,campo in enumerate(local):
                    if index < len(local)-1:
                        linea += str(campo) + ','
                    else:
                        linea +=  str(campo)   
                
                linea += '\n'
                archivo.write(linea)
    except IOError as e:
        print(f"Error al intentar leer el archivo: {nombre_archivo} \n {e}")
        

def crear_archivos_por_barrio(lista_locales:list):
    barrios = obtener_lista_barrios(lista_locales)
    for barrio in barrios:
        locales_por_barrio = []
        for local in lista_locales:
            if barrio == local[BARRIO]:
                locales_por_barrio.append(local)
        nombre_archivo = f"{CAMINO}{barrio}.csv"
        locales_por_barrio.sort(key = lambda x: x[CALLE])
        crear_archivo(nombre_archivo,locales_por_barrio)

def main():

    lista_locales = obtener_lista_desde_archivo(NOMBRE_ARCHIVO)
    crear_archivos_por_barrio(lista_locales)
    

main()


