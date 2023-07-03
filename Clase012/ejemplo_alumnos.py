
import fechas_int as fech
from ejer import *



"""
Alumno ==> legajo:int,fecha_nac:int,promedio:float

"""


def leer_fecha(cartel):
    todo_ok = False
    while not todo_ok:
        print(cartel)
        dia = leer_entero_rango("Dia: ", 1,31)
        mes = leer_entero_rango("Mes:",1,12)
        anio = leer_entero_rango("Ano: ",1800,2035)


        fecha = fech.crear_fecha(dia,mes,anio)
        if fech.isfecha_valida(fecha):
            todo_ok = True

        else:
            print("Error en la fecha!")

    return fecha


def leer_alumno():
    legajo = leer_entero("Legajo: ")
    fecha_nac = leer_fecha("Fecha de nascimiento")
    nota = leer_entero_rango("Nota: ", 1,10)
    return legajo,fecha_nac,nota

def main():
    a = leer_alumno()
    print(a)
    print(type(a).__name__)



main()