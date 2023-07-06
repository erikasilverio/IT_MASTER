



CAMINO = "Clase016\\"

def limpiar(cadena:str) -> str:
   nueva = ''

   for letra in cadena:  # para cada letra na cadena
      if letra.isalpha():
         nueva += letra



   return nueva


def buscar_posicion(palabra:str,lista_totales:str) -> int:

   for indice,tupla_elemento in enumerate(lista_totales):
      if palabra == tupla_elemento[0]:
         return indice
      
   return None



def obtener_lista_totales(lista_palabras:list) -> list:
   lista_totales = [] # ["palabra", cantidad], ["mono",3], []]
#                             0     1
#                             0
   for palabra in lista_palabras:
      posicion = buscar_posicion(palabra,lista_totales)
      if posicion == None:
         lista_totales.append( [palabra,1] )

      else:
         lista_totales[posicion][1] += 1
          
      
   return lista_totales


def obtener_las_palabras(nombre_archivo:str) -> list:
   lista_palabras = []



   with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
      for linea in archivo:
         lista_cadenas = linea.rstrip().split()
         for cadena in lista_cadenas:
            palabra = limpiar(cadena).lower()
            
            lista_palabras.append(palabra)
      


   return lista_palabras




def main():

   lista_palabras = obtener_las_palabras(CAMINO + "El_Muerto.txt")
   print(f"Cantidad de palabras: {len(lista_palabras)} ")

   lista_sin_repetir = list(set(lista_palabras))
   print(f"Cantidad de palabras sin repetir: {len(lista_sin_repetir)} ")
   # print(lista_sin_repetir)
   lista_totales = obtener_lista_totales(lista_palabras)
   for palabra,contador in lista_totales:
      print(f"{palabra} ==> {contador}")



main()


