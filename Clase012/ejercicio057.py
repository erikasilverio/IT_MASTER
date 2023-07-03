"""
Ejercicio 057
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar
que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
Cantidad de alumnos que aprobaron (nota >= 4).
Cantidad de alumnos que desaprobaron el examen (nota < 4).
Porcentaje de alumnos que están aplazados (nota == 1).

"""

def isint(str_numero):
    try:
        int(str_numero)

    except:
        return False
    return True

def isentero(str_numero):
    return isinstance(str_numero, int)






def es_numero_entero(cadena):
    index = 0
    while index < len(cadena):
        if(index != 0 or cadena[index] != '-') and (cadena[index] not in "0123456789") and len(cadena) <= 1:
            return False
    
        index += 1

    return True
    
    """
    pass
         for caracter in cadena:
        if caracter in "0123456789"
        
    """



def leer_entero(mensaje): 
    tudo_ok = False
    while not tudo_ok:
        cadena = input(mensaje)
        if isinstance(cadena, int):
            tudo_ok = True
        else:
            print(f"{cadena} No es un numero")

        return int(cadena)

def main():
    legajo = leer_entero("Legajo: ")
    while legajo != -1:
        nota = leer_entero("Nota: ")

        legajo = leer_entero("Legajo: ")

main()