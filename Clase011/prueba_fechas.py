from fechas_int import *


def main():
    for i in range(10):
        fecha = obtener_fecha_random(2021)
        cantidad_dias = random.randint(1, 100)

        cadena = f"{str_fecha(fecha)} + {cantidad_dias} ==> {str_fecha(fecha_mas_dias(fecha,cantidad_dias))} - {cantidad_dias} ==> {str_fecha(fecha_menos_dias(fecha,cantidad_dias))}"
        print(cadena)
    fecha_actual = obtener_fecha_actual()
    for i in range(1000):
        nueva_fecha = fecha_mas_dias(fecha_actual, i)
        print(f"{str_fecha_dia(nueva_fecha)}")


main()
