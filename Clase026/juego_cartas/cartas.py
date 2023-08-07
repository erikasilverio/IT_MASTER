from abc import ABC,abstractclassmethod

class Carta(ABC):
    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        self.__numero = numero
        self.__palo = palo
        self.__tapada = tapada

    def setNumero(self, numero: int) -> None:
        self.__numero = numero

    def getNumero(self) -> int:
        return self.__numero

    def setPalo(self, palo: int) -> None:
        self.__palo = palo

    def getPalo(self) -> int:
        return self.__palo

    def tapar(self)->None:
        self.__tapada = True
    
    def destapar(self)->None:
        self.__tapada = False

    def isTapada(self) -> bool:
        return self.__tapada 

    def isDestapada(self) -> bool:
        return not self.isTapada()
    

    @abstractclassmethod
    def dibujo_numero(self):
        pass

    @abstractclassmethod

    def dibujo_palo(self):
        pass

    def __str__(self) -> str:
        return f'[{self.dibujo_numero()},{self.dibujo_palo()}]' 

class CartaPoker(Carta):
    
    NUMEROS = ('#','A','2','3','4','5','6','7','8','9','10','J','Q','K')               
    PALOS = ('#','♥','♦','♣','♠')

    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        super().__init__(numero, palo, tapada)

    def dibujo_numero(self):
        return CartaPoker.NUMEROS[self.getNumero()]
        

    def dibujo_palo(self):
        return CartaPoker.PALOS[self.getPalo()]


class CartaEspanola(Carta):
    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        super().__init__(numero, palo, tapada)

    def dibujo_numero(self):
        pass

    def dibujo_palo(self):
        pass

def test():
    carta1 = CartaPoker(2,3)
    
    print(carta1)

if __name__ == '__main__':
    test()