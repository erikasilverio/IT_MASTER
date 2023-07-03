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

def isnumero(str_numero):
    return isint(str_numero) or isfloat(str_numero)
    




def isfloat(str_numero):
    try:
        float(str_numero)
    except:
        return False
    return True


def isint(str_numero):
    try:
        int(str_numero)
    except:
        return False
    return True



def es_numero_entero(cadena):   # TAREA A RESOLVER!!!!

    if len(cadena) == 0:
        return False
    
    index = 0
    while index < len(cadena):

#        if (index == 0 and cadena [index] == '-') or (cadena[index] in "123456789"):
        if (index != 0 or cadena [index] != '-') and (cadena[index] not in "123456789"):
            return False
        index += 1

    return True



def leer_entero_rango(cartel,desde,hasta):

    todo_ok = False
    while not todo_ok:
        cadena = input(cartel)
        if isint(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:
                todo_ok = True
            else: 
                print(f"{numero} no esta en el rango {desde} .. {hasta}")
        else:
            print(f"{cadena} No es un numero")

    return int(cadena)


def leer_entero(mensaje):

    todo_ok = False
    while not todo_ok:
        cadena = input(mensaje)
        if isint(cadena):
            todo_ok = True
        else:
            print(f"{cadena} No es un numero")

    return int(cadena)


def main():
    legajo = leer_entero("Legajo: ")
    while legajo != -1:

        nota = leer_entero_rango("Nota: ", 1,10)

        # TENGO LOS DATOS DE UN ALUNO !!!
        if nota == 1:
            pass
        if nota < 4:
            pass
        else:
            pass

        legajo = leer_entero("Legajo: ")



if __name__ ==  '__main__':


    main()