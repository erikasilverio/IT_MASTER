

class Persona:




    def __init__(self,dni:int=0,nombre:str='',edad:int=0) -> None:   
        self.__dni:int = dni
        self.__nombre:str = nombre
        self.__edad:int = edad

    def setDni(self,dni:int)->None:
        self.__dni = dni

    def getDni(self) -> int:
        return self.__dni
    

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
    

    
    # if p1 == p


    def __eq__(self, __otro_objeto: object) -> bool:
        if not isinstance(__otro_objeto,Persona):
            return False        
        return self.getDni() == __otro_objeto.getDni()
    
    
    def __ne__(self, __otro_obejeto: object) -> bool:
        return not self.__eq__(__otro_obejeto)





  

def main():
    p = Persona()
    p.setDni(9567854321)
    p.setEdad(35)
    p.setNombre("Raul")

    print(p)

    p1 = Persona(9678656432,"Juan",35)
    print(p1)
    a = int()
    print(a)



    if p.es_mayor_de_edad():
        print(f'{p.getNombre()} esmayor de Edad')

    
    if p1 == p1:
        print("Iguales")
        print(str(p1))
        print(str(p))
        print(p1)
        print(p)


        p2 = p1

        print("antes")
        print(p1)
        print(p2)


        p1.setNombre("huahauhauahuahu")

        print("depues") 
        print(p1)
        print(p2)








main()