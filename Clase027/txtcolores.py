"""
Módulo para colorear texto en la consola de Windows.

Este módulo utiliza la librería colored (https://pypi.org/project/colored/).

Funciones:
    - strclr: Devuelve el texto indicado con el color de texto, fondo y estilo indicado.
    - strclr_random: Devuelve el texto indicado con un color de texto aleatorio.
"""
import random
from colored import fore, back, style


# escribir los comentarios con la forma pep8
def strclr(texto, color_texto: str | int = None, color_fondo: str | int = None, estilo: str | int = None) -> str:
    """
    función que devuelve el texto indicado con el color de texto, fondo y estilo indicado.

    args:
        - texto: texto a devolver con el color indicado

        - color_texto: color de texto a utilizar. Puede ser un string con el nombre del color o un entero con el número de color.

        - color_fondo: color de fondo a utilizar. Puede ser un string con el nombre del color o un entero con el número de color.

        - estilo: estilo a utilizar. Puede ser un string con el nombre del estilo o un entero con el número de estilo.

    @return: 
        - devuelve el texto indicado con el color de texto, fondo y estilo indicado.

    @raise: 
        - ValueError si el color o estilo indicado no existe.

    @example: 
       
        - strclr('texto', 'red', 'blue', 'bold')
        - strclr('texto', 'red', 'blue')
        - strclr('texto', 'red')
        - strclr('texto')
        - strclr('texto', estilo='bold')
        - strclr('texto', color_texto='red', color_fondo='blue', estilo='bold')
        - strclr('texto', color_texto= 11,    color_fondo= 12,    estilo= 1)

    """
    try:
        color_str = ''
        if color_texto:
            color_str += fore(color_texto)
        if color_fondo:
            color_str += back(color_fondo)
        if estilo:
            color_str += style(estilo)

        color_str_reset = style('reset')
        return (f'{color_str}{texto}{color_str_reset}')
    except Exception as e:
        raise ValueError(f'Error al aplicar el color o estilo indicado:\n{e}')


def strclr_random(texto: str, cantidad_colores: int=250) -> str:
    """
    Devuelve el texto indicado con una letra de cada color con cantidad de colores random.

    args:
        - texto: texto a devolver con el color indicado

        - cantidad_colores: cantidad de colores a utilizar.

    @return: 
        - devuelve el texto indicado con una letra de cada color con cantidad de colores random.
    
    @raise: 
        - ValueError si el color o estilo indicado no existe.
    """
    try:
        color_str = ''
        for letra in texto:
            color_str += fore(random.randint(0, cantidad_colores)) + letra            
        color_str_reset = style('reset')
        return (f'{color_str}{color_str_reset}')
    except Exception as e:
        raise ValueError(f'Error al aplicar el color o estilo indicado:\n{e}')

# Código para probar el módulo
if __name__ == "__main__":
    texto_prueba = "¡Hola, esto es un texto de prueba!"
    print(strclr(texto_prueba, 15, 22))
    print(strclr(texto_prueba, 15, 22, 1))
    print(strclr_random(texto_prueba, 250))
    print(strclr(texto_prueba, 'red', 'blue', 'bold'))
