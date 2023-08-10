"""
Módulo que contiene las clases que representan las cartas de un juego de cartas.

Carta: Clase abstracta que representa una carta de cualquier juego de cartas.

    - Métodos publicos:
        - getNumero: Devuelve el numero de la carta.
        - getPalo: Devuelve el palo de la carta.
        - tapar: Tapar la carta.
        - destapar: Destapar la carta.
        - istapada: Devuelve True si la carta esta tapada.
        - isdestapada: Devuelve True si la carta esta destapada.

    - Métodos especiales implementados:
        - __str__: Devuelve una cadena con la carta.
        - __repr__: Devuelve una cadena con la carta.
    
    - Métodos abstractos:
        - dibujo_palo: Devuelve el dibujo del palo de la carta.
        - dibujo_numero: Devuelve el dibujo del numero de la carta.

CartaPoker: Clase que representa una carta de poker.

    - Métodos publicos:
        - dibujo_palo: Devuelve el dibujo del palo de la carta.
        - dibujo_numero: Devuelve el dibujo del numero de la carta.
        - isRoja: Devuelve True si la carta es roja.
        - isNegra: Devuelve True si la carta es negra.
        - isPica: Devuelve True si la carta es pica.
        - isCorazon: Devuelve True si la carta es corazon.
        - isDiamante: Devuelve True si la carta es diamante.
        - isTrebol: Devuelve True si la carta es trebol.
        - isAs: Devuelve True si la carta es un as.
        - isfigura: Devuelve True si la carta es una figura.
"""

import sys
sys.path.append('recursos/')
from abc import ABC, abstractmethod
from txtcolores import strclr


class Carta(ABC):
    """
    Clase abstracta que representa una carta de cualquier juego de cartas.
    """

    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        """
        Inicializa una carta con un numero y un palo.
        Por defecto la carta no esta destapada.

        Args:
            numero (int): Numero de la carta.
            palo (int): Palo de la carta.
            tapada (bool, optional): Indica si la carta esta tapada. Defaults to False.
        """
        self.__numero: int = numero
        self.__palo: int = palo
        self.__tapada: bool = tapada

    def getNumero(self) -> int:
        """
        Devuelve el numero de la carta.
        """
        return self.__numero

    def getPalo(self) -> int:
        """
        Devuelve el palo de la carta.        
        """
        return self.__palo

    def tapar(self) -> None:
        """
        Tapar la carta.
        """
        self.__tapada = True

    def destapar(self) -> None:
        """
        Destapar la carta.
        """
        self.__tapada = False

    def istapada(self) -> bool:
        """
        Devuelve True si la carta esta tapada.
        """
        return self.__tapada

    def isdestapada(self) -> bool:
        """
        Devuelve True si la carta esta destapada.
        """
        return not self.isTapada()

    @abstractmethod
    def dibujo_numero(self)->str:
        """
        Devuelve el dibujo del numero de la carta.
        """
        pass

    @abstractmethod
    def dibujo_palo(self)->str:
        """
        Devuelve el dibujo del palo de la carta.
        """
        pass
    
    def __repr__(self) -> str:
        """
        Devuelve una cadena con la carta.
        """
        return f"{self.__class__.__name__}({self.getNumero()}, {self.getPalo()}, {self.istapada()})"

    def __str__(self) -> str:        
        """
        Devuelve el dibujo de la carta.
        """
        return f"{strclr('[','aquamarine_3')}{self.dibujo_numero()}{self.dibujo_palo()}{strclr(']','aquamarine_3')}"


class CartaPoker(Carta):

    NUMEROS = ('#', 'A', '2', '3', '4', '5', '6',
               '7', '8', '9', '10', 'J', 'Q', 'K')
    PALOS = ('#', '♥', '♦', '♣', '♠')

    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        super().__init__(numero, palo, tapada)

    def isRoja(self) -> bool:   
        """
        Devuelve True si la carta es roja. ==> Corazones o Diamantes
        """     
        return self.getPalo() == 1 or self.getPalo() == 2
    
    def isfigura(self) -> bool:
        """
        Devuelve True si la carta es una figura. ==> J, Q o K
        """
        return self.getNumero() > 10

    def isNegra(self) -> bool:
        """
        Devuelve True si la carta es negra. ==> Treboles o Picas
        """
        return not self.isRoja()

    def isPica(self) -> bool:
        """
        Devuelve True si la carta es pica.
        """
        return self.getPalo() == 4
    
    def isCorazon(self) -> bool:
        """
        Devuelve True si la carta es corazon.
        """
        return self.getPalo() == 1
    
    def isDiamante(self) -> bool:
        """
        Devuelve True si la carta es diamante.
        """
        return self.getPalo() == 2
    
    def isTrebol(self) -> bool:
        """
        Devuelve True si la carta es trebol.
        """
        return self.getPalo() == 3
    
    def isAs(self) -> bool:
        """
        Devuelve True si la carta es un as.
        """
        return self.getNumero() == 1

    def dibujo_numero(self)->str:
        if self.istapada():
            return strclr(CartaPoker.NUMEROS[0],'dark_orange')
        return strclr(CartaPoker.NUMEROS[self.getNumero()],'dark_orange')

    def dibujo_palo(self)->str:
        if self.istapada():
            return strclr(CartaPoker.PALOS[0], 'dark_orange')
        if self.isRoja():
            return strclr(CartaPoker.PALOS[self.getPalo()],'red_1')
        else:
            return strclr(CartaPoker.PALOS[self.getPalo()],'white')


def test():
    carta1 = CartaPoker(2, 3, True) 
    carta2 = CartaPoker(2, 3)
    print(carta1,carta2)
    carta1 = CartaPoker(1, 4, True) 
    carta2 = CartaPoker(1, 4)
    print(carta1,carta2)
    carta1 = CartaPoker(1, 1, True) 
    carta2 = CartaPoker(1, 1)
    print(carta1,carta2)
    


if __name__ == '__main__':
    test()
