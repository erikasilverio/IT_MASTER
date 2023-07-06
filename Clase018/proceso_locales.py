




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
                calle = lista_cadenas[CALLE]
                superficie = float(lista_cadenas[SUPERFICIE])
PRECIOUSD = 2
PRECIOPESOS = 3
USDM2= 4
ANTIG= 5
EN_GALERIA =6
COTIZ= 7
TRIMESTRE=8
BARRIO= 9
COMUNA=10
          locales.append([calle,superficie,])      

    except IOError as e:
        print(f"Error al intentar leer el archivo: {nombre_archivo} \n {e}")

    return locales

def main():

    lista_locales = obtener_lista_desde_archivo(NOMBRE_ARCHIVO)



main()


