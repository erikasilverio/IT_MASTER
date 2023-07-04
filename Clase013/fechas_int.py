"""
Este módulo contiene funciones relacionadas con la manipulación y validación de fechas en formato AAAAMMDD


- isfecha_valida(aaaammdd): Verifica si una fecha es válida. Retorna True si la fecha es válida y False en caso contrario.

- isbisiesto(a): Verifica si un año es bisiesto. Retorna True si el año es bisiesto y False en caso contrario.

- obtener_cantidad_dias_del_mes(m, anio): Retorna la cantidad de días que tiene un mes en un año determinado.

- crear_fecha(d, m, a): Crea una fecha en formato AAAAMMDD a partir de un día, mes y año.

- obtener_fecha_actual(): Retorna la fecha actual del sistema en formato AAAAMMDD.

- fecha_mas_dias(aaaammdd, cantidad_dias): Retorna una fecha que resulta de sumar una cantidad de días a una fecha dada.

- fecha_menos_dias(aaaammdd, cantidad_dias): Retorna una fecha que resulta de restar una cantidad de días a una fecha dada.

- obtener_fecha_random(anio): Genera una fecha aleatoria dentro del rango del año indicado.

- el_anio(aaaammdd): Retorna el año de una fecha en formato AAAAMMDD.

- el_mes(aaaammdd): Retorna el mes de una fecha en formato AAAAMMDD.

- el_dia(aaaammdd): Retorna el día de una fecha en formato AAAAMMDD.

- str_fecha(aaaammdd): Retorna una cadena con la fecha en formato DD/MM/AAAA.

- nombre_del_mes(m): Retorna el nombre del mes correspondiente a un número de mes.

- str_fecha_larga(aaaammdd): Retorna una cadena con la fecha en formato DD de "NOMBRE DEL MES" de AAAA.

- str_fecha_dia(aaaammdd): Retorna una cadena con la fecha en formato "NOMBRE_DIA" día de "NOMBRE DEL MES" de AAAA.

- numero_de_dia_semana(aaaammdd): Retorna el número del día de la semana para una fecha en formato AAAAMMDD.

- nombre_del_dia_semana(numero_dia_semana): Retorna el nombre del día de la semana correspondiente a un número de día de la semana.

Autor: Curso Python Itmaster
Fecha: 06/06/2023
"""

import random  # importo el modulo random
# from random import *
# import random as r

import datetime  # importo el modulo datetime


def isfecha_valida(aaaammdd):
    """
    Retorna True si la fecha es valida, False en caso contrario

    """
    a = el_anio(aaaammdd)
    m = el_mes(aaaammdd)
    d = el_dia(aaaammdd)

    if m < 1 or m > 12:
        return False
    
    cantidad_dias =  obtener_cantidad_dias_del_mes(m, a)
    if d < 1 or d > cantidad_dias:
        return False
    
    return True


def isbisiesto(anio):
    """
    Retorna True si el año es bisiesto, False en caso contrario
    """
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0


def obtener_cantidad_dias_del_mes(mes, anio):
    """
    Retorna la cantidad de dias del mes indicado en el año indicado
    """
    cantidad = 31
    if mes in (4, 6, 9, 11):
        cantidad = 30
    elif mes == 2:
        if isbisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28
    return cantidad


def crear_fecha(dia, mes, anio):
    """
    Retorna una fecha con el formato AAAAMMDD

    """
    return (anio*10000) + (mes*100) + dia  # AAAAMMDD


def obtener_fecha_actual():
    """
    Retorna la fecha actual del sistema en formato AAAAMMDD.

    """
    # Obtiene la fecha y hora actual como un objeto datetime
    fecha_actual = datetime.datetime.now().date()
    
    # Extrae el día, mes y año de la fecha actual
    d = fecha_actual.day
    m = fecha_actual.month
    a = fecha_actual.year
    
    # Retorna la fecha actual en formato AAAAMMDD 
    return crear_fecha(d, m, a)


def fecha_mas_dias(aaaammdd, cantidad_dias):
    """
    Retorna una fecha con la cantidad de dias indicada a partir de la fecha indicada
    """
    a = el_anio(aaaammdd)
    m = el_mes(aaaammdd)
    d = el_dia(aaaammdd)
    while cantidad_dias > 0:
        cantidad_dias -= 1
        d += 1
        if d > obtener_cantidad_dias_del_mes(m, a):
            d = 1
            m += 1
            if m > 12:
                m = 1
                a += 1
    return crear_fecha(d, m, a)


def fecha_menos_dias(aaaammdd, cantidad_dias):
    """
    Retorna una fecha con la cantidad de dias indicada a partir de la fecha indicada
    """
    a = el_anio(aaaammdd)
    m = el_mes(aaaammdd)
    d = el_dia(aaaammdd)
    while cantidad_dias > 0:
        cantidad_dias -= 1
        d -= 1
        if d < 1:
            m -= 1
            if m < 1:
                m = 12
                a -= 1
            d = obtener_cantidad_dias_del_mes(m, a)
    return crear_fecha(d, m, a)


def obtener_fecha_random(anio):
    """
    Genera una fecha aleatoria en el rango del año indicado
    """

    mes = random.randint(1, 12)
    cantidad_dias = obtener_cantidad_dias_del_mes(mes, anio)
    dia = random.randint(1, cantidad_dias)
    return crear_fecha(dia, mes, anio)


