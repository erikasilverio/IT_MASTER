from abc import ABC, abstractmethod
from mazos import Mazo,MazoBlackJack
from cartas import Carta,CartaPoker



class JugadorCartas(ABC):
    def __init__(self,nombre:str,mano:Mazo) -> None:
        super().__init__()
        self.__nombre:str = nombre
        self.__mano:Mazo = mano

    def poner(self, carta: Carta, index: int = -1) -> None:
        self.__mano.poner(carta,index)

    def sacar(self, index: int = 0) -> Carta:
        return self.__mano.sacar(index)

    def tieneCartas(self)->bool:
        return not self.__mano.isvacio()
    
    def getNombre(self)->str:
        return self.__nombre
    
    def getMano(self)->Mazo:
        return self.__mano
    
class JugadorBlackjack(JugadorCartas):
    
    def __init__(self, nombre: str ) -> None:
        super().__init__(nombre, MazoBlackJack())

    def poner(self, carta: CartaPoker, index: int = -1) -> None:
        self.getMano().poner(carta,index)

    def sacar(self, index: int = 0) -> CartaPoker:
        return self.getMano().sacar(index)

    def tieneBlackJack(self)->bool:        
        return len(self.getMano()) == 2 and self.getMano().suma() == 21

    def getMano(self)->MazoBlackJack:
        return self.getMano()

    @abstractmethod
    def sePlanta(self)->bool:
        pass


class Croupier(JugadorBlackjack):
    def __init__(self) -> None:
        super().__init__("Sr Croupier")

    def sePlanta(self)->bool:
        return self.getMano().suma() >= 17

class Cliente(JugadorBlackjack):
    def __init__(self, nombre: str,fichas:int) -> None:
        super().__init__(nombre)
        self.__fichas = fichas


class JugadorHumano(Cliente):
    
    def sePlanta(self)->bool:
        return self.getMano().suma() >= 17


class JugadorComputadora(Cliente):
    
    def sePlanta(self)->bool:
        return self.getMano().suma() >= 17




def test():
    pass


if __name__ == '__main__':
    test()

