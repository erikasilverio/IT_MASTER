



CAMINO = 'Clase019/'
NOMBRE_ARCHIVO = CAMINO+'locales-en-venta-2020-transformado.csv'





def obtener_lista_desde_archivo(nombre_archivo:str)->list:
    
    try:
        with open(file=nombre_archivo,mode='r', encoding='utf-8') as archivo:

            titulos = archivo.readline().rstrip().split(',')
            return [ dict(zip(titulos,linea.rstrip().split(','))) for linea in archivo ]
   
   
      
    except IOError as e:
        raise Exception(f'ERROR AL INTENTAR LER EL ARCHIVO: {nombre_archivo} \nPyton dice: {e}' )
    
    
def filtrar_por_barrio(lista:list[dict],nombre_barrio:str)->list[dict]:
   # return [if local ['BARRIO'] == nombre_barrio for local in lista]  ## resolver

   salida =  []
   for local in lista:
       if local ['BARRIO'] == nombre_barrio:
           salida.append(local)

   return salida
    




    
def main():
    try:
        lista_locales = obtener_lista_desde_archivo(NOMBRE_ARCHIVO)
    except Exception as e:
        print(e)
    else:
        for local in filtrar_por_barrio(lista_locales, " VILLA DEL PARQUE "):
            print(local)



main()

