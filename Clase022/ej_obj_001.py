"""
Implementar la clase CajaFuerte, que recibe en su constructor la cantidad de 
objetos que puede contener, y tiene los siguientes comportamientos:

c = CajaFuerte(12345,20)    
c.abrir(12345)
c.poner("Reloj")
c.poner("Cadena")
c.poner(1000)
c.cerrar()
c.poner("Reloj Oro") ==> ValueError ("La caja esta cerrada")
c.abrir(3456) ==> ValueError ("Error en la clave")
c.abrir(12345)
c.sacar("Cadena")
c.sacar("Tortuga")  ==> ValueError ("El objeto Tortuga no esta en la caja")
c.abrir(12345) ==> ValueError("La caja esta abierta")
c.cerrar()
"""

class CajaFuerte:

    def __init__(self,clave:int=123,cantidad_maxima:int=10) -> None:
        self.__clave:int=clave
        self.__cantidad_maxima:int=cantidad_maxima
        
        self.__elementos:list=[] 
        self.__estado:bool=False

    def __haylugar(self)->bool:
        return len(self.__elementos) < self.__cantidad_maxima

    def __iscerrada(self)->bool:
        return self.__estado == False

    def __isabierta(self)->bool:
        return not self.__iscerrada()

    def abrir(self,clave:int)->None:
        if self.__isabierta():
            raise ValueError("La caja ya esta abierta")
        if self.__clave != clave:
            raise ValueError("Error en la clave")
        self.__estado = True
    
    def cerrar(self)->None:
        if self.__iscerrada():
            raise ValueError("La caja ya esta cerrada")
        self.__estado = False
        

    def poner(self,elemento:object)->None:
        if self.__iscerrada():
            raise ValueError("No se puede poner en una caja cerrada")
        
        if not self.__haylugar():
            raise ValueError("No hay mas lugar")
        
        self.__elementos.append(elemento)


    def sacar(self,elemento:object)->object:
        if self.__iscerrada():
            raise ValueError("No se puede sacar de una caja cerrada")
        if elemento not in self.__elementos:
            raise ValueError("No esta!!")
        return self.__elementos.pop(self.__elementos.index(elemento))

    def ver(self,clave:int)->str:
        if self.__clave != clave:
            raise ValueError("Error en la clave")
        cadena = ''

        for elemento in self.__elementos:
            cadena += str(elemento) + '\n'

        return cadena

def main():
    c = CajaFuerte(12345,20)    
    c.abrir(12345)
    c.poner("Reloj")
    c.poner("Cadena")
    c.poner(1000)
    c.cerrar()
    #c.poner("Reloj Oro") #==> ValueError ("La caja esta cerrada")
    #c.abrir(3456) #==> ValueError ("Error en la clave")
    c.abrir(12345)
    c.sacar("Cadena")
    #c.sacar("Tortuga")#  ==> ValueError ("El objeto Tortuga no esta en la caja")
    # c.abrir(12345)# ==> ValueError("La caja esta abierta")
    c.cerrar()
    print(c.ver(12345))
main()