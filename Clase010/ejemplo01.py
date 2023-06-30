



"""
PROGRAMA PRINCIPAL
"""

def main():
    fecha = int(19851217)  # AAAAMMDD (fecha)
    anio = fecha//10000 # AAAA <== | MMDD
    dia = fecha%100 # AAAAMM | ==>  DD
    mes = (fecha//100)%100  # AAAA| ==> MM <==| DD

    print(f"{dia}/{mes}/{anio}")


main() # LLAMO A LA FUNCION PRINCIPAL