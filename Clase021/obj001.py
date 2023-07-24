

class Persona:
    def __init__(self,dni:int=0,nombre:str='',edad:int=0) -> None:   
        self.__dni:int = dni
        self.__nombre:str = nombre
        self.__edad:int = edad

    def setDni(self,dni:int)->None:
        self.dni = dni

    def getDni(self) -> int:
        return self.dni
    

    def setNombre(self,nombre:str)->None:
        self.__nombre = nombre

    def getNombre(self) -> str:
        return self.__nombre
    

    def setEdad(self,edad:int)->None:
        self.__edad = edad

    def getEdad(self) -> int:
        return self.__edad
    


    def __str__(self) -> str:
        return f'{self.__dni} {self.__nombre} {self.__edad}'




def main():
    p = Persona()

    print(p)

    p1 = Persona(96543142,"Juan",45)
    print(p1)
    a = int()
    print(a)





main()