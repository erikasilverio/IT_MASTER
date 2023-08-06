from abc import ABC,abstractmethod
from cartas import Carta,CartaPoker
from random import shuffle

class Mazo(ABC):
    def __init__(self) -> None:
        self.__las_cartas:list[Carta] = []

    def poner(self,carta:Carta,index:int=-1)->None:
        self.__las_cartas.insert(index,carta)
    
    def sacar(self,index:int=0)->Carta:
        self.__las_cartas.pop(index)
    
    def mezclar(self)->None:
        shuffle(self.__las_cartas)

    def __str__(self) -> str:       
        return ''.join([str(carta)for carta in self.__las_cartas])
    
    def len(self)->int:
        return len(self.__las_cartas)
    
    def isvacio(self)->bool:
        return len(self) == 0

    @abstractmethod
    def llenar(self)->None:
        pass

class MazoPoker(Mazo):
    def __init__(self) -> None:
        super().__init__()
    
    def llenar(self) -> None:
        for numero in range(1,53):
            for palo in range(1,5):
                self.poner(CartaPoker(numero,palo))

class MazoBlackJack(Mazo):
    def __init__(self) -> None:
        super().__init__()
    
    def llenar(self) -> None:
        for mazo in range(10):
            for numero in range(1,55):
                for palo in range(1,5):
                    self.poner(CartaPoker(numero,palo))


def test():
    mazo1 = MazoPoker()
    mazo1.llenar()
    print(mazo1) 

if __name__ == '__main__':
    test()



