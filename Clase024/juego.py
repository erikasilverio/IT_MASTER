import random


PIEDRA = 1
NOMBRE_PIEDRA = "PIEDRA"

PAPEL = 2
NOMBRE_PAPEL = "PAPEL"

TIJERA = 3
NOMBRE_TIJERA = "TIJERA"



class Gesto:
    def __init__(self) -> None:
        self.__gesto = self.__gesto_random()



    def __gesto_random(self):
        return random.randint(1,3)
    
    def __str__(self) -> str:
        if self.__gesto == PIEDRA:
            return NOMBRE_PIEDRA
        elif self.__gesto == PAPEL:
            return NOMBRE_PAPEL
        else:
            return NOMBRE_TIJERA
        


class Jugador:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.__mano = Gesto

    def hacer_gesto(self)-> None:
        self.__mano = Gesto()

    def __str__(self) -> str:
        return f"{self.__nombre} ==> {str(self.__mano)}"

class Juego:
    def __init__(self,nomb_jug_1,nomb_jug_2) -> None:
        self.__jug1 = Jugador(nomb_jug_1)
        self.__jug2 = Jugador(nomb_jug_2)

    def jugar(self)->None:
        pass

def main():
    juego = Juego("Juan","Pinchame")

    juego.jugar()


main()