from os import system
def isint(str_numero):
    """
    Devuelve True si str_numero es un int, False en caso contrario
    """
    try:
        int(str_numero)
    except:
        return False
    return True

def isfloat(str_numero):
    """
    Devuelve True si str_numero es un float, False en caso contrario
    """
    try:
        float(str_numero)
    except:
        return False
    return True

def leer_entero(mensaje):
    """
    Permite leer un entero desde el teclado
    """
    todo_ok = False
    while not todo_ok:
        cadena = input(mensaje)
        if isint(cadena):
            todo_ok = True
        else:
            print(f"{cadena} No es un int.")    
    return int(cadena)

def leer_float(mensaje):
    """
    Permite leer un float desde el teclado
    """
    todo_ok = False
    while not todo_ok:
        cadena = input(mensaje)
        if isfloat(cadena):
            todo_ok = True
        else:
            print(f"{cadena} No es un float.")    
    return int(cadena)

def leer_entero_rango(mensaje, minimo, maximo):
    """
    Permite leer un entero desde el teclado en un rango determinado
    """
    todo_ok = False
    while not todo_ok:
        numero = leer_entero(mensaje)
        if minimo <= numero <= maximo:
            todo_ok = True
        else:
            print(f"{numero} No esta en el rango {minimo} a {maximo}.")    
    return numero

def leer_float_rango(mensaje, minimo, maximo):
    """
    Permite leer un float desde el teclado en un rango determinado
    """
    todo_ok = False
    while not todo_ok:
        numero = leer_float(mensaje)
        if minimo <= numero <= maximo:
            todo_ok = True
        else:
            print(f"{numero} No esta en el rango {minimo} a {maximo}.")    
    return numero


def titulo(texto,largo):    
    return f"{'-'*largo}\n{texto.title().center(largo)}\n{'-'*largo}"

def obtener_largo_opcion_mas_larga(tupla_opciones):
    maximo_largo = -float('inf')
    for i,texto in enumerate(tupla_opciones):
        if len(texto) > maximo_largo:
            maximo_largo = len(texto)
    return maximo_largo

def menu(tupla_opciones):
    largo = obtener_largo_opcion_mas_larga(tupla_opciones)
    system("cls")
    for index,opcion in enumerate(tupla_opciones):
        if index == 0: 
            print(titulo(opcion,largo))
        else:
            print(opcion.title())
    return leer_entero_rango("Ingrese una opcion: ",1,8)
    
def continua(texto_pregunta):
    resp = input(f'Continua {texto_pregunta} [S/N]: ').upper()
    if resp == 'S':
        return True
    return False


if __name__ == '__name__':
    print("Esto es un modulo no un programa")