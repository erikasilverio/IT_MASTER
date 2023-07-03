






def sumar(*parametros):
    print(parametros)
    s = 0
    for x in parametros:
        s += x
    return s


def main():
    suma = sum((2,3,4,5,7))
    print(suma)
    suma = sumar(1,2)
    print(suma)
    suma = sumar (1,2,3,4,5,6)
    print(suma)

main()