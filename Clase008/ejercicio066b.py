"""
Ejercicio 066b

La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.

"""

CANTIDAD_LIBROS_POR_ESTANTE = 2
total_h = 0
total_i = 0
total_n = 0

estante = input("Estante:").upper()

while estante != "F":
        print(f"Proceso el estante {estante}")



        mayor_cantidad_pagina = 0
        nombre_libro_mayor = ""
        
        for numero_libro in range(CANTIDAD_LIBROS_POR_ESTANTE):
                nombre = input("Nombre del Livro: ")
                


                genero = input("Genero:\nN: Novela\nI: Infantil\nH: Historia : ").upper()
                while genero not in ('N','I','H'): #TIPO DE LETRAS ACEITAS
                    print("ERROR EN EL GENERO")
                    genero = input("Genero: ['N','I','H']: ").upper()


    
                cantidad_paginas = int(input("Cantidad de pagina:"))

                if genero == 'I':
                    total_i += 1
                elif genero == 'H':
                    total_h += 1
                else:
                      total_n += 1

        # FIN CICLO FOR (FIN ESTANTE)
                
                if cantidad_paginas > mayor_cantidad_pagina:
                        mayor_cantidad_pagina = cantidad_paginas
                        nombre_libro_mayor = nombre


        print(f"Estante: {estante} Livro con mas pagina: {nombre_libro_mayor} con {mayor_cantidad_pagina}")
        
        estante = input("Estante:").upper()

# FIN DEL CICLO WHILE
print(f"Total H: {total_h}")
print(f"Total I: {total_i}")
print(f"Total N: {total_n}")