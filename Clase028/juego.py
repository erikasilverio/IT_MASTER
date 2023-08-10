import sys
sys.path.append('recursos/')

from mazos import MazoBlackJack
from cartas import CartaPoker
from txtcolores import strclr
from jugadores import Croupier,JugadorHumano,JugadorComputadora,Cliente
from typing import List
from random import randint
class BlackJack():
    

    def __init__(self,nombres:str=None) -> None:
        self.__color_alerta:int = 196       
        self.__color_sitema:int = 15        
        self.__croupioer:Croupier = Croupier()
        self.__jugadores:List[Cliente] = []
        self.__mazo:MazoBlackJack = MazoBlackJack()
        self.__mazo.llenar()
        if nombres:
            for nombre in nombres.split(','):
                self.__jugadores.append(JugadorComputadora(nombre,randint(100,1000)))

    def agregar_jugador(self,cliente:Cliente) -> None:
        """
        Agrega un jugador al juego.

        Args:
            cliente (Cliente): Cliente a agregar.
        """
        if not isinstance(cliente,Cliente):
            raise TypeError('El jugador debe ser un objeto de tipo Cliente.')
        self.__jugadores.append(cliente)

def test():
    juego = BlackJack('C_Juan,C_Pepe,C_Carlos')
    juego.agregar_jugador(JugadorHumano('Raul',1000))
    print(juego)


if __name__ == '__main__':
    test()