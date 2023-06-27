

texto = """
Ejercicio 066b

La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.

"""
"""
"La casa grande"
#01234567891111
#          0123
#
"""


contador = 0
i = 0
while i < len(texto): # serve para descartar caracteres que nao sao letras
    while i < len(texto) and texto[i] == ' ':
        i += 1 #paso al siguinte caracter

    # TRABAJO CON LAS LETRAS DE UNA PALABRA
    
    palabra = ""
    while i < len(texto) and texto[i] != ' ':
        palabra += texto[i]
        i += 1 #paso al siguinte caracter
    
    if len(palabra) > 0:
        print(palabra)
        contador += 1

print(f"La cantidad de palabras es: {contador}")