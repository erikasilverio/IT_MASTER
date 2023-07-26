"""
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la
cantidad de localidades para el mismo; de modo tal que cumpla el siguiente comportamiento:

Ejemplo:

b = Boleteria("Rush",500)                       
print(b) ==> "Evento: Rush - Localidades vendidas: 0 de 500" 
print(b.localidades_agotadas()) ==>  False
b.vender_localidades(100)
b.vender_localidades(400)  
print(b.localidades_agotadas()) ==>  True
b.vender_localidades(200) ==> ValueError: No hay localidades suficientes     
print(b) "Evento: Rush - Localidades vendidas: 500 de 500"


Crear una clase TikeTon que permita la venta de localidades para distintos eventos.
La clase TikeTon debe tener un método inicio que permita agregar boleterías y vender
localidades para las mismas. El método inicio debe mostrar un menú con las opciones
disponibles y permitir al usuario elegir una de ellas. Las opciones disponibles son:

"""
import random
import pickle


class Boleteria:
    """
    Clase que implementa el comportamiento de una boleteria.
    """

    def __init__(self, nombre: str, disponibles: int = 100) -> None:
        if len(nombre) == 0 or disponibles <= 0:
            raise ValueError("Error en parametros.")
        self.__disponibles: int = disponibles
        self.__vendidas: int = 0
        self.__nombre: str = nombre

    def get_nombre(self) -> str:
        return self.__nombre

    def get_disponibles(self) -> int:
        return self.__disponibles

    def get_vendidas(self) -> int:
        return self.__vendidas

    def guardar(self) -> None:
        try:
            nombre_archivo = f"{self.__nombre}.pkl"
            with open(file=nombre_archivo, mode='wb') as archivo:
                pickle.dump(self, archivo)
        except Exception as e:
            print(f"Error: {nombre_archivo}\n{e}")

    def recuperar(self) -> None:
        try:
            nombre_archivo = f"{self.__nombre}.pkl"
            with open(file=nombre_archivo, mode='rb') as archivo:
                self = pickle.load(archivo)
        except IOError as e:
            print(f"Error: {nombre_archivo}\n{e}")

    def localidades_agotadas(self) -> bool:
        return self.__vendidas >= self.__disponibles

    def vender_localidades(self, cantidad: int):
        if self.localidades_agotadas():
            raise ValueError("Localidades Agotadas!!!")
        if cantidad > self.__disponibles:
            raise ValueError("Localidades insuficientes.")
        self.__vendidas += cantidad

    def __str__(self) -> str:
        return f"Evento: {self.__nombre} - Localidades Vendidas {self.__vendidas} de {self.__disponibles}"


class TikeTon:
    """
    Clase que implementa el comportamiento de un sistema de venta de localidades para distintos eventos.
    """

    def __init__(self) -> None:
        self.__nombre_archivo: str = "TikeTon.pkl"
        self.__boleterias: list[Boleteria] = []
        

    def __existe_archivo(self) -> bool:
        try:
            with open(file=self.__nombre_archivo, mode='rb') as archivo:
                return True
        except IOError:
            return False

    def __guardar(self) -> None:
        try:
            with open(file=self.__nombre_archivo, mode='wb') as archivo:
                pickle.dump(self, archivo)
        except Exception as e:
            print(f"Error: {self.__nombre_archivo}\n{e}")

    def __recuperar(self) -> None:
        if not self.__existe_archivo():
            self.__boleterias = []
            return
        try:
            with open(file=self.__nombre_archivo, mode='rb') as archivo:
                datos_recuperados = pickle.load(archivo)                
                self.__boleterias = datos_recuperados.__boleterias
        except IOError as e:
            print(f"Error: {self.__nombre_archivo}\n{e}")

    def __buscar_boleteria(self, nombre: str) -> Boleteria:
        for boleteria in self.__boleterias:
            if boleteria.get_nombre() == nombre:
                return boleteria
        return None

    def inicio(self) -> None:
        self.__recuperar()
        salir = False
        while not salir:
            print("1. Agregar Boleteria")
            print("2. Vender Localidades")
            print("3. Ver Boleterias")
            print("4. Salir")
            opcion = input("Ingrese opcion: ")
            if opcion == "1":
                nombre = input("Ingrese nombre del evento: ")
                disponibles = int(
                    input("Ingrese cantidad de localidades disponibles: "))
                boleteria = Boleteria(nombre, disponibles)
                self.__boleterias.append(boleteria)
            elif opcion == "2":
                nombre = input("Ingrese nombre del evento: ")
                cantidad = int(
                    input("Ingrese cantidad de localidades a vender: "))
                boleteria_encontrada = self.__buscar_boleteria(nombre)
                if boleteria_encontrada is not None:
                    boleteria_encontrada.vender_localidades(cantidad)
                    print(f"Localidades vendidas: {cantidad}")
            elif opcion == "3":
                for boleteria in self.__boleterias:
                    print(boleteria)
            elif opcion == "4":
                salir = True
        self.__guardar()


def main():    
    TikeTon().inicio()


if __name__ == '__main__':
    main()
