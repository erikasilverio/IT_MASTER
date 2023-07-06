from os import system
"""
Este modulo contiene funciones de utilidad para el manejo de datos

Funciones:

- isint(str_numero): Devuelve True si str_numero es un int, False en caso contrario

- isfloat(str_numero): Devuelve True si str_numero es un float, False en caso contrario

- leer_entero(mensaje): Permite leer un entero desde el teclado

- leer_float(mensaje): Permite leer un float desde el teclado

- leer_entero_rango(mensaje, minimo, maximo): Permite leer un entero desde el teclado en un rango determinado

- leer_float_rango(mensaje, minimo, maximo): Permite leer un float desde el teclado en un rango determinado

- limpiar_pantalla(): Limpia la pantalla

- pausar(): Pausa la ejecucion del programa

- menu(mensaje, opciones): Muestra un menu de opciones y permite elegir una

- continua(mensaje): Pregunta al usuario si desea continuar
"""

def isint(str_numero):
    """
    Devuelve True si str_numero es un int, False en caso contrario

    Args:
        str_numero (str): Cadena a evaluar

    Returns:
        bool: True si str_numero es un int, False en caso contrario
    """
    try: # Intenta convertir str_numero a int
        int(str_numero)
    except: # Si no puede convertirlo devuelve False
        return False
    return True # Si puede convertirlo devuelve True

def isfloat(str_numero):
    """
    Devuelve True si str_numero es un float, False en caso contrario

    Args:
        str_numero (str): Cadena a evaluar

    Returns:
        bool: True si str_numero es un float, False en caso contrario
    """
    try: # Intenta convertir str_numero a float
        float(str_numero)
    except: # Si no puede convertirlo devuelve False
        return False # Si puede convertirlo devuelve True
    return True # Si puede convertirlo devuelve True

def leer_entero(mensaje):
    """
    Permite leer un entero desde el teclado

    Args:
        mensaje (str): Mensaje a mostrar al usuario

    Returns:    
        int: Entero ingresado por el usuario
    """
    todo_ok = False # Bandera para saber si se ingreso un int
    while not todo_ok: # Mientras no se haya ingresado un int
        cadena = input(mensaje) # Se pide un numero
        if isint(cadena): # Si es un int
            todo_ok = True # Se cambia la bandera a True
        else: # Si no es un int
            print(f"{cadena} No es un int.") # Se informa que no es un int    
    return int(cadena) # Se devuelve el int

def leer_float(mensaje):
    """
    Permite leer un float desde el teclado

    Args:
        mensaje (str): Mensaje a mostrar al usuario

    Returns:
        float: Float ingresado por el usuario
    """
    todo_ok = False # Bandera para saber si se ingreso un float
    while not todo_ok: # Mientras no se haya ingresado un float
        cadena = input(mensaje) # Se pide un numero
        if isfloat(cadena): # Si es un float
            todo_ok = True # Se cambia la bandera a True
        else: # Si no es un float
            print(f"{cadena} No es un float.") # Se informa que no es un float   
    return int(cadena) # Se devuelve el float

def leer_entero_rango(mensaje, minimo, maximo):
    """
    Permite leer un entero desde el teclado en un rango determinado

    Args:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (int): Valor minimo del rango    
        maximo (int): Valor maximo del rango    

    Returns:
        int: Entero ingresado por el usuario
    """
    todo_ok = False # Bandera para saber si se ingreso un int
    while not todo_ok: # Mientras no se haya ingresado un int
        numero = leer_entero(mensaje) # Se pide un numero
        if minimo <= numero <= maximo: # Si esta en el rango
            todo_ok = True # Se cambia la bandera a True
        else: # Si no esta en el rango
            # Se informa que no esta en el rango
            print(f"{numero} No esta en el rango {minimo} a {maximo}.")    
    return numero # Se devuelve el int en el rango

def leer_float_rango(mensaje, minimo, maximo):
    """
    Permite leer un float desde el teclado en un rango determinado

    Args:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (float): Valor minimo del rango
        maximo (float): Valor maximo del rango

    Returns:
        float: Float ingresado por el usuario
    """
    todo_ok = False # Bandera para saber si se ingreso un float
    while not todo_ok: # Mientras no se haya ingresado un float
        numero = leer_float(mensaje) # Se pide un numero
        if minimo <= numero <= maximo: # Si esta en el rango
            todo_ok = True # Se cambia la bandera a True
        else: # Si no esta en el rango
            # Se informa que no esta en el rango
            print(f"{numero} No esta en el rango {minimo} a {maximo}.")    
    return numero # Se devuelve el float en el rango

def titulo(texto,largo):    
    """
    Devuelve un titulo centrado con guiones

    Args:
        texto (str): Texto a mostrar en el titulo
        largo (int): Largo del titulo

    Returns:
        str: Titulo centrado con guiones
    """
    return f"{'-'*largo}\n{texto.title().center(largo)}\n{'-'*largo}"

def obtener_largo_opcion_mas_larga(tupla_opciones):
    """
    Devuelve el largo de la opcion mas larga

    Args:
        tupla_opciones (tuple): Tupla con las opciones

    Returns:
        int: Largo de la opcion mas larga
    """
    maximo_largo = -float('inf') # Se inicializa en infinito negativo
    for i,texto in enumerate(tupla_opciones): # Se recorre la tupla
        if len(texto) > maximo_largo: # Si el largo es mayor al maximo
            maximo_largo = len(texto) # Se actualiza el maximo
    return maximo_largo # Se devuelve el largo maximo

def menu(tupla_opciones):
    """
    Muestra un menu con las opciones de la tupla
    
    La primera opcion es el titulo
    
    Las demas son las opciones
    
    Args:
        tupla_opciones (tuple): Tupla con las opciones

    Returns:    
        int: Opcion elegida por el usuario
    """

    largo = obtener_largo_opcion_mas_larga(tupla_opciones)
    system("cls") # Limpia la pantalla
    for index,opcion in enumerate(tupla_opciones): # Se recorre la tupla
        if index == 0:  # Si es el titulo
            print(titulo(opcion,largo)) # Se muestra el titulo
        else: # Si es una opcion
            print(opcion.title()) # Se muestra la opcion
    return leer_entero_rango("Ingrese una opcion: ",1,len(tupla_opciones)-1)
    
def continua(texto_pregunta):
    """
    Devuelve True si el usuario responde S, False en caso contrario

    Args:
        texto_pregunta (str): Texto a mostrar al usuario

    Returns:
        bool: True si el usuario responde S, False en caso contrario
    """
    # Se pide al usuario que responda S o N
    resp = input(f'Continua {texto_pregunta} [S/N]: ').upper()
    if resp == 'S': # Si responde S
        return True # Devuelve True
    return False # Devuelve False


if __name__ == '__name__':
    print("Esto es un modulo no un programa")