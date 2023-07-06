import datetime

def ishora_valida(hhmmss):
    """
    Retorna True si la hora es válida, False en caso contrario
    
    Args:
        hhmmss (int): hora en formato HHMMSS

    Returns:
        bool: True si la hora es válida, False en caso contrario        
    """
    # Separo horas, minutos y segundos
    h = las_horas(hhmmss)
    m = los_minutos(hhmmss)
    s = los_segundos(hhmmss)

    # Si la hora es menor a 0 o mayor a 23, no es válida
    if h < 0 or h > 23:
        return False

    # Si los minutos son menores a 0 o mayores a 59, no es válida
    if m < 0 or m > 59:
        return False

    # Si los segundos son menores a 0 o mayores a 59, no es válida
    if s < 0 or s > 59:
        return False

    return True # Si llego hasta acá, es porque la hora es válida


def crear_hora(hora, minuto, segundo):
    """
    Retorna una hora con el formato HHMMSS

    Args:
        hora (int): Hora.
        minuto (int): Minuto.
        segundo (int): Segundo.

    Returns:
        int: Hora en formato HHMMSS.    
    """
    return (hora * 10000) + (minuto * 100) + segundo  # HHMMSS


def las_horas(hhmmss):
    """
    Retorna la hora de una hora en formato HHMMSS

    HH <== |MMSS

    Args:
        hhmmss (int): Hora en formato HHMMSS.

    Returns:
        int: Hora en formato HH.
    """
    return hhmmss // 10000  # HH <== |MMSS


def los_minutos(hhmmss):
    """
    Retorna el minuto de una hora en formato HHMMSS

    HH| ==> MM <== |SS

    Args:
        hhmmss (int): Hora en formato HHMMSS.

    Returns:
        int: Minuto de la hora en formato MM.
    """
    return (hhmmss // 100) % 100  # HH| ==> MM <== |SS


def los_segundos(hhmmss):
    """
    Retorna el segundo de una hora en formato HHMMSS

    HHMM| ==> SS

    Args:
        hhmmss (int): Hora en formato HHMMSS.

    Returns:
        int: Segundo de la hora en formato SS.
    """
    return hhmmss % 100  # HHMM| ==> SS


def obtener_hora_actual():
    """
    Retorna la hora actual del sistema en formato HHMMSS.

    Returns:
        int: Hora actual en formato HHMMSS.
    """
    # Obtiene la fecha y hora actual como un objeto datetime
    hora_actual = datetime.datetime.now().time()

    # Extrae la hora, minuto y segundo de la hora actual
    h = hora_actual.hour
    m = hora_actual.minute
    s = hora_actual.second

    # Retorna la hora actual en formato HHMMSS
    return crear_hora(h, m, s)


def str_hora(hhmmss):
    """
    Retorna una cadena con la hora en formato HH:MM:SS.

    Args:
        hhmmss (int): Hora en formato HHMMSS.

    Returns:    
        str: Hora en formato HH:MM:SS.

    """
    return f"{las_horas(hhmmss):02}:{los_minutos(hhmmss):02}:{los_segundos(hhmmss):02}"


def a_segundos(hhmmss):
    """
    Convierte una hora en formato HHMMSS a segundos.

    Args:
        hhmmss (int): Hora en formato HHMMSS.

    Returns:
        int: Hora convertida a segundos.
    """
    h = las_horas(hhmmss)
    m = los_minutos(hhmmss)
    s = los_segundos(hhmmss)

    total_segundos = h * 3600 + m * 60 + s  # Convertir a segundos

    return total_segundos

if __name__ == '__main__':
    hora = obtener_hora_actual()
    print(hora)
    print(str_hora(hora))
    