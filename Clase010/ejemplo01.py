
import random

"""
20210000
    0700
+     25
------------
20210725

"""


def isfecha_valida(aaaammdd):
    pass

def isbisiesto(a):
    es = a%4 == 0 and a%100 != 0 or a%400 == 0  # se o ano é DIV por 4 e ademas nao é DIV ( é distindo de zero, que sig , nao é div.)  
    return es                                   # por 100 ou tem que ser div. por 400 ( CONDICAO DE ANO BISEXTO)
    


def obtener_cantidad_dias_del_mes(m,anio):

    cantidad = 31
    if m in (4,6,9,11):  # SE O MES É 4,6,9,11
        cantidad = 30    # a quantidade é 30

    elif m == 2:
        if isbisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28

    return cantidad



def obtener_fecha_ranom(anio):

    m = random.randint(1,12)
    cantidad_dias = obtener_cantidad_dias_del_mes(m,anio)
    d = random.randint(1,cantidad_dias)

    return (anio*10000) + (m*100) + d # AAAAMMDD
    

def el_anio(aaaammdd):
    """
    retorna el año de una fecha

    AAAA < === MMDD

    """
    return aaaammdd//10000 # AAAA < === MMDD

def el_mes(aaaammdd):
    return (aaaammdd//100)%100  # AAAAMM | ==>  DD

def el_dia(aaaaammdd):
    return aaaaammdd%100  # AAAA| ==> MM <==| DD

def str_fecha(aaaammdd):
    
    d = el_dia(aaaammdd)   # dia
    m = el_mes(aaaammdd)   # mes
    a = el_anio(aaaammdd)  # anio

    return f"{d:02}/{m:02}/{a:04}"


"""

PROGRAMA PRINCIPAL

"""

def main():
    fecha = obtener_fecha_ranom(2023)        # AAAAMMDD (fecha)
    cadena = str_fecha(fecha)

    print(cadena)


    # anio = el_anio(fecha)        # anio = fecha//10000 # AAAA <== | MMDD
    # dia = el_dia (fecha)         # fecha%100 # AAAAMM | ==>  DD
    # mes =  el_mes (fecha)        # (fecha//100)%100  # AAAA| ==> MM <==| DD


    

    # x = str (fecha)

    # print( str_fecha(fecha) )

    # print(f"{dia}/{mes}/{anio}")


main() # LLAMO A LA FUNCION PRINCIPAL