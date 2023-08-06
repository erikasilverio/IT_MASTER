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

    def getgesto(self)->int:
        return self.__gesto

    def __gesto_random(self)->int:
        return random.randint(1,3)
    
    def __str__(self) -> str:
        if self.__gesto == PIEDRA:
            return NOMBRE_PIEDRA
        elif self.__gesto == PAPEL:
            return NOMBRE_PAPEL
        else:
            return NOMBRE_TIJERA 



class Jugador:
    def __init__(self,nombre=None) -> None:
        self.__nombre = nombre
        self.__mano = Gesto()


    def hacer_gesto(self)-> None:
        self.__mano = Gesto()

    def getnombre(self)->str:
        return self.__nombre
    
    def getmano(self)->Gesto():
        return self.__mano


    def __str__(self) -> str:
        return f"{self.__nombre} ==> [{str(self.__mano)}]"
    

class Juego:
    def __init__(self,nomb_jug_1,nomb_jug_2) -> None:
        self.__jug1 = Jugador(nomb_jug_1)
        self.__jug2 = Jugador(nomb_jug_2)


    def __quien_gana(self)->Jugador:

        gesto1 = self.__jug1.getmano().getgesto()
        gesto2 = self.__jug2.getmano().getgesto()

        if gesto1 == gesto2:
            return None        
        elif gesto1 == PIEDRA and gesto2 == TIJERA:
            return self.__jug1
        
        elif gesto1 == PAPEL and gesto2 == PIEDRA:
            return self.__jug1
        elif gesto1 == TIJERA and gesto2 == PAPEL:
            return self.__jug1
        return self.__jug2


    def jugar(self)-> None:
        puntos_jugador1 = 0
        puntos_jugador2 = 0
        terminar = False
        ganador = Jugador()

        while not terminar:
            self.__jug1.hacer_gesto()
            print(self.__jug1)
            self.__jug2.hacer_gesto()
            print(self.__jug2)


            ganador = self.__quien_gana()


            if ganador == self.__jug1:
                puntos_jugador1 += 1
                print(f"Gana {self.__jug1.getnombre()}")
            elif ganador == self.__jug2:
                print(f"Gana {self.__jug2.getnombre()}")
                puntos_jugador2 += 1

            else:
                print("Empate")

            if puntos_jugador1 == 2 or puntos_jugador2 == 2:
                terminar = True

        print(f"Ganador: {ganador.getnombre()}")


        




def main():
    Juego("Juan","Maria").jugar()




main()


