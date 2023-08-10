"""
Modulo que contiene las clases que representan los mazos de cartas.

Mazo: Clase abstracta que representa un mazo de cartas.

    - Métodos publicos:
        - poner: Agrega una carta al mazo.
        - sacar: Saca una carta del mazo.
        - tapar: Tapar todas las cartas del mazo.
        - mezclar: Mezcla las cartas del mazo.
        - isvacio: Devuelve True si el mazo esta vacio.

    - Métodos especiales implementados:
        - __str__: Devuelve una cadena con las cartas del mazo.
        - __len__: Devuelve la cantidad de cartas del mazo.
        - __iter__: Devuelve un iterador de las cartas del mazo.
        - __repr__: Devuelve una cadena con las cartas del mazo.

    - Métodos abstractos:
        - llenar: Llena el mazo con las cartas del juego.


MazoPoker: Clase que representa un mazo de cartas de poker.

    - Métodos publicos:
        - llenar: Llena el mazo con las cartas del juego.

MazoBlackJack: Clase que representa un mazo de cartas de BlackJack.

    - Métodos publicos:
        - llenar: Llena el mazo con las cartas del juego.
"""
from typing import List
from cartas import Carta, CartaPoker
from abc import ABC, abstractmethod
from random import shuffle
import sys
sys.path.append('recursos/')


class Mazo(ABC):
    """
    Clase abstracta que representa un mazo de cartas.
    """

    def __init__(self) -> None:
        super().__init__() # Inicializa la clase base.
        """
        Inicializa un mazo de cartas vacio.
        """
        self.__las_cartas: List[Carta] = [] # Lista de cartas del mazo.

    def poner(self, carta: Carta, index: int = -1) -> None:
        """
        Agrega una carta al mazo.

        Args:
            carta (Carta): Carta a agregar.
            index (int, optional): Posicion donde se agrega la carta. Defaults to -1.
            Si index es -1 la carta se agrega al final del mazo.
            De lo contrario se agrega en la posicion index.
        """
        if index <= -1:
            self.__las_cartas.append(carta)
        else:
            self.__las_cartas.insert(index, carta)

    def sacar(self, index: int = 0) -> Carta:
        """
        Saca una carta del mazo.

        Args:
            index (int, optional): Posicion de la carta a sacar. Defaults to 0.
            Si index es 0 se saca la primera carta del mazo.
            De lo contrario se saca la carta en la posicion index.

        Returns:
            Carta: Carta sacada del mazo.

        Raises:
            IndexError: Si el index esta fuera de rango.
        """
        if 0 <= index < len(self):
            return self.__las_cartas.pop(index)
        raise IndexError('Index fuera de rango.')

    def tapar(self,index:int=None) -> None:
        """
        Tapar una o todas las cartas del mazo.
        si index es None se tapan todas las cartas del mazo.
        si index es un entero se tapa la carta en la posicion index.
        """
        if index:            
            self.__las_cartas[index].tapar()
        else:
            for carta in self:
                carta.tapar()

    def destapar(self,index:int=None) -> None:
        """
        Destapar todas las cartas del mazo.
        """
        if index:
            self.__las_cartas[index].destapar()
        else:
            for carta in self:
                carta.destapar()

    def mezclar(self) -> None:
        """
        Mezcla las cartas del mazo.
        """
        shuffle(self.__las_cartas)

    def __repr__(self) -> str:
        return ','.join([carta for carta in self.__las_cartas])

    def __str__(self) -> str:
        """
        Devuelve una cadena con las cartas del mazo.
        """
        return ''.join([str(carta) for carta in self.__las_cartas])

    def __len__(self) -> int:
        """
        Devuelve la cantidad de cartas del mazo.
        """
        return len(self.__las_cartas)

    def __iter__(self):
        """
        Devuelve un iterador para recorrer las cartas del mazo.
        """
        return iter(self.__las_cartas)

    def isvacio(self) -> bool:
        """
        Devuelve True si el mazo está vacío.
        """
        return len(self) == 0

    @abstractmethod
    def llenar(self) -> None:
        """
        Llena el mazo con las cartas correspondientes.
        """
        pass


