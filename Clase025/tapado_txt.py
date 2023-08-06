
from os import system
from time import sleep
from random import choice, randint

LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def cara_random() -> str:
    cara = ""
    for x in range(3):
        cara += choice(LETRAS)
    return cara


FILAS = 2
COLUMNAS = 2
NADA = '---'
FONDO = '###'


class Ficha():
    def __init__(self, cara: str = None, tapada: bool = True) -> None:
        if cara == None:
            self.cara = cara = NADA
        else:
            self.cara = cara
        self.fondo = FONDO
        self.tapada = tapada

    def get_cara(self) -> str:
        return self.cara

    def istapada(self) -> bool:
        return self.tapada

    def destapar(self) -> None:
        self.tapada = False

    def tapar(self) -> None:
        self.tapada = True

    def __str__(self) -> str:
        cadena = ''
        if self.istapada():
            cadena = self.fondo
        else:
            cadena = self.cara
        return f'[{cadena}]'

    def isvacia(self) -> bool:
        return self.cara == NADA

    def __eq__(self, otra_ficha: object) -> bool:
        iguales = False
        if isinstance(otra_ficha, Ficha) and self.cara == otra_ficha.cara:
            iguales = True
        return iguales


class Tablero():
    def __init__(self) -> None:
        self.tablero = self.crear()
        self.llenar()

    def getficha(self, f: int, c: int) -> Ficha:
        return self.tablero[f][c]

    def destapar(self) -> None:
        for f in range(FILAS):
            for c in range(COLUMNAS):
                self.tablero[f][c].destapar()

    def contar_tapadas(self) -> int:
        cantidad_tapadas = 0
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if self.getficha(f, c).istapada():
                    cantidad_tapadas += 1
        return cantidad_tapadas

    def destapar_celda(self, f: int, c: int) -> None:
        self.tablero[f][c].destapar()

    def tapar_celda(self, f: int, c: int) -> None:
        self.tablero[f][c].tapar()

    def crear(self) -> list:
        filas = []
        for f in range(FILAS):
            columnas = []
            for c in range(COLUMNAS):
                columnas.append(Ficha())
            filas.append(columnas)
        return filas

    def isvacio(self, fila: int, columna: int) -> bool:
        return self.tablero[fila][columna].isvacia()

    def poner(self, fila: int, columna: int, ficha: Ficha) -> None:
        self.tablero[fila][columna] = ficha

    def existe(self, ficha: Ficha) -> bool:
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if self.tablero[f][c] == ficha:
                    return True
        return False

    def __str__(self) -> str:
        cadena = "     "
        for c in range(COLUMNAS):
            cadena += f'{str(c+1).center(5)}'
        cadena += '\n'
        for f in range(FILAS):
            cadena += f'{str(f+1).center(5)}'
            for c in range(COLUMNAS):
                cadena += str(self.tablero[f][c])
            cadena += '\n'
        return cadena

    def llenar(self) -> None:
        contar = 0  # TENGO QUE PONER 50 FICHAS
        while contar < FILAS*COLUMNAS//2:  # MIENTRAS NO SE COMPLETE EL TABLERO
            cad = cara_random()
            ficha1 = Ficha(cad)  # OBTENGO UNA FICHA RANDOM
            ficha2 = Ficha(cad)
            if not self.existe(ficha1):  # SI NO EXISTE LA FICHA EN EL TABLERO
                # BUSCO LUGAR PARA LA PRIMERA FICHA
                encontre_lugar = False  # LE TENGO QUE BUSCAR UN LUGAR VACIO
                while not encontre_lugar:  # MIENTRAS NO ENCUENTRO UN LUGAR VACIO
                    f = randint(0, FILAS - 1)  # OBTENGO UNA FILA CUALQUIERA
                    # OBTENNGO UNA COLUMNA CUALQUIERA
                    c = randint(0, COLUMNAS-1)
                    if self.isvacio(f, c):  # SI NO HAY FICHA
                        # PONGO LA FICHA EN EL LUGAR VACIO
                        self.poner(f, c, ficha1)
                        encontre_lugar = True  # ROMPER EL CICLO DE NO ENCONTRE LUGAR
                # BUSCO LUGAR PARA LA SEGUNDA FICHA
                encontre_lugar = False
                while not encontre_lugar:
                    f = randint(0, FILAS - 1)
                    c = randint(0, COLUMNAS-1)
                    if self.isvacio(f, c):
                        self.poner(f, c, ficha2)
                        encontre_lugar = True
                contar += 1  # CUENTO UNA FICHA MAS EN EL TABLERO




class Juego():
    def __init__(self, nombre: str) -> None:
        self.nombre_jug = nombre
        self.tablero = Tablero()

    def leer_coordenadas(self) -> tuple:
        f = 0
        c = 0
        todo_ok = False
        while not todo_ok:
            f=int(input("Fila: "))-1
            c=int(input("Columna: "))-1
            if self.tablero.getficha(f,c).istapada():
                todo_ok = True
        return (f, c)

    def jugar(self):
        puntos = 0
        terminar = False
        while not terminar:
            system('cls')
            print(self.tablero)
            print(f'Juega: {self.nombre_jug:25s}')
            f1, c1 = self.leer_coordenadas()
            self.tablero.destapar_celda(f1, c1)
            system('cls')
            print(self.tablero)
            print(f'Juega: {self.nombre_jug:25s}')
            f2, c2 = self.leer_coordenadas()
            self.tablero.destapar_celda(f2, c2)
            
            if self.tablero.getficha(f1,c1) != self.tablero.getficha(f2,c2):
                system('cls')
                print(self.tablero)
                sleep(2)
                self.tablero.tapar_celda(f1,c1)
                self.tablero.tapar_celda(f2,c2)

            puntos += 1    



            if self.tablero.contar_tapadas() == 0:
                terminar = True
        system('cls')
        print(self.tablero)
        print(f"Cantidad de movimientos: {puntos}")

def main():
    # t = Tablero()
    # print(t)
    # t.destapar()
    # print(t)

    #f1 = Ficha()
    # print(f1,f1.isvacia())

    # f2 = Ficha('ABC')
    # print(f2)
    # f2.tapar()
    # print(f2)
    # f2.destapar()
    # print(f2)
    # print("vacia: ",f2.isvacia())

    juego = Juego("Pepe")
    juego.jugar()

main()
