

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
    

    def es_mayor_de_edad(self)->bool:
        return self.getEdad() > 18



    def __str__(self) -> str:
        return f'{self.__dni} {self.__nombre} {self.__edad}'
    

    

    def __eq__(self, __value: object) -> bool:
        pass




  

def main():
    p = Persona()
    p.setDni(963546352)
    p.setEdad(35)
    p.setNombre("Raul")

    print(p)

    p1 = Persona(96543142,"Juan",45)
    print(p1)
    a = int()
    print(a)



    if p.es_mayor_de_edad():
        print(f'{p.getNombre()} esmayor de Edad')

    
    if p1 == p:
        print(str(p1))
        print(str(p))
        print(p1)
        print(p)


    








main()