class MazoPoker(Mazo):
    """
    Clase que representa un mazo de cartas de poker.
    """

    # Cantidad de cartas del mazo.
    CANTIDAD_CARTAS = 52

    @classmethod
    def get_cantidad_cartas(cls) -> int:
        """
        Devuelve la cantidad de cartas del mazo.
        """
        return cls.CANTIDAD_CARTAS

    def __init__(self) -> None:
        super().__init__() # Llama al constructor de la clase padre.
        

    def llenar(self) -> None:
        """
        Llena el mazo con las 52 cartas de poker.
        """
        for numero in range(1, 14): # Llena el mazo con 52 cartas.
            for palo in range(1, 5):
                self.poner(CartaPoker(numero, palo))

    
    def sacar(self, index: int = 0) -> CartaPoker:
        return super().sacar(index)
    
    def poner(self, carta: CartaPoker, index: int = -1) -> None:
        return super().poner(carta, index)


class MazoBlackJack(Mazo):
    """
    Clase que representa un mazo de cartas de blackjack.
    """

    # Cantidad de cartas del mazo.
    CANTIDAD_CARTAS = 52 * 10

    @classmethod
    def get_cantidad_cartas(cls) -> int:
        """
        Devuelve la cantidad de cartas del mazo.
        """
        return cls.CANTIDAD_CARTAS
    
    def __init__(self) -> None:
        super().__init__() # Llama al constructor de la clase padre.

    def llenar(self) -> None:
        """
        Llena el mazo con las con 10 mazos de 52 cartas de poker.
        """
        for mazo in range(10): # Llena el mazo con 10 mazos de 52 cartas.
            for numero in range(1, 14):
                for palo in range(1, 5):
                    self.poner(CartaPoker(numero, palo))

    
    def sacar(self, index: int = 0) -> CartaPoker:
        """
        Saca una carta del mazo.
        Sobreescribe el metodo sacar de la clase padre.

        Args:
            index (int, optional): Posicion de la carta a sacar. Defaults to 0.

        Returns:
            CartaPoker: Carta sacada del mazo.

        Raises:
            IndexError: Si el index esta fuera de rango.
        """    
        return super().sacar(index)
    
    def poner(self, carta: CartaPoker, index: int = -1) -> None:
        """
        Agrega una carta al mazo.
        Sobreescribe el metodo poner de la clase padre.

        Args:
            carta (CartaPoker): Carta a agregar.
            index (int, optional): Posicion donde se agrega la carta. Defaults to -1.
            Si index es -1 la carta se agrega al final del mazo.
            De lo contrario se agrega en la posicion index.

        Raises:
            IndexError: Si el index esta fuera de rango.
        """
        super().poner(carta,index)
    
    def suma(self)->int:
        cantidad_unos = 0
        suma_numeros = 0
        for carta in self:
            if carta.getNumero() == 1:
                cantidad_unos += 1
            elif carta.getNumero() <= 10:
                suma_numeros += carta.getNumero()
            else:
                suma_numeros += 10

        suma = 0

        if cantidad_unos == 0:
            suma = suma_numeros
        elif cantidad_unos == 1:
            if suma_numeros + 11 > 21:
                suma = suma_numeros + 1
            else:
                suma = suma_numeros + 11        
        else:   
            if (suma_numeros + 11 + cantidad_unos - 1) > 21:
                suma = suma_numeros + 11 + cantidad_unos - 1
            else:
                suma = suma_numeros + cantidad_unos

        return suma            

def test():
    mazo = MazoBlackJack()
    mazo.llenar()
    mazo.mezclar()
    print(mazo)
    print("Cantidad de cartas del mazo:", len(mazo))
    carta = mazo.sacar()
    print("Saco la primera carta:", carta)
    if carta.isfigura():
        print("Es una figura")
    else:
        print("No es una figura")
    if carta.isNegra():
        print("Es negra")
    else:
        print("Es roja")
    print("Cantidad de cartas del mazo:", len(mazo))
    print("El mazo esta vacio?", mazo.isvacio())
    mazo.poner(carta)
    print("Cantidad de cartas del mazo:", len(mazo))
    mazo.tapar()
    print(mazo)

    
    

if __name__ == '__main__':
    test()