def el_anio(aaaammdd):
    """
    Retorna el año de una fecha con el formato AAAAMMDD

    AAAA <== |MMDD
    """
    return aaaammdd//10000  # AAAA <== |MMDD


def el_mes(aaaammdd):
    """
    Retorna el mes de una fecha con el formato AAAAMMDD

    AAAA| ==> MM <== |DD
    """
    return (aaaammdd//100) % 100  # AAAA| ==> MM <==|DD


def el_dia(aaaammdd):
    """
    Retorna el dia de una fecha con el formato AAAAMMDD

    AAAAMM| ==> DD
    """
    return aaaammdd % 100  # AAAAMM| ==> DD


def nombre_del_mes(mes):
    """
    Retorna el nombre del mes indicado
    """
    nombre = ""
    if mes == 1:
        nombre = "Enero"
    elif mes == 2:
        nombre = "Febrero"
    elif mes == 3:
        nombre = "Marzo"
    elif mes == 4:
        nombre = "Abril"
    elif mes == 5:
        nombre = "Mayo"
    elif mes == 6:
        nombre = "Junio"
    elif mes == 7:
        nombre = "Julio"
    elif mes == 8:
        nombre = "Agosto"
    elif mes == 9:
        nombre = "Septiembre"
    elif mes == 10:
        nombre = "Octubre"
    elif mes == 11:
        nombre = "Noviembre"
    elif mes == 12:
        nombre = "Diciembre"

    return nombre


def str_fecha(aaaammdd):
    """
    Retorna una cadena con la fecha en formato DD/MM/AAAA
    """
    
    return f"{el_dia(aaaammdd):02}/{el_mes(aaaammdd):02}/{el_anio(aaaammdd):04}"


def str_fecha_larga(aaaammdd):
    """
    Retorna una cadena con la fecha en formato DD de "NOMBRE DEL MES" de AAAA
    """
    
    d = el_dia(aaaammdd)
    nombre_mes = nombre_del_mes(el_mes(aaaammdd))
    a = el_anio(aaaammdd)

    return f"{d:02} de {nombre_mes} de {a:04}"


def str_fecha_dia(aaaammdd):
    """
    Retorna una cadena con la fecha en formato "NOMBRE_DIA" dia de "NOMBRE DEL MES" de AAAA
    """

    nombre_dia = nombre_del_dia_semana(numero_de_dia_semana(aaaammdd))    
    nombre_mes = nombre_del_mes(el_mes(aaaammdd))
    
    return f"{nombre_dia} {el_dia(aaaammdd):02} de {nombre_mes} de {el_anio(aaaammdd):04}"


def numero_de_dia_semana(aaaammdd):
    """
    Retorna el número del día de la semana para una fecha en formato AAAAMMDD.
    El domingo se representa con el número 0, y el sábado con el número 6.
    
    """

    # Convierte la fecha en formato AAAAMMDD a un objeto datetime
    fecha = datetime.datetime(el_anio(aaaammdd), el_mes(aaaammdd), el_dia(aaaammdd))
    
    # Obtiene el número del día de la semana de la fecha
    # El método weekday() retorna un número del 0 al 6, donde el lunes es 0 y el domingo es 6
    # Para representar el domingo como el día 0 y el sábado como el día 6, 
    # se utiliza el ajuste: (weekday() + 1) % 7
    
    numero_dia_semana = (fecha.weekday() + 1) % 7
    
    # Por ejemplo, si fecha.weekday() retorna 0 (lunes), se suma 1 y se obtiene 1. 
    # Al aplicar el operador módulo 7, el resultado es 1, lo cual representa correctamente al día lunes.
    # Si fecha.weekday() retorna 6 (domingo), se suma 1 y se obtiene 7. 
    # Al aplicar el operador módulo 7, el resultado es 0, lo cual representa correctamente al día domingo.
    
    # Retorna el número del día de la semana
    return numero_dia_semana


def nombre_del_dia_semana(numero_dia_semana):
    """
    Retorna el nombre del día de la semana para un número de día de la semana.
    """

    dias_semana = ( 'Domingo','Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado')    # TUPLA
    #                   0        1        2          3           4           5         6
    return dias_semana[numero_de_dia_semana]  

    """
    OTRA MANERA

    nombre_dia_espanol = ""
    if numero_dia_semana == 0:
        nombre_dia_espanol = "Domingo"
    elif numero_dia_semana == 1:
        nombre_dia_espanol = "Lunes"
    elif numero_dia_semana == 2:
        nombre_dia_espanol = "Martes"
    elif numero_dia_semana == 3:
        nombre_dia_espanol = "Miércoles"
    elif numero_dia_semana == 4:
        nombre_dia_espanol = "Jueves"
    elif numero_dia_semana == 5:
        nombre_dia_espanol = "Viernes"
    elif numero_dia_semana == 6:
        nombre_dia_espanol = "Sábado"

    return nombre_dia_espanol
"""


def test():
    print(f"\n\n\nEsta compilando la prueba de un modulo de funciones de fecha (AAAAMMDD)!\n\n")

if __name__ == "__main__":
    test()
