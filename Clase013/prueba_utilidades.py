import sys
sys.path.append("recursos/") # Agregar al path la ruta donde se encuentran los modulos
from utilidades import *
from fechas_int import *


def leer_fecha(mensaje):
    """
    Permite leer una fecha desde el teclado
    """
    todo_ok = False
    while not todo_ok:
        print(mensaje)
        dia = leer_entero_rango("Dia: ", 1, 31)
        mes = leer_entero_rango("Mes: ", 1, 12)
        anio = leer_entero_rango("Anio: ", 1900, 2100)
        fecha = crear_fecha(dia, mes, anio)
        if isfecha_valida(fecha):
            todo_ok = True
        else:
            print(f"{fecha} No es una fecha valida.")     
    return fecha

def main():
    for x in sys.path:
        print(x)
    fecha = leer_fecha("Fecha de ingreso")
    print(f"Fecha ingresada: {str_fecha_larga(fecha)}")

main